import unittest
from movie_rating_system import (

    Movie,
    find_movie,
    add_movie,
    rate_movie,
    get_average_rating_message,
    get_all_average_ratings_lines,
)


class TestMovie(unittest.TestCase):

    def test_that_new_movie_has_zero_ratings_and_zero_average(self):
    
        movie = Movie("Inception")

        self.assertEqual(0, movie.get_number_of_ratings())
        self.assertEqual(0.0, movie.get_average_rating())

    def test_that_adding_one_rating_sets_average_to_that_rating(self):
    
        movie = Movie("Inception")
        movie.add_rating(5)

        self.assertEqual(1, movie.get_number_of_ratings())
        self.assertEqual(5.0, movie.get_average_rating())

    def test_that_average_is_calculated_correctly_across_multiple_ratings(self):
    
        movie = Movie("Inception")
        movie.add_rating(5)
        movie.add_rating(4)
        movie.add_rating(3)
        movie.add_rating(4)

        
        self.assertEqual(4.0, movie.get_average_rating())
        self.assertEqual(4, movie.get_number_of_ratings())

    def test_that_average_is_not_truncated_to_an_integer(self):
    
        movie = Movie("Interstellar")
        movie.add_rating(5)
        movie.add_rating(4)

       
        self.assertEqual(4.5, movie.get_average_rating())

    def test_that_has_name_matches_exactly_the_same_name(self):
    
        movie = Movie("Inception")

        self.assertTrue(movie.has_name("Inception"))

    def test_that_has_name_is_case_insensitive(self):
        movie = Movie("Inception")

        self.assertTrue(movie.has_name("inception"))
        self.assertTrue(movie.has_name("INCEPTION"))

    def test_that_has_name_returns_false_for_a_different_name(self):
    
        movie = Movie("Inception")

        self.assertFalse(movie.has_name("Interstellar"))

    def test_that_name_attribute_holds_the_original_name(self):
    
        movie = Movie("Koto Aye")

        self.assertEqual("Koto Aye", movie.name)

    def test_that_formatted_date_added_is_not_none_or_empty(self):
    
        movie = Movie("Inception")

        self.assertIsNotNone(movie.get_formatted_date_added())
        self.assertNotEqual("", movie.get_formatted_date_added())


class TestFindMovie(unittest.TestCase):

    def test_that_find_movie_returns_none_when_list_is_empty(self):
    
        movies = []
        self.assertIsNone(find_movie(movies, "Inception"))

    def test_that_find_movie_finds_an_existing_movie_by_exact_name(self):
    
        movies = [Movie("Inception"), Movie("Interstellar")]

        found = find_movie(movies, "Interstellar")

        self.assertIsNotNone(found)
        self.assertEqual("Interstellar", found.name)

    def test_that_find_movie_is_case_insensitive(self):
    
        movies = [Movie("Inception")]

        found = find_movie(movies, "inception")

        self.assertIsNotNone(found)
        self.assertEqual("Inception", found.name)

    def test_that_find_movie_returns_none_for_a_movie_that_does_not_exist(self):
    
        movies = [Movie("Inception")]

        self.assertIsNone(find_movie(movies, "Ghost Movie"))


class TestAddMovie(unittest.TestCase):

    def test_that_adding_a_new_movie_succeeds(self):
    
        movies = []

        success, message = add_movie(movies, "Inception")

        self.assertTrue(success)
        self.assertEqual(1, len(movies))
        self.assertIn("added", message)

    def test_that_adding_a_duplicate_movie_fails(self):
    
        movies = [Movie("Inception")]

        success, message = add_movie(movies, "Inception")

        self.assertFalse(success)
        self.assertEqual(1, len(movies))  

    def test_that_adding_an_empty_name_fails(self):
    
        movies = []

        success, message = add_movie(movies, "   ")

        self.assertFalse(success)
        self.assertEqual(0, len(movies))

    def test_that_adding_a_name_with_only_punctuation_fails(self):

        movies = []

        success, message = add_movie(movies, ",, ,,,")

        self.assertFalse(success)
        self.assertEqual(0, len(movies))

    def test_that_adding_a_name_with_only_commas_and_spaces_fails(self):

        movies = []

        success, message = add_movie(movies, ", , ,")

        self.assertFalse(success)
        self.assertEqual(0, len(movies))

    def test_that_adding_none_as_a_name_fails(self):

        movies = []

        success, message = add_movie(movies, None)

        self.assertFalse(success)
        self.assertEqual(0, len(movies))

    def test_that_a_purely_numeric_name_is_still_allowed(self):
        
        movies = []

        success, message = add_movie(movies, "1917")

        self.assertTrue(success)
        self.assertEqual(1, len(movies))


class TestRateMovie(unittest.TestCase):

    def test_that_rating_an_existing_movie_succeeds(self):
    
        movies = [Movie("Inception")]

        success, message = rate_movie(movies, "Inception", "5")

        self.assertTrue(success)
        self.assertEqual(5.0, movies[0].get_average_rating())

    def test_that_rating_a_nonexistent_movie_fails(self):
    
        movies = []

        success, message = rate_movie(movies, "Inception", "5")

        self.assertFalse(success)

    def test_that_rating_out_of_range_fails(self):
    
        movies = [Movie("Inception")]

        success, message = rate_movie(movies, "Inception", "9")

        self.assertFalse(success)
        self.assertEqual(0, movies[0].get_number_of_ratings())

    def test_that_non_numeric_rating_fails_without_crashing(self):
    
        movies = [Movie("Inception")]

        success, message = rate_movie(movies, "Inception", "abc")

        self.assertFalse(success)
        self.assertEqual(0, movies[0].get_number_of_ratings())


class TestAverageRatingMessages(unittest.TestCase):

    def test_that_get_all_average_ratings_lines_formats_each_movie(self):
    
        movies = [Movie("Inception"), Movie("Interstellar")]
        movies[0].add_rating(5)
        movies[0].add_rating(4)
        movies[1].add_rating(4)

        lines = get_all_average_ratings_lines(movies)

        self.assertEqual("- Inception: 4.50", lines[0])
        self.assertEqual("- Interstellar: 4.00", lines[1])

    def test_that_movie_with_no_ratings_shows_correct_message(self):
    
        movies = [Movie("Inception")]

        message = get_average_rating_message(movies, "Inception")

        self.assertIn("no ratings yet", message)


if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
