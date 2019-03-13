import csv
filename = 'data.csv'

all_albums = []

with open(filename) as f:
    reader = csv.DictReader(f)
    temp_all_albums = [dict(row) for row in reader]
    print(temp_all_albums)

for album in temp_all_albums:
    album['number'] = int(album['number'])
    album['year'] = int(album['year'])
    all_albums.append(album)

def find_album(album_name):
    solution = None
    for album in all_albums:
        if album['album'] == album_name:
            solution = album
    return solution

def find_rank(album_rank):
    solution = None
    for album in all_albums:
        if album['number'] == album_rank:
            solution = album['album']
    return solution

def find_by_year(year):
    solution = []
    for album in all_albums:
        if album['year'] == year:
            solution.append(album['album'])
    return solution

def find_by_years(start_year, end_year):
    solution = []
    for album in all_albums:
        if album['year'] >= start_year and album['year'] <= end_year:
            solution.append(album['album'])
    return solution

def find_by_ranks(start_rank, end_rank):
    solution = []
    for album in all_albums:
        if album['number'] > start_rank and album['number'] < end_rank:
            solution.append(album['album'])
    return solution

def all_titles():
    return [album['album'] for album in all_albums]

def all_artists():
    return [album['artist'] for album in all_albums]

def most_appearances():
    album_count_by_artist = {}

    for album in all_albums:
        album_count_by_artist[album['artist']] = album_count_by_artist.get(album['artist'], 0) + 1
    max_apperances = sorted(album_count_by_artist.items(), key=lambda x: x[1], reverse=True)
    max_num = max_apperances[0][1]

    return [key for (key, value) in album_count_by_artist.items() if value == max_num]
    
def most_popular():
    all_words = []
    for album in all_titles():
        all_words += album.split()

    word_count = {}
    for word in all_words:
        word_count[word] = word_count.get(word, 0) + 1

    max_appearances = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print('"{}" appears {} times'.format(max_appearances[0][0], max_appearances[0][1]))
    
def albums_by_year():
    by_year = {}
    for album in all_albums:
        by_year[album['year']] = by_year.get(album['year'], 0) + 1
    return  sorted(by_year.items(), key=lambda x: x[0], reverse=True)

def genre_counts():
    by_genre = {}
    for album in all_albums:
        by_genre[album['genre']] = by_genre.get(album['genre'], 0) + 1
    return sorted(by_genre.items(), key=lambda x: x[1], reverse=True)

text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()

def string_to_list(string):
    all_songs = []
    for line in string:
        all_songs.append(((line.rstrip()).split('\t')))
    return all_songs

def list_to_dict(_list):
    songs_dict = [{'RANK': Rank, 'NAME': Name, 'ARTIST': Artist, 'YEAR': Year} for (Rank, Name, Artist, Year) in _list]
    return songs_dict


# print(find_album('The Sun Sessions'))
# print(find_rank(11))
# print(find_by_year(1976))
# print(find_by_years(1976, 1977))
# print(find_by_ranks(1, 10))
# print(all_titles())
# print(all_artists())
# print(most_appearances())
# most_popular()
# print(albums_by_year())
# print(genre_counts())
# songs_list = string_to_list(lines)
# print(list_to_dict(songs_list))

