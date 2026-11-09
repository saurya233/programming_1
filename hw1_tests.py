"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest
import math

import data
import hw1


class TestHomework1(unittest.TestCase):

# Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("Apple"), 2)
        self.assertEqual(hw1.vowel_count("AEIOUaeiou"), 10)
        self.assertEqual(hw1.vowel_count("rhythm"), 0)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        lists = [[1], [2, 3], [], [4, 5, 6], [7, 8]]
        self.assertEqual(hw1.short_lists(lists), [[2, 3], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [], [1, 2, 3]]), [])
        self.assertEqual(hw1.short_lists([]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(
            hw1.ascending_pairs([[9, 2], [1, 2], [5, 5]]),
            [[2, 9], [1, 2], [5, 5]],
        )

    def test_ascending_pairs_other_lengths_unchanged(self):
        lists = [[], [3], [3, 1, 2], [4, 3, 2, 1]]
        self.assertEqual(hw1.ascending_pairs(lists), lists)
        self.assertEqual(
            hw1.ascending_pairs([[9, 2], [3, 1, 2], [5, 5]]),
            [[2, 9], [3, 1, 2], [5, 5]],
        )

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        result = hw1.add_prices(data.Price(1, 20), data.Price(2, 30))
        self.assertEqual(result, data.Price(3, 50))

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(
            hw1.add_prices(data.Price(3, 75), data.Price(2, 50)),
            data.Price(6, 25),
        )
        self.assertEqual(
            hw1.add_prices(data.Price(1, 50), data.Price(2, 50)),
            data.Price(4, 0),
        )

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rect = data.Rectangle(data.Point(0, 3), data.Point(4, 0))
        self.assertEqual(hw1.rectangle_area(rect), 12)

    def test_rectangle_area_negative_coordinates(self):
        rect = data.Rectangle(data.Point(-5, -1), data.Point(-2, -4))
        self.assertEqual(hw1.rectangle_area(rect), 9)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        a = data.Book(["Ann Lee"], "Alpha")
        b = data.Book(["Bo Kim"], "Beta")
        c = data.Book(["Ann Lee", "Bo Kim"], "Gamma")
        d = data.Book(["Ann Lee"], "Delta")
        books = [a, b, c, d]
        self.assertEqual(hw1.books_by_author("Ann Lee", books), [a, c, d])
        self.assertEqual(hw1.books_by_author("Bo Kim", books), [b, c])

    def test_books_by_author_no_matches(self):
        books = [data.Book(["Ann Lee"], "Alpha")]
        self.assertEqual(hw1.books_by_author("Cy Doe", books), [])
        self.assertEqual(hw1.books_by_author("Ann Lee", []), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rect = data.Rectangle(data.Point(-1, 1), data.Point(1, -1))
        self.assertEqual(
            hw1.circle_bound(rect),
            data.Circle(data.Point(0, 0), math.sqrt(2)),
        )

    def test_circle_bound_non_square_rectangle(self):
        rect = data.Rectangle(data.Point(0, 8), data.Point(6, 0))
        self.assertEqual(
            hw1.circle_bound(rect),
            data.Circle(data.Point(3, 4), 5),
        )

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        staff = [
            data.Employee("Ann", 10),
            data.Employee("Bo", 40),
            data.Employee("Cy", 20),
            data.Employee("Di", 30),
        ]
        self.assertEqual(hw1.below_pay_average(staff), ["Ann", "Cy"])
        staff = [
            data.Employee("Ann", 10),
            data.Employee("Bo", 20),
            data.Employee("Cy", 30),
        ]
        self.assertEqual(hw1.below_pay_average(staff), ["Ann"])

    def test_below_pay_average_empty_list(self):
        self.assertEqual(hw1.below_pay_average([]), [])
        staff = [data.Employee("Ann", 15), data.Employee("Bo", 15)]
        self.assertEqual(hw1.below_pay_average(staff), [])


if __name__ == '__main__':
    unittest.main()
