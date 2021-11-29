The script is one possible solution of the following exercise: 

9. *Snowballs
Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best
snowballs. They have decided to involve you in their fray, by making you write a program, which calculates snowball
data, and outputs the best snowball value.
You will receive N – an integer, the number of snowballs being made by Tony and Andi.
For each snowball you will receive 3 input lines:
 On the first line you will get the snowball_snow – an integer.

On the second line you will get the snowball_time – an integer.
 On the third line you will get the snowball_quality – an integer.
For each snowball you must calculate its snowball_value by the following formula:
(snowball_snow / snowball_time) ^ snowball_quality

At the end you must print the highest calculated snowball_value.
Input
 On the first input line you will receive N – the number of snowballs.
 On the next N * 3 input lines you will be receiving data about snowballs.
Output
 As output you must print the highest calculated snowball_value, by the formula, specified above.
 The output format is:
{snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})
Constraints
 The number of snowballs (N) will be an integer in range [0, 100].
 The snowball_snow is an integer in range [0, 1000].
 The snowball_time is an integer in range [1, 500].
 The snowball_quality is an integer in range [0, 100].

Input 	Output
2	10 : 2 = 125 (3)
10
2
3
5
5
5



