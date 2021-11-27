The script is one possible solution of the following exercise: 

8. * Party Profit

© SoftUni – https://softuni.org. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
Follow us: Page 1 of 1
As a young adventurer, you travel with your party around the world, seeking for gold and glory. But you need to split
the profit among your companions.
You will receive a party size. After that you receive the days of the adventure.
Every day, you are earning 50 coins, but you also spent 2 coins per companion for food.
Every 3 rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.
Every 5 th (fifth) day you slay a boss monster and you gain 20 coins per companion. But if you have a motivational
party the same day, you spent additional 2 coins per companion.
Every 10 th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15 th (fifteenth) day 5
(five) new companions are joined at the beginning of the day.
You have to calculate how much coins gets each companion at the end of the adventure.
Input / Constraints
The input will consist of exactly 2 lines:
 party size – integer in range [1…100]
 days – integer in range [1…100]
Output
Print the following message: &quot;{companions_count} companions received {coins} coins each.&quot;
You cannot split a coin, so take the integral part (round down the coins to integer number).

Examples
Input 	Output
3	3 companions received 90 coins each.
5

Input 	Output
15	19 companions received 102 coins each.
30






