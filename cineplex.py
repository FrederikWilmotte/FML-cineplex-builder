# Fantasy Movie League cineplex builder
# Author: Frederik Wilmotte

import csv
from itertools import combinations_with_replacement


# Define class movie
class movie:
    def __init__(self, name, prediction, value):
        self.name = name
        self.prediction = float(prediction)
        self.value = float(value)


# Read input file
movies = []
with open('movies.csv') as movieFile:
    movieLine = csv.reader(movieFile)
    for element in movieLine:
        movieData = movie(element[0], element[1], element[2])
        movies.append(movieData)

# The total budget of the cineplex
totalBudget = 1000

# The number of movies you can display
nrMovies = 8

# The best prediction within budget so far (initialize)
bestPrediction = 0
bestBudget = 0

# All possible combinations with the given movies
allPossibleMovieCombinations = combinations_with_replacement(movies, nrMovies)

for movieCombination in allPossibleMovieCombinations:
    # for each combination of movies, calculate the prediction and the budget
    cineBudget = 0
    cinePrediction = 0
    for movieData in movieCombination:
        # Makes the sum of the predictions and budget for this combination of movies
        cineBudget += movieData.value
        cinePrediction += movieData.prediction

    if cineBudget <= totalBudget:
        # Only check the combination that don't exceed the budget
        if cinePrediction > bestPrediction:
            # Save the combination with the highest prediction
            bestPrediction = cinePrediction
            bestBudget = cineBudget
            bestMovieCombination = movieCombination

# Print the results
print("---Best Movie Combination:--")
for movieData in bestMovieCombination:
    print(movieData.name)
print("==> Prediction:", round(bestPrediction, 1))
print("==> Budget:", round(bestBudget, 1))
