import csv

#read the files for movies
def read_movies(filename: str):
    movies = {}
    with open(filename, "r", encoding="utf-8", newline="") as source_file:
        reader = csv.reader(source_file)
        next(reader)
        for row in reader:
            movie = (row[1], row[2])
            movies[movie] = row[3]
    return movies
#read the file for casts
def read_casts(filename: str):
    casts = {}
    with open(filename, "r", encoding="utf-8", newline="") as source_file:
        reader = csv.reader(source_file)
        for row in reader:
            movie = (row[0], row[1])
            actors = []
            for actor in row[3:]:
                if actor != "" and actor not in actors:
                    actors.append(actor)
            casts[movie] = (row[2], actors)
    return casts

def get_total(entry: tuple):
    return entry[-1]
#create ranking base on file
def display_ranking(totals: dict, limit: int | None = 10):
    ranking = []
    for names, total in totals.items():
        ranking.append(names + (total,))
    ranking.sort(key=get_total, reverse=True)
    if limit is not None:
        if limit < 0:
            raise ValueError("The display limit cannot be negative, duh.")
        ranking = ranking[:limit]
    position = 1
    for entry in ranking:
        print("{:2}. {}".format(position, entry))
        position = position + 1

def display_top_collaborations(movies: dict, casts: dict, limit: int | None = 10):
    totals = {}
    for movie in movies:
        director, actors = casts[movie]
        for actor in actors:
            pair = (director, actor)
            if pair not in totals:
                totals[pair] = 0
            totals[pair] = totals[pair] + 1
    display_ranking(totals, limit)

def display_top_actors(movies: dict, casts: dict,
                       limit: int | None = 10) -> None:
    totals = {}
    for movie in movies:
        actors = casts[movie][1]
        box_office = int(movies[movie])
        for actor in actors:
            name = (actor,)
            if name not in totals:
                totals[name] = 0
            totals[name] = totals[name] + box_office
    display_ranking(totals, limit)
#part C: testing the code
def main() -> None:
    try:
        print("Name: Minh Hy Phan")
        print("FAU ID: Z23766758")
        rated = read_movies("imdb-top-rated.csv")
        grossing = read_movies("imdb-top-grossing.csv")
        casts = read_casts("imdb-top-casts.csv")
        limit = 10  #showing top 10 results
        print("\nPart a: Top director-actor collaborations")
        display_top_collaborations(rated, casts, limit)
        print("\nPart b: Top actors by total USA box office (USD)")
        display_top_actors(grossing, casts, limit)
    except Exception:
        print("Error! Please check the codes and files and try again, dear manager.")
        raise

if __name__ == "__main__":
    main()