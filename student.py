from NSSperson import NSSPerson

class Student(NSSPerson):
  def __init__(self):
    self.cohort = []
    self.exercise = []

  def add_cohort(self, cohort):
    self.cohort.append(cohort)
  
  def add_exercise(self, exercise):
    self.exercise.append(exercise)

  def __str__(self):
    return f"{self.first_name} is in {self.cohort}"
