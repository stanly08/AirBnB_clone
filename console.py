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

    def help_quit(self):
        """help command for quit"""
        print("Quit command to exit the program")

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
        print("Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        if not arg:
            print("class name missing")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("class doesn't exist")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        args = arg.split()
        if not arg:
            print("class name missing")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("no instance found")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        args = arg.split()
        if not arg:
            print("class name missing")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("no instance found")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based on the class name. Ex: $ all BaseModel"""
        try:
            cls = eval(arg)
            objs = storage.all(cls)
            print([str(obj) for obj in objs.values()])
        except NameError:
            print("class doesn't exist")

    def do_update(self, line):
        """Usage: update <class name> <id> <dictionary representation>
        Updates an instance based on the class name and id with a dictionary representation"""

        args = line.split()
        if len(args) == 0:
            print("class name is missing")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Place",
                             "Review", "Amenity"]:
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("no instance found")
            return
        if len(args) < 3:
            print("dictionary representation missing")
            return
        try:
            updates = json.loads(' '.join(args[2:]))
        except ValueError:
            print("invalid dictionary representation")
            return

        obj = all_objs[key]
        for key, value in updates.items():
            setattr(obj, key, value)
        obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        try:
            cls = eval(arg)
            count = len(storage.all(cls))
            print(count)
        except NameError:
            print("class doesn't exist")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

