#!/usr/bin/python3
"""Module for HBNB command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all"""
        args = arg.split()
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in storage.all().items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@samuelstanly.com" """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            setattr(objects[key], args[2], eval(args[3]))
            storage.save()
        except AttributeError:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

