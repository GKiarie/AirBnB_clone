#!/usr/bin/python3
"""Entry Point to command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the class interperter
    """

    prompt = "(hbnb) "
    class_dict = {"BaseModel": BaseModel}

    def do_create(self, line):
        """
        Create a new instance of BaseModel
        Saves it to a JSON file
        Prints the id
        """
        if not line:
            print("** class name missing **")
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                my_model = HBNBCommand.class_dict[line]()
                my_model.save()
                print(my_model.id)

    def do_show(self, line):
        """
        Prints the string repr of an instance based
        on the class name and id.
        $ show BaseModel xxxx-xxxx-xxxx
        """
        key = line_checker(line)
        if key:
            my_dict = storage.all()
            print(my_dict[key].to_dict())

    def do_destroy(self, line):
        """
        Deletes an instancebased on the class name and id
        """
        key = line_checker(line)
        if key:
            my_dict = strorage.all()
            del my_dict[key]
            storage.save()

    def do_all(self, line):
        """
        Prints all string repr of all instances based or not on
        the class name
        """
        my_dict = storage.all()
        my_list = []
        if len(line) == 0:
            for value in my_dict.values():
                my_list.append(str(value))
            print(my_list)
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                for value in my_dict.values():
                    if value.to_dict()["__class__"] == line:
                        my_list.append(str(value))
                print(my_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        my_list = parse(line)
        key = line_checker(line)
        if key:
            if len(my_list) > 4:
                print("Usage:update <class name> <id> <attribute name>\
 \"<attribute value>\"")
            elif len(my_list) == 3:
                print("** value missing **")
            elif len(my_list) == 2:
                print("** attribute name missing **")
            else:
                my_dict = storage.all()
                my_inst = my_dict[key]
                val = my_list[3][1:-1]
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
                setattr(my_inst, my_list[2], val)
                storage.save()

    def do_quit(self, line):
        """
        Exits the program by inputting 'quit'
        """
        return True

    def do_EOF(self, line):
        """
        Exits the console by typing:
        > EOF
        > Cntrl + D
        """
        return True

    def emptyline(self):
        """
        Define empty line
        """
        pass


def parse(arg):
    """
    Conver s series of zero or more args to a list
    """
    return arg.split()


def line_checker(line):
    """
    Takes line as input and performs checks to give right
    input depending on length of input and the input iteself
    """
    my_list = parse(line)
    if len(my_list) == 0:
        print("** class name missing **")
    elif len(my_list) == 1:
        if my_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")
    elif len(my_list) >= 2:
        if my_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            key = f"{my_list[0]}.{my_list[1]}"
            my_dict = storage.all()
            if key in my_dict:
                return key
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
