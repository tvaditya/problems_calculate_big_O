# Problems_calculate_big_O ( Runtime Analysis, worst case Big O notatios )

## task0.py
Runtime is an O(1) as it is independent of the inputs. 
We are only printing out results:
print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2][11:]}")
So this is O(1)

## task1.py
We have to nested for loops which is quadratic complexity.
So we will have O(2n^2)
Statments like prints will be O(1)

Runtime can be approximated O(n^2) as it is the worst case

## task2.py
We have one nested for loop which is O(n^2).
One simple for loop which is O(n).
Another for loop with an if statements which also is O(n)
Statments like prints will be O(1)

Runtime can be approximated O(n^2) as it is the worst case

## task3.py
We have one for nested loop which is O(n^2)
And three for loops which are O(n)
In onefor loop we have sorting is O(n*log(n))
Statments like prints will be O(1)

Runtime can be approximated O(n^2) as it is the worst case

## task4.py
We have four for loops each of them is O(n),  the ones that create our sets
In the fifth for loop we have sorting is O(n*log(n)), the for loop itself is also O(n)
Statments like prints will be O(1)

Runtime can be approximated O(n) as it is the worst case
