The script is one possible solution of the following exercise: 

Furniture
Write a program to calculate the total cost of different types of furniture. You will be given some lines of input until you receive the line "Purchase". For the line to be valid it should be in the following format:
">>{furniture name}<<{price}!{quantity}"
The price can be floating point number or whole number. Store the names of the furniture and the total price. At the end print the each bought furniture on separate line in the format:
"Bought furniture:
{1st name}
{2nd name}
…"
And on the last line print the following: "Total money spend: {spend money}" formatted to the second decimal point.
Examples
Input	Output	Comment
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase
	Bought furniture:
Sofa
TV
Total money spend: 2436.69	Only the Sofa and the TV are valid, for each of them we multiply the price by the quantity and print the result

