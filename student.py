class Student:
  def __init__(self, first_name, last_name, slack_handle):
    self.first_name = first_name
    self.last_name = last_name
    self.slack_handle = slack_handle
    self.cohort = []
    self.exercise = []

  def add_cohort(self, cohort):
    self.cohort.append(cohort)
  
  def add_exercise(self, exercise):
    self.exercise.append(exercise)

  def __str__(self):
    return f"{self.first_name} is in {self.cohort}"
