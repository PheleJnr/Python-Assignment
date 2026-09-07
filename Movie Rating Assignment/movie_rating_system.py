from datetime import datetime


class Movie:
    
    def __init__(self, name):
    
        self.name = name
        
        self.date_added = datetime.now()
        
        self.ratings = []  

    def get_formatted_date_added(self):
    
        return self.date_added.strftime("%Y-%m-%d %H:%M:%S")

    def add_rating(self, rating):    

        self.ratings.append(rating)

    def get_number_of_ratings(self):
    
        return len(self.ratings)

    def get_average_rating(self):
    
        if len(self.ratings) == 0:
        
            return 0.0

        total = 0
        
        for rating in self.ratings:
        
            total += rating

        return total / len(self.ratings)  

    def has_name(self, other_name):
    
        return self.name.lower() == other_name.lower()

    def __str__(self):
    
        count = self.get_number_of_ratings()
        
        plural = "" if count == 1 else "s"
        
        return (f"{self.name} (added {self.get_formatted_date_added()}) - "
                f"Average rating: {self.get_average_rating():.2f} ({count} rating{plural})")


def find_movie(movies, name):
    
    for movie in movies:
    
        if movie.has_name(name):
        
            return movie
            
    return None


def is_valid_movie_name(name):

    if name is None:

        return False

    name = name.strip()

    if name == "":

        return False
   
    if not any(character.isalnum() for character in name):

        return False

    return True


def add_movie(movies, name):
    
    name = name.strip() if name is not None else ""

    if not is_valid_movie_name(name):

        return False, "Invalid movie name. Movie not added."

    if find_movie(movies, name) is not None:
    
        return False, f'Movie "{name}" already exists. Not adding a duplicate.'

    movies.append(Movie(name))
    
    return True, f'Movie "{name}" added!'


def rate_movie(movies, name, rating_text):
   
    movie = find_movie(movies, name)
    
    if movie is None:
    
        return False, f'Movie "{name}" was not found. Add it first.'

    try:
    
        rating = int(rating_text)
        
    except ValueError:
    
        return False, "That's not a valid number. Rating not added."

    if rating < 1 or rating > 5:
    
        return False, "Rating must be between 1 and 5. Rating not added."

    movie.add_rating(rating)
    
    return True, f"Rating added for '{movie.name}': {rating}"


def get_average_rating_message(movies, name):

    movie = find_movie(movies, name)
    
    if movie is None:
    
        return f'Movie "{name}" was not found.'

    if movie.get_number_of_ratings() == 0:
    
        return f"'{movie.name}' has no ratings yet."

    return f"Average rating for '{movie.name}': {movie.get_average_rating():.2f}"


def get_all_average_ratings_lines(movies):
  
    lines = []
    
    for movie in movies:
    
        if movie.get_number_of_ratings() == 0:
        
            lines.append(f"- {movie.name}: no ratings yet")
            
        else:
        
            lines.append(f"- {movie.name}: {movie.get_average_rating():.2f}")
            
    return lines


def print_menu():

    print("1. Add a Movie")
    print("2. Rate a Movie")
    print("3. Get Average Rating for a Movie")
    print("4. Get Average Ratings of All Movies")
    print("5. Exit")


def main():

    movies = []
    
    running = True

    while running:
    
        print_menu()
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
        
            name = input("Enter the movie name: ")
            
            success, message = add_movie(movies, name)
            
            print(message)

        elif choice == "2":
        
            if not movies:
            
                print("No movies have been added yet. Add a movie first.")
                
            else:
            
                name = input("Enter the movie name: ")
                
                rating_text = input("Enter your rating (1-5): ")
                
                success, message = rate_movie(movies, name, rating_text)
                
                print(message)

        elif choice == "3":
        
            if not movies:
            
                print("No movies have been added yet.")
                
            else:
            
                name = input("Enter the movie name: ")
                
                print(get_average_rating_message(movies, name))

        elif choice == "4":
        
            if not movies:
            
                print("No movies have been added yet.")
                
            else:
            
                print("Average Ratings:")
                
                for line in get_all_average_ratings_lines(movies):
                
                    print(line)

        elif choice == "5":
        
            print("Exiting the application. Goodbye!")
            
            running = False

        else:
        
            print("Invalid choice. Please enter a number from 1 to 5.")

        print() 


if __name__ == "__main__":
    main()
