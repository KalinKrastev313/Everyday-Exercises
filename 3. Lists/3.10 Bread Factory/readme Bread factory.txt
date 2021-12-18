The script is one possible solution of the following exercise: 

You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events. 
Each event is separated with '|' (vertical bar): "event1|event2|event3…"Each event contains event name or item and a number, 
separated by dash("{event/ingredient}-{number}")If the event is "rest": you gain energy, the number in the second part. 
But your energy cannot exceed yourinitial energy (100). Print: "You gained {0} energy.".
After that, print your current energy: "Current energy: {0}.".If the event is "order": You've earned some coins, the number in the second part.
Each time you get anorder, your energy decreases with 30 points.
If you have energy to complete the order, print: "You earned {0} coins.".
If your energy drops below 0, you skip the order and gain 50 energy points. 
Print: "You had torest!".In any other case you are having an ingredient, you have to buy. 
The second part of the event, contains thecoins you have to spent and remove from your coins.
If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print("You bought {ingredient}.")
If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rushis over.





