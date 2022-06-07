## Why this exists

On page 1 of Glenford Myers' _The Art Of Software Testing_, it is written:

Before beginning the book, it is strongly recommended that you take the following short test. The problem is the testing of the following program:

> The program reads three integer values from a card. The three values are interpreted as representing the lengths of the sides of a triangle. The program prints a message that states whether the triangle is scalene, isosceles, or equilateral.

On a sheet of paper, write a set of test cases (i.e., specific sets of data) that you feel would adequately test this program. When you have completed this, turn the page to analyze your tests.

## Run the tests

```
make test
```

## Scoring

On page 2, it is written, "Give yourself one point for each 'yes' answer" for 14 questions.

By my score, I got: 1,2,3,4,5,6,7,8,12,13,14 and half-point for 11 (see below) — 11.5 out of 14 points.

The ones I missed are:

9. A test case with three integers greater than zero such that the sum of two of the numbers is less than the third (e.g., 1,2,4 or 12,15,30)
10. At least three test cases in category 9 such that you have tried all three permutations
11. A test case in which all sides are 0 — I think I should get half a point here because I have 3 separate tests about a 0 not being allowed at _any_ of the three positions.
