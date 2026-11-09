"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
import math
"""compares words to string to see if any letters in word match and every time a letter matches add 1
vowels is a string or the "list"
it will return sum of vowels in list
"""
# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    vowels = "aeiouAEIOU"
    s = sum(1 for l in text if l in vowels)
    return s
    raise NotImplementedError("Part 1: implement vowel_count")

"""checks if list is exactly 2 elements long and adds wthem to new list
r is new list
items is list containing smaller lists
function only returns lists with 2 elements"""
# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    r = []
    for l in items:
        if len(l) == 2:
            r.append(l)
    return r
    raise NotImplementedError("Part 2: implement short_lists")

"""
puts lists with 2 elemts in ascedning oreder
l is the lists inside if items
sorted sorts in ascending oreder
function puts lists witrh 2 elements in ascedning oredr and leaves everything else alone
"""
# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    r = []
    for l in items:
        if len(l) == 2:
            r.append(sorted(l))
        else:
            r.append(l)
    return r
    raise NotImplementedError("Part 3: implement ascending_pairs")

"""
function finds dollars and cents
totalC finds total cents between 2 values
dlrs finds dollars and cpmputes cents that go over 100 and divides it to add to dollars, cents are rounded here
c takes total cents and divides by 100
returns dollars as a int and cents as an int
"""
# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    totalC = first.cents + second.cents
    dlrs = first.dollars + second.dollars + totalC // 100
    c = totalC % 100
    return data.Price(dlrs, c)
    raise NotImplementedError("Part 4: implement add_prices")

"""
finds rect area
w = right-left while h = top - bottom
returns area of rectangle using two points diagonal of each other diagonally
"""
# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    w = rectangle.bottom_right.x - rectangle.top_left.x
    h = rectangle.top_left.y - rectangle.bottom_right.y
    return h * w
    raise NotImplementedError("Part 5: implement rectangle_area")

"""
return books in original order of list of given author
author is authors books is books assigned to author and books is assigned list of differnt authors and books
function returns all books with author is on
"""
# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    r = []
    for book in books:
        if author in book.authors:
            r.append(book)
    return r
    raise NotImplementedError("Part 6: implement books_by_author")

"""
finds smallest circle that rectange canfit in
left-right divided by 2 for horizontal, same for top bottom
returns radius of smallest circle
"""
# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    center = data.Point(
        (rectangle.top_left.x + rectangle.bottom_right.x) / 2,
        (rectangle.top_left.y + rectangle.bottom_right.y) / 2,
    )
    radius = math.hypot(rectangle.bottom_right.x - center.x, rectangle.bottom_right.y - center.y,)
    return data.Circle(center, radius)
    raise NotImplementedError("Part 7: implement circle_bound")

"""
finds what wage is below average
employees contains data about employee name and wage
average takes all wages and averages them out
returns employees who arenpaid below average of group
"""
# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    if not employees:
        return []
    average = sum(e.pay_rate for e in employees) / len(employees)
    return [e.name for e in employees if e.pay_rate < average]
    raise NotImplementedError("Part 8: implement below_pay_average")
