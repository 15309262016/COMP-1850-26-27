# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music_database = {
    "The Beatles": ["Abbey Road", "Let It Be", "Sgt. Pepper's Lonely Hearts Club Band"],
    "Pink Floyd": ["The Dark Side of the Moon", "Wish You Were Here", "Animals"],
    "Led Zeppelin": ["Led Zeppelin IV", "Physical Graffiti", "Houses of the Holy"]  
}

# Pretty-print the data structure
pprint(music_database)

# Display details of one album recorded by a specific artist
print("First album by The Beatles:", music_database["The Beatles"][0])

# Additional work: count the total number of albums in the database
print("Total albums:", sum(len(albums) for albums in music_database.values()))
