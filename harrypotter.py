max_opening_weekend = 0
max_movie_name = []

with open('harry-potter.txt') as movie_file:
    movie_file.readline() # this skips the header row
    for line in movie_file:
        line = line.strip()
        movie_data = line.split(',')
        opening_weekend = int(movie_data[3]) # data  [3] is the opening weekend amount
        if opening_weekend > max_opening_weekend:
            max_opening_weekend = opening_weekend
            max_movie_data = movie_data[0] #data [0]is the name of the movie


print(f'Movie: {max_movie_data[0]}')
print(f'Highest opening weekend was ${max_opening_weekend:,}.')
print(f'Release on:{max_movie_data [5]}')
print(f'lifetime gross of ${')
print(f'Highest opening weekend; {max_movie_name} with ${max_opening_weekend:,}.')
