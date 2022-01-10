The script is one possible solution of the following exercise: 

10. * Inventory

As a young traveler, you gather items and craft new items.

Input / Constraints
You will receive a journal with some Collecting items, separated with &#39;, &#39; (comma and space). After that, until
receiving &quot;Craft!&quot; you will be receiving different commands.
Commands (split by &quot; - &quot;):
 &quot;Collect - {item}&quot; – Receiving this command, you should add the given item in your inventory. If the
item already exists, you should skip this line.
 &quot;Drop - {item}&quot; – You should remove the item from your inventory, if it exists.
 &quot;Combine Items - {oldItem}:{newItem}&quot; – You should check if the old item exists, if so, add the
new item after the old one. Otherwise, ignore the command.



&quot;Renew – {item}&quot; – If the given item exists, you should change its position and put it last in your
inventory.
Output
After receiving &quot;Craft!&quot; print the items in your inventory, separated by &quot;, &quot; (comma and space).
Examples
Input 
Iron, Wood, Sword
Collect - Gold
Drop - Wood
Craft!

Output
Iron, Sword, Gold






