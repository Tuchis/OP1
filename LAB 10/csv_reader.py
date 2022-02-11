import csv
from typing import Iterator

path = "title.ratings.tsv"

with open(path, 'r') as csv_file:
    ratings_reader = csv.reader(csv_file)
    print(type(ratings_reader), isinstance(ratings_reader, Iterator))
    print(len([row for row in ratings_reader]))


x_file = open('top_ratings.csv', 'w')
ratings_writer = csv.writer(x_file, delimiter=",")

with open(path, 'r', newline='') as csv_file:
    ratings_reader_dict = csv.DictReader(csv_file, delimiter='\t')
    #print(len([row for row in ratings_reader_dict]))
    for row in ratings_reader_dict:
        if float(row['averageRating']) > 9 and int(row['numVotes']) > 1000:
            ratings_writer.writerow((row['tconst'], row['averageRating']))

x_file.close()
