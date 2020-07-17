from student import Student
from instructor import Instructor
from exercise import Exercise
from cohort import Cohort


kandy_korner = Exercise("Kandy Korner", "Python")
stocks_report = Exercise("Mushroom Picker", "Python")
planet_list = Exercise("Planet List", "React")
mushroom_picker = Exercise("Mushroom Picker", "Javascript")
star_wars = Exercise("Star Wars", "C+")

c40 = Cohort("C40")
e11 = Cohort("E11")
c42 = Cohort("E42")

stephen = Student("Stephen", "Castaneda","stephencastaneda")
davis = Student("Davis", "Lindell","davislindell")
sarah = Student("Sarah", "Holder","sarahholder")
david = Student("David", "Everett","davideverett")
zane = Student("Zane", "Bliss","zanebliss")

c40.add_students(stephen)
e11.add_students(sarah)
c40.add_students(davis)
c42.add_students(david)
c40.add_students(zane)

zoe = Instructor("Zoe", "Ames", "zames", "knowing every pie flavor ever created")
joe = Instructor("Joe", "Shephered", "joes", "writing witty stories for our exercises")
bryan = Instructor("Bryan", "Nilsen", "bnelsen", "encouraging speeches")
greg = Instructor("Greg", "Korte", "gkorte", "knowing every star wars character")

e11.add_instructors(zoe)
c40.add_instructors(joe)
c40.add_instructors(bryan)
c42.add_instructors(bryan)
e11.add_instructors(greg)

stephen.add_exercise(kandy_korner)
stephen.add_exercise(mushroom_picker)
davis.add_exercise(kandy_korner)
davis.add_exercise(planet_list)
sarah.add_exercise(planet_list)
sarah.add_exercise(star_wars)
david.add_exercise(star_wars)
david.add_exercise(stocks_report)
zane.add_exercise(mushroom_picker)
zane.add_exercise(stocks_report)

students = list()
exercises = list()
students.append(stephen)
students.append(davis)
students.append(sarah)
students.append(david)
students.append(zane)

exercises.append(kandy_korner)
exercises.append(stocks_report)
exercises.append(planet_list)
exercises.append(mushroom_picker)
exercises.append(star_wars)






