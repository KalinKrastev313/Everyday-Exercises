The script is one possible solution of the following exercise: 

2. Weapon
Create a class Weapon. The __init__ method should receive an amount of bullets (integer). Create an attribute
called bullets, to store them. The class should also have the following methods:
 shoot() - if there are bullets in the weapon, reduce them by 1 and return a message "shooting…". If
there are no bullets left, return: "no bullets left"
You should also override the toString method, so that the following code: print(weapon) should work. To do that
define a __repr__ method that returns "Remaining bullets: {amount_of_bullets}". You can read more
about the __repr__ method here: link
Example

Test Code Output

weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)





