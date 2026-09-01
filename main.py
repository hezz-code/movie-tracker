from tmdb_api import movie_search

movie_name = input("Enter a movie: ")
results = movie_search(movie_name)

if results and results["results"]:
    movie = results["results"][0]

    print("")
    print("Title: ", movie["title"])
    print("Release Date: ", movie["release_date"])
    print("Rating: ", movie["vote_average"])
    print("Overview: ", movie["overview"])

else:
    print("Movie not found.")