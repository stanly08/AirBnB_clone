#!/usr/bin/python3


import unittest
from models import storage
from models.engine.file_storage import FileStorage
import os
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand_prompting(unittest.TestCase):
    
    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f_show:
                HBNBCommand().onecmd(f"show User {user_id}")
                self.assertIn(user_id, f_show.getvalue())

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn("[]", f.getvalue().strip())

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"update User {user_id} name 'John Doe'")
            with patch('sys.stdout', new=StringIO()) as f_update:
                HBNBCommand().onecmd(f"show User {user_id}")
                self.assertIn("John Doe", f_update.getvalue())

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f_destroy:
                HBNBCommand().onecmd(f"destroy User {user_id}")
                HBNBCommand().onecmd(f"show User {user_id}")
                self.assertIn("** no instance found **", f_destroy.getvalue())


class TestConsole(unittest.TestCase):

    def test_help_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("Show instances based on class name", output)


if __name__ == '__main__':
    unittest.main()
