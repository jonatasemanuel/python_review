def get_formatted_name():
    while True:
        print('Please tell me your name.' )
        print("(Enter 'q' at aby time to quit)")
        f_name = str(input('First name: ')) 
        if f_name == 'q': break
        l_name = str(input('Last name: '))
        if l_name == 'q': break
        full_name = f_name + ' ' + l_name
        return full_name.title()


formatted_name = get_formatted_name()
print(f'Hello, {formatted_name} !')

def city_country(city, country):
    formatted = city + ', '+ country
    return formatted.title()


town = city_country('sao paulo', 'brazil')
print(town)


def make_album(artist='', album='', n_tracks=''):
    while True:
        # if n_tracks:
        print('(For stop press "q")')
        artist = str(input('Please tell me a artist name: '))
        if artist == 'q': break
        album = str(input('The album name: '))
        if album == 'q': break
        n_tracks = int(input('Tracks: '))
        if n_tracks == 'q': break
        complete = {'artist': artist, 'album': album, 'n_tracks': n_tracks}
        return complete


alb = make_album()
print(alb)
