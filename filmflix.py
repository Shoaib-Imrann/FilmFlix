# cine_match.py

# List to store movies
movies = []

# Function to add a new movie
def add_movie(title, genre, rating):
    movie = {
        'title': title,
        'genre': genre,
        'rating': rating
    }
    movies.append(movie)
    print(f"Movie '{title}' added successfully!")

# Function to search for movies by title or genre
def search_movies(search_term, search_type='title'):
    results = [movie for movie in movies if search_term.lower() in movie[search_type].lower()]
    return results

# Function to recommend top N movies based on rating
def recommend_top_movies(n):
    sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)
    return sorted_movies[:n]

# Function to delete a movie by title
def delete_movie(title):
    global movies
    movies = [movie for movie in movies if movie['title'].lower() != title.lower()]
    print(f"Movie '{title}' deleted successfully!")

# Function to display the movie list
def display_movies():
    if not movies:
        print("No movies in the list.")
    else:
        for movie in movies:
            print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")

# Interactive CLI for the movie recommendation system
def cine_match():
    while True:
        print("\nWelcome to Filmflix!")
        print("1. Add a new movie")
        print("2. Search for movies")
        print("3. Recommend top N movies")
        print("4. Delete a movie")
        print("5. Display all movies")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            rating = float(input("Enter the movie rating: "))
            add_movie(title, genre, rating)
        elif choice == '2':
            search_type = input("Search by title or genre? ")
            search_term = input(f"Enter the {search_type}: ")
            results = search_movies(search_term, search_type)
            if results:
                for movie in results:
                    print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
            else:
                print(f"No movies found for {search_type} '{search_term}'.")
        elif choice == '3':
            n = int(input("Enter the number of top movies to recommend: "))
            recommendations = recommend_top_movies(n)
            if recommendations:
                for movie in recommendations:
                    print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
            else:
                print("No movies to recommend.")
        elif choice == '4':
            title = input("Enter the title of the movie to delete: ")
            delete_movie(title)
        elif choice == '5':
            display_movies()
        elif choice == '6':
            print("Exiting CineMatch. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the interactive CLI
cine_match()
