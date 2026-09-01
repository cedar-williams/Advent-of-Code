# Advent-of-Code-2025

## Day 1
Part 1 was pleasantly easy, but part 2 was not...  I was plagued with so many off-by-one errors that I ended up just making a function to step through a virtual number by number turning of the dial and counting the 0 hits.

## Day 2
Part 1 was again easy, but part 2 had a PEBCAK.  I didn't understand that when they said "at least twice" they meant at least twice so didn't take in to account single digit numbers in my test case.

## Day 3
I'm learning I should be trying to make these solutions modular on part 1 since part 2 seems to be adjusting my solution to select for n somethings every time.  But it was easier this time. This time I went directly to a scratch pad and worked out the logic first and then implemented it.

## Day 4
Part 1 was harder than I expected.  I switched up X and Y which was giving me invalid inputs. Once resolved it solved easy-peasy.  Part 2 was a simple addition, I just had to emulate a do-while loop and repeat the part 1 solution until it did an iteration that didn't make any changes.

## Day 5
The hardest part was figuring out how to easily eval the id's against the ranges.  I think there's probably a faster way to do this, such as collapsing the ranges down, but for puzzle solving this works fine.
Part 2, I spoke too soon. I first tried solving this by mapping each possible value to a dict so there were no duplicates.  This worked for the test case but for the actual problem it was prohibitively slow.  Instead, I wrote some methods to collapse the valid ID's so there were no overlaps then calculate how many values each encompassed.

## Day 6
I considered converting the each column to a different format, something like ((sign),(value1, value2, ...)) but decided that was overcomplicated and just extracted each sign then walked the other values in the column and performed the operation.