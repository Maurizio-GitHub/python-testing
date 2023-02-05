from datetime import date, timedelta
import requests


# Since we want first name, last name and start date to be read-only fields,
# we can prepend these properties with an underscore, so that other developers
# know how to behave. When an instance of our Student class is created, the
# start_date value is set using the time at the moment of the instance’s
# creation. In our  fictional school, students will enroll for a year, so we
# can define end_date and set it equal to date.today() plus a timedelta of
# 365 days. This does not allow for leap years, though:
class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # Since this is a method to get data only, we add the @property decorator
    # to our full_name method:
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    # Since this is a method to get data only, we add the @property decorator
    # to our full_name method:
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date += timedelta(days=days)

    def course_schedule(self):
        response = requests.get(
            f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong"
