#Defining the imports
from os import path

#Defining the directory everything is saved in
DATA_DIR = '/Users/mohamed.alzarai/Desktop/Git/Tracking Artist Mental Health Through Lyrical Evolution'
#Defining the file path and names for all files to be opened and used
song_file = open(path.join(DATA_DIR,'Kanye West Discography/College Dropout (2004)/We Dont Care.txt'),'r')
positive_words_file = open(path.join(DATA_DIR,'positive_words.txt'),'r')

#Extracting the contents of each file 
song_lyrics = [word.lower() for word in song_file.read().split()]
positive_words = positive_words_file.read().split()

#Defining a function that gets the number of positive words in a song
def positive_word_per_song(song,words):
    p_word_count = 0
    for word in words:
        for lyric in song:
            if lyric == word:
                p_word_count+=1
    print(p_word_count)

positive_word_per_song(song_lyrics,positive_words)