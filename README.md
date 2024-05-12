# BusNumbersGame
Code using my FYP code to solve the bus numbers game.

## Rules
A NSW bus has 4 digit ID's, using each number only once with the operations (addition, subtraction, multiplication and division) you have to make 10.

## Modelling

### State
We'll have 5 bits to our state. Each of the four numbers in the ID and a running total. Numbers will start out as False if they're unavailable.

$$
\begin{align*}
n = range = \{False, \mathcal{I}\} \\
x = \{T, n, n, n\} \\
\end{align*}
$$

### Functions
**Addition**
$$
\begin{align*}
add(n_1:n, n_2:n)\\
pre: nill \\
post: \\
n_1 = False, n_2 = False, T = n_1 + n_2
\end{align*}
$$
**Subtraction**
$$
\begin{align*}
add(n_1:n, n_2:n)\\
pre: nill \\
post: \\
n_1 = False, n_2 = False, T = n_1 - n_2
\end{align*}
$$
**Multiplication**
$$
\begin{align*}
add(n_1:n, n_2:n)\\
pre: nill \\
post: \\
n_1 = False, n_2 = False, T = n_1 \times n_2
\end{align*}
$$
**Division**
$$
\begin{align*}
add(n_1:n, n_2:n)\\
pre: n_2 \notin 0 \\
post: \\
n_1 = False, n_2 = False, T = \frac{n_1}{n_2}
\end{align*}
$$

## Program
1. Select possible bus number
1. Convert to state $x_0$
1. Solve
1. Output