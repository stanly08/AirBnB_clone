#!/usr/bin/python3
"""Module for HBNB command interpreter."""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"user created - ID {digit} : {name}")
        else:
            print("invalid input Use: create <digit> <name>")
            return True


    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        print("list of users")
        for digit, name in self.users.items():
            print(f'ID:{digit}, Name:{name}')

    def do_update(self, line):
        """updates users name"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print(f"user updated - ID {digit} : {name}")
            else:
                print(f"no user found with ID: {digit} name: {name}")
        else:
                print(f"Invalid command. Please use update <id:digit> <new name>.")

    def do_destroy(self, line):
        """deletes a user"""
        if line in self.users:
            del self.users[line]
            print(f"deleted user {line}")
        else:
            print(f"no user ID like: {line}")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based on the class name. Ex: $ all BaseModel"""
        try:
            cls = eval(arg)
            objs = storage.all(cls)
            print([str(obj) for obj in objs.values()])
        except NameError:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        try:
            cls = eval(arg)
            count = len(storage.all(cls))
            print(count)
        except NameError:
            print("** class doesn't exist **")

    def default(self, arg):
        """Default behavior for console  when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False



    def help_quit(self):
        """help command for quit"""
        print("Quit the console")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handles EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

