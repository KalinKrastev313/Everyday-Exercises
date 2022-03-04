The script is one possible solution of the following exercise: 

Treasure Finder
Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its coordinates. On the first line you will receive a key (sequence of numbers). On the next few lines until you receive "find" you will get lines of strings. You have to loop through every string and decrease the ascii code of each character with a corresponding number of the key sequence. The way you choose a key number from the sequence is just looping through it. If the length of the key sequence is less than the string sequence, you start looping from the beginning of the key. For more clarification see the example below. After decrypting the message you will get a type of treasure and its coordinates. The type will be between the symbol '&' and the coordinates will be between the symbols '<' and '>'. For each line print the type and the coordinates in format "Found {type} at {coordinates}".
Example
Input	Output	Comment
1 2 1 3
ikegfp'jpne)bv=41P83X@
ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
find	Found gold at 10N70W
Found Silver at 32S43W	We start looping through the first string and the key. When we reach the end of the key we start looping from the beginning of the key, but we continue looping through the string. (until the string is over)

The first message is: "hidden&gold&at<10N70W>" so we print we found gold at the given coordinates

We do the same for the second string 
"thereIs&Silver&atCoordinates<32S43W>"(starting from the beginning of the key and the beginning of the string)






