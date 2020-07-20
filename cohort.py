class Cohort:
  def __init__(self, name):
    self.name = name
    self.students = []
    self.instructors = []

  def add_students(self, student):
    self.students.append(student)

  def add_instructors(self, instructor):
    self.instructors.append(instructor)
