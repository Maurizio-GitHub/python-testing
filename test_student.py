import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    """
    The following code, built via an approach step-by-step, is "DRY".
    To avoid repeating ourselves, we leveraged the 'setUp' method.
    """

    # def test_full_name(self):
    #     student = Student("John", "Doe")
    #     self.assertEqual(student.full_name, "John Doe")

    # def test_email(self):
    #     student = Student("John",  "Doe")
    #     self.assertEqual(student.email, "john.doe@email.com")

    # def test_alert_santa(self):
    #     student = Student("John",  "Doe")
    #     student.alert_santa()
    #     self.assertTrue(student.naughty_list)

    # The 'setUpClass' method can be used to create temporary files and
    # folders or set up a database connection during tests. Adding the
    # @classmethod decorator to a method and passing 'cls' as a method
    # parameter makes it a class method, which acts on the class instead
    # of an instance of the class:
    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    # The 'tearDown' method is used to remove temporary files or folders
    # or close a connection to a database. Adding the
    # @classmethod decorator to a method and passing 'cls' as a method
    # parameter makes it a class method, which acts on the class instead
    # of an instance of the class:
    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    def tearDown(self):
        print("tear down")

    # The 'setUp' method is run before each test;
    # the tearDown method is run after:
    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        """
        The 'patch' method imported can be  used as a decorator or a context
        manager. We will use a context manager for our test method. We want
        to mock a get request in the student module, so we can set our context
        manager as an object called 'mocked_get', which can be used to test
        our get request functionality:
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        """
        In the path, 'student' comes from the name of the file 'student.py'.
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")


if __name__ == "__main__":
    unittest.main()
