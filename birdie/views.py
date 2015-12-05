from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.views import password_change
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from birdie.forms import UserForm, GameForm, PasswordChangeForm
from birdie.models import Game


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')

            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'login.html', {})


@login_required()
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('/')


@login_required()
def home(request):
    return render(request, 'home.html', {})


def register(request):
    registered = False
    passphrase_error = None

    if request.method == 'POST':
        code = request.POST.get('passphrase', '')
        user_form = UserForm(data=request.POST)
        if code != 'CHANGE_THIS':
            passphrase_error = 'The passphrase you entered is incorrect.'
        else:
            if user_form.is_valid():
                user = user_form.save()
                password = request.POST.get('password1', '')
                print(password)

                user = authenticate(username=user.username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'registered': registered, 'passphrase_error': passphrase_error})


@login_required()
def create_game(request):
    created = False

    if request.method == 'POST':
        game_form = GameForm(data=request.POST)

        if game_form.is_valid():
            game = game_form.save(commit=False)
            game.organiser = request.user
            game.save()

            game.players.add(request.user)
            game.save()
            created = True
        else:
            print(game_form.errors)

    else:
        game_form = GameForm()

    return render(request, 'create_game.html', {'game_form': game_form, 'created': created})


@login_required()
def upcoming_games(request):
    games = Game.objects.filter(datetime__gt=timezone.now())

    return render(request, 'game_list.html', {'games': games, 'title': 'Upcoming games'})


@login_required()
def my_games(request):
    games = request.user.organised_games.all()

    return render(request, 'game_list.html', {'games': games, 'title': 'Games I organise(d)'})


@login_required()
def joined_games(request):
    games = request.user.games.all()

    return render(request, 'game_list.html', {'games': games, 'title': 'Games I joined'})


@login_required()
def past_games(request):
    games = Game.objects.filter(datetime__lt=timezone.now())

    return render(request, 'game_list.html', {'games': games, 'title': 'Past games'})


@login_required()
def game(request, game_id):
    my_game = Game.objects.get(id=game_id)

    just_joined = False
    has_joined = False
    is_past_game = my_game.datetime < timezone.now()

    if request.method == 'POST':
        if request.POST.get('action_type', '') == 'add':
            if len(my_game.players.all()) < my_game.max_players:
                my_game.players.add(request.user)
        elif request.POST.get('action_type', '') == 'remove':
            my_game.players.remove(request.user)

        just_joined = True

    if my_game.players.filter(id=request.user.id):
        has_joined = True

    empty_list = range(0, my_game.max_players - len(my_game.players.all()))

    context_dict = {
        'game': my_game,
        'has_joined': has_joined,
        'just_joined': just_joined,
        'empty_list': empty_list,
        'is_past_game': is_past_game
    }

    return render(request, 'game.html', context_dict)


@login_required()
def members(request):
    users = User.objects.filter(is_staff=False)

    return render(request, 'members.html', {'users': users})


@login_required()
def update_password(request):
    return password_change(request, post_change_redirect='/password_updated/', password_change_form=PasswordChangeForm)


@login_required()
def password_updated(request):
    return render(request, 'registration/password_updated.html', {})


def bad_request(request):
    response = render(request, 'error.html', {'error_message': '400 - Bad request.'})
    response.status_code = 400
    return response


def permission_denied(request):
    response = render(request, 'error.html', {'error_message': '403 - Permission denied.'})
    response.status_code = 403
    return response


def page_not_found(request):
    response = render(request, 'error.html', {'error_message': '404 - Requested page was not found.'})
    response.status_code = 404
    return response


def server_error(request):
    response = render(request, 'error.html', {'error_message': '500 - Unexpected server error.'})
    response.status_code = 500
    return response
