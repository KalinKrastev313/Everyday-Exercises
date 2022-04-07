Solution of the following exercise: 

Create a class called Programmer. Upon initialization it should receive name (string), language (string), skills (integer). The class should have two methods:
watch_course(course_name, language, skills_earned)
If the programmer's language is the equal to the one on the course increase his skills with the given one and return a message "{programmer} watched {course_name}".
Otherwise return "{name} does not know {language}".
change_language(new_language, skills_needed) 
If the programmer has the skills and the language is different from his, change his language to the new one and return "{name} switched from {previous_language} to {new_language}".
If the programmer has the skills, but the language is the same as his return "{name} already knows {language}".
In the last case the programmer does not have the skills, so return "{name} needs {needed_skills} more skills" and don't change his language
Examples
Test Code	
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))	

Output
John does not know Python
John already knows Java
John needs 50 more skills
John watched Java: zero to hero
John switched from Java to Python
John watched Python Masterclass

