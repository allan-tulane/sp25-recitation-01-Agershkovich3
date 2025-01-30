[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tqM-lrvp)
# CMPS 2200 Recitation 01

**Name (Team Member 1):**Aaron Gershkovich 
**Name (Team Member 2):** Josh Sasson

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**
The worst case for linear search is that it is not present in the list because the function then needs to loop through every value in the list until the end, or if it is the last value of the list, leading to an O(n) complexity. The worst case for binary_search is a value that is acheived by dividing by 2 the most amount of times or if the value is not present in the list, leading to an O(n) complexity.
- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**
The best case for linear search is that the key is the first value because the function would only need to read the first value. The best case input value of key for binary_search is the middle value because that is the first value the function looks at when dividing the whole list by 2.
- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO: add your timing results here**
|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.002 |    0.003 |
|      100 |    0.003 |    0.001 |
|     1000 |    0.036 |    0.002 |
|    10000 |    0.395 |    0.003 |
|   100000 |    4.252 |    0.005 |
|  1000000 |   43.058 |    0.010 |
| 10000000 |  456.888 |    0.020 |
- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**TODO: your answer goes here**
Yes, my results support this conclusion because although initially the binary function may take longer than the linear function for smaller n, eventually the binary function is a lot faster than the linear search and the time only increases slightly even if the number of values is multiplied by 10.


- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **TODO: your answer goes here**
    The worst case time complexity is just k* O(n) or just O(kn).
  + For binary search? **TODO: your answer goes here**
    For binary search the complexity is a lot worse because it would be $O(n^2)$ to sort the array, then k *log(n) to actually complete the binary search. So, the total complexity is $O(n^2 + k*log(n)$, or just O(n^2).
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: your answer goes here**
    For Large n, n^2 dominates kn, but we are looking for n^2 < kn, so dividing by n, n < k. Thus, sorting then using binary search is more efficient when n < k, and using linear search is more efficient when n >= k because the sorting overhead becomes so large.
