import random

# Take user input of number of songs and song metadata
nr_of_songs = int(input())

raw_songs = []
raw_song = []

for i in range(nr_of_songs):
    raw_song = input().split()
    raw_songs.append(raw_song)

# Create a function that would spit up a shuffled list of songs
def shuffledsongs(songs):
    song_dict = {}
    songs_to_play = []
    final_song_list = []
    # Create a dictionary mapping between Album ID and song name
    for i in songs:
        if i[1] in song_dict:
            song_dict[i[1]].append(i[2])
        else:
            song_dict[i[1]] = [i[2]]
    # Shuffle albums
    shuffled_albums = random.sample(list(song_dict.keys()), len(list(song_dict.keys())))
    # Creat a shuffled list of songs with non-overlaping albums
    for j in shuffled_albums:
        if j in song_dict:
            song = sorted(song_dict[j])
            random_title = random.choice(song)
            for song_meta in songs:
                if song_meta[1]==j and song_meta[2]==random_title:
                    final_song_list.append(song_meta)
    return final_song_list

print(shuffledsongs(raw_songs))
