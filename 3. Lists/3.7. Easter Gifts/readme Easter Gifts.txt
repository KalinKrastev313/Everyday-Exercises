The script is one possible solution of the following exercise: 

7. * Easter Gifts
As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts
you plan on buying on a single line, separated by space, in the following format:
"{gift 1 } {gift 2 } {gift 3 }… {gift n }"
Then you will start receiving commands until you read the &quot;No Money&quot; message. There are three possible
commands:
 "OutOfStock {gift}"
o Find the gifts with this name in your collection, if there are any, and change their values to
"None".

 "Required {gift} {index}"
o Replace the value of the current gift on the given index with this gift, if the index is valid.
 "JustInCase {gift}"
o Replace the value of your last gift with this one.

In the end, print the gifts on a single line, except the ones with value &quot;None&quot;, separated by a single space in the
following format:
"{gift 1 } {gift 2 } {gift 3 }… {gift n }"
Input / Constraints
 On the 1 st line you are going to receive the names of the gifts, separated by a single space.
 On the next lines, until the "No Money" command is received, you will be receiving commands.
 The input will always be valid.
Output
 Print the gifts in the format described above.
Examples
Input 					Output
Eggs StuffedAnimal Cozonac Sweets	StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg
EasterBunny Eggs Clothes
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money

