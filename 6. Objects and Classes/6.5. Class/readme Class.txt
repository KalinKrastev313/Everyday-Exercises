The script is one possible solution of the following exercise: 

5. Class
Create a class Class. The __init__ method should receive the name of the class. It should also have 2 lists
(students and grades). Create a class attribute __students_count equal to 22. The class should also have 3
additional methods:

© SoftUni – https://softuni.org. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
Follow us: Page 5 of 5
 add_student(name, grade) - if there is space in the class, add the student and the grade in the two
lists
 get_average_grade() - returns the average of all existing grades formatted to the second decimal point
(as a number)
 __repr__ - returns the string (single line): "The students in {class_name}: {students}.
Average grade: {get_average_grade()}". The students must be seperated by ", "
Example

Test Code Output

a_class = Class(&quot;11B&quot;)
a_class.add_student("Peter";, 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

The students in 11B: Peter, George, Amy.
Average grade: 4.77



