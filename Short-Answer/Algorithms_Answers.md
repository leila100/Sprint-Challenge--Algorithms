#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n) because the loop will run only n times (when n is in this case n^3)

b)
O(nlog(n)) because the while loop runs only half of the n for every for loop

c)
O(n) because it will run for as long as bunnies is > 0 (n in this case is bunnies)

## Exercise II

'''
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.
'''
A solution could be:

- check if the egg breaks at n/2-story building.
  - if it does, it mean that it is too high, so need to check the lower half of the building.
  - if it doesn't break, that mean it's too low, need to check the upper half of the building
- keep checking until the building is only one story high, that would be the f floor

def get_f(n, start = 0, end = n):

<!-- If building is only one story, that is f -->

if n == 1:
return start
middle = (end-start) // 2
if egg breaks at middle:
<!-- if egg breaks at middle, try a floor n/2 lower -->
return get_f((end-start), start, middle)
else:
<!-- if egg doesn't break, try a floor n/2 above -->
return get_f((end-start), middle, end)
