from datetime import datetime
from django import forms
from django.contrib.auth.forms import PasswordChangeForm as PwForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget
from birdie.models import Location, Game


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label=_("Password"))
    password2 = forms.CharField(max_length=30, min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label=_("Password Confirmation"),
                                help_text=_("Enter the same password as before, for verification."))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class GameEditForm(forms.ModelForm):

    _datetime_options = {
        'pickerPosition': 'bottom-left',
        'format': 'dd/mm/yyyy hh:ii',
        'startDate': '%s-%s-%s' % (datetime.now().year, datetime.now().month, datetime.now().day),
        'minuteStep': '30'
    }

    location = forms.ModelChoiceField(required=True, queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control'}))
    datetime = forms.DateTimeField(widget=DateTimeWidget(attrs={'id': 'datetimepicker'},bootstrap_version=3, options=_datetime_options), input_formats=['%d/%m/%Y %H:%M',],
                                   label='Date and time')
    duration = forms.ChoiceField(choices=[(x,x) for x in range(1, 5)], widget=forms.Select(attrs={'class': 'form-control'}),
                                 required=True, initial='1', label='Duration (hours)')
    max_players = forms.ChoiceField(choices=[(x,x) for x in range(2, 16)], widget=forms.Select(attrs={'class': 'form-control'}), required=True, initial='4')

    class Meta:
        model = Game
        fields = ('location', 'description', 'datetime', 'duration', 'max_players')


class GameForm(GameEditForm):
    name = forms.CharField(max_length=30, min_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Game
        fields = ('name', 'location', 'description', 'datetime', 'duration', 'max_players')


class PasswordChangeForm(PwForm):
    old_password = forms.CharField(label=_("Old password"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
