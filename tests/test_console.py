import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestHBNBCommandCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_string(self):
        output = StringIO()
        sys.stdout = output
        self.console.onecmd('create State name="California"')
        state_id = output.getvalue().strip()
        self.assertTrue(len(state_id) > 0)

    def test_create_with_int_and_float(self):
        output = StringIO()
        sys.stdout = output
        self.console.onecmd('create Place number_rooms=4 latitude=37.773972')
        place_id = output.getvalue().strip()
        self.assertTrue(len(place_id) > 0)

    def test_create_invalid_class(self):
        output = StringIO()
        sys.stdout = output
        self.console.onecmd('create InvalidClass')
        self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
                )

    def tearDown(self):
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
