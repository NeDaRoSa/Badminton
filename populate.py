import os


def populate():
    add_location('Glasgow Club Gorbals',
                 275,
                 'Ballater St',
                 'G5 0YP',
                 'Glasgow club near Glasgow Green. Phone: 0141 276 1490',
                 'http://www.glasgowlife.org.uk/sport/glasgow-club/gorbals/pages/home.aspx',
                 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5327.1149087834565!2d-4.248403052216435!3d55.84920321146375!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x488846bd21982bd3%3A0x3067f1e84ae37204!2sGlasgow%2C+Glasgow+City+G5+0YP!5e0!3m2!1sen!2suk!4v1449439799110')

    add_location('Glasgow Club Holyrood',
                 505,
                 'Aikenhead Rd',
                 'G42 0PD',
                 'Glasgow club in the south side. Phone: 0141 276 1500',
                 'http://www.glasgowlife.org.uk/sport/glasgow-club/holyrood/Pages/home.aspx',
                 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4481.540037462443!2d-4.250693739471702!3d55.83195101336835!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x488846e9b2cec517%3A0x772f782587ee0901!2sGlasgow%2C+Glasgow+City+G42+0PD!5e0!3m2!1sen!2suk!4v1449439890722')

    add_location('Glasgow Club Scotstoun',
                 72,
                 'Danes Dr',
                 'G14 9HD',
                 'Phone: 0141 276 1620',
                 'http://www.glasgowlife.org.uk/sport/glasgow-club/scotstoun/pages/home.aspx',
                 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5322.6525798128705!2d-4.345866993350715!3d55.88175380436904!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x488845f540c10a1f%3A0x11c2e76b9cab4104!2sGlasgow%2C+Glasgow+City+G14+9HD!5e0!3m2!1sen!2suk!4v1449439934676')


def add_location(name, street_number, street, postcode, description, url, embed_url):
    loc = Location.objects.get_or_create(name=name,
                                         street_number=street_number,
                                         street=street,
                                         postcode=postcode,
                                         description=description,
                                         url=url,
                                         embed_url=embed_url)
    return loc


if __name__ == '__main__':
    print('Starting population script.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gtc_badminton.settings')
    from birdie.models import Location
    populate()