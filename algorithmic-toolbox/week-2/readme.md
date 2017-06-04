# why we study algorithms ?

**simple programming problems**
- linear scan
- can not do much better
- solution is obvious

**Standard programming problems**
1. Find the best pairing of students and dorm rooms
2. Find the shortest path to reach the destination

If we solve these problems ourselves, there is always a room for optimisation. These problems are generally math problems indirectly.
It will be a non-trivial result.

**Artificial Intelligence problems**
1. Natural language processing
2. Identify the objects in photograph
3. Play games

Its hard to clear state the problem.

### Two algorithm problems: 
We will cover the two basic algorithm problems:
- Fibonaci numbers
- Greatest common divisors

**Fibonaci Numbers**

<code>Fn = Fn-1 + Fn-2 , n > 1</code>
It was used to estimate rabbit population. How to calculate nth fibonaci number?

**Running time - why is it so slow ?**

Using the naive algorithm, will take a long time to evaulate. As we have a big recursive tree to find the number.

**Greatest Common Divisor**

GCD of 2 numbers, a and b, is defined as the largest number that divides both a and b.

### Big O Notation
Number of lines is not the correct method to measure the complexity of the code.
In order to compute runtime, we need - speed of computer, the system architecture, compiler being used, memory hierarchy, etc.
Figuring out accurate runtime is a huge mess.

Measure runtime in a way that ignores constant multiples.

**Asymptotic runtime**

How does the runtime scale with input size? Approximate run time: 
```logn < n^.5 < n < nlogn < n^2 < 2^n```

Big O notation is used to report algorithm runtime. 

```f(n) = O(g(n))``` if ```f(n) < c.g(n)``` for n >= N 

**Common rules**

- n^a > n^b , a > b
- n^a < b^n , a > 0,  b > 1
- (logn)^a < n^b 
- smaller terms can be ignored

