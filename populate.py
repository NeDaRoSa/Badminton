import os


def populate():
    add_location('Glasgow Club Gorbals',
                 275,
                 'Ballater St',
                 'G5 0YP',
                 'Glasgow club near Glasgow Green. Phone: 0141 276 1490',
                 'http://www.glasgowlife.org.uk/sport/glasgow-club/gorbals/pages/home.aspx')

    add_location('Glasgow Club Holyrood',
                 505,
                 'Aikenhead Rd',
                 'G42 0PD',
                 'Glasgow club in the south side. Phone: 0141 276 1500',
                 'http://www.glasgowlife.org.uk/sport/glasgow-club/holyrood/Pages/home.aspx')

    add_location('Glasgow Club Scotstoun',
                 72,
                 'Danes Dr',
                 'G14 9HD',
                 'Phone: 0141 276 1620',
                 'http://www.glasgowlife.org.uk/sport/glasgow-club/scotstoun/pages/home.aspx')


def add_location(name, street_number, street, postcode, description, url):
    loc = Location.objects.get_or_create(name=name,
                                         street_number=street_number,
                                         street=street,
                                         postcode=postcode,
                                         description=description,
                                         url=url)
    return loc


if __name__ == '__main__':
    print('Starting population script.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gtc_badminton.settings')
    from birdie.models import Location
    populate()