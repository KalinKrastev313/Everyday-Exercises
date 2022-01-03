The script is one possible solution of the following exercise: 

4. Office Chairs
So you've found a meeting room - phew! You arrive there ready to present, and find that someone has taken one or
more of the chairs!! You need to find some quick.... check all the other meeting rooms to see if all of the chairs are in
use.
You will be given a number n representing how many rooms there are. On the next n lines for each room you will
get how many chairs there are and how many of them will be taken. The chairs will be represented by 'X's, then
there will be a space ' ' and a number representing the taken places. Example: 'XXXXX 4' (5 chairs and 1 of
them is left free). Keep track of the free chairs, you will need them later. However if you get to a room where there
are more people than chairs, print the following message: '{needed_chairs_in_room} more chairs
needed in room {number_of_room}'. If there is enough chairs in each room print: 'Game On,
{total_free_chairs} free chairs left'


Example
Input 			Output
4			Game On, 4 free chairs left
XXXX 4
XX 1
XXXXXX 3
XXX 3

3			1 more chairs needed in room 2
XXXXXXX 5		2 more chairs needed in room 3
XXXX 5
XXXXXX 8










