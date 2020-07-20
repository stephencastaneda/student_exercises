from NSSperson import NSSPerson

class Instructor(NSSPerson):
  def __init__(self, specialty):
    self.cohort = []
    self.specialty = specialty

  def add_student_exercise(self, student):
    self.student.exercises.append(student)


    