class Instructor:
  def __init__(self, first_name, last_name, slack_handle, specialty):
    self.first_name = first_name
    self.last_name = last_name
    self.slack_handle = slack_handle
    self.cohort = []
    self.specialty = specialty

  def add_student_exercise(self, student):
    self.student.exercises.append(student)


    