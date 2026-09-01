from tmdb_api import movie_search

# user enters a movie name and its searched for using the api
movie_name = input("Enter a movie: ")
results = movie_search(movie_name)

# checking if the movie exists
if results and results["results"]:
    print("\nSearch Results: \n")
    for i, movie in enumerate(results["results"]):#
        # prints the number, title, release date
        print(f"{i}. {movie['title']} ({movie['release_date'][:4]})")
        # prints the rating, vote average
        print(f"Rating: {movie['vote_average']}")
        print()




















else:
    print("Movie not found.")