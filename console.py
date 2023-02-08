#!/usr/bin/python3
"""
    ======= for console.py documentation ========== \
    implementing the console for the AirBnB_clone project
    actions :
            do_create * for creating a new model
            do_update * for update exist model
            do_destroy * for destroying the specific model \
                    from the models
            do_all * show all models
            do_show * show the spectific model
            do_help * for The usage of this program
"""

import sys
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

console_model = BaseModel()
store_model = FileStorage()
PROMPT = "(hbnb) "


class HBNBCommand(cmd.Cmd):
    """ hbnb command line manager """

    prompt = PROMPT

    def emptyline(self):
        pass

    def do_create(self, argv):
        """ create a new model of object """
        argc = shlex.split(argv)
        if len(argc) == 0:
            print("** class name missing **")
        if len(argc) > 0:
            try:
                arg_instance = eval(argc[0])()
                arg_instance.save()
                print(arg_instance.id)
            except:
                print("** class doesn't exist **")


    def do_show(self, argv):
        """ show the current object """
        argc = shlex.split(argv)
        if len(argc) == 0:
            print("** class name is missing **")
        if len(argc) == 1:
            print("** instance id missing **")

        if len(argc) > 1:
            store_model.reload()
            # print(console_model)
            m_obj = store_model.all()
            try:
                eval(argc[0])
            except NameError:
                print("** class doesn't exist **")
                return
            key = "{}.{}".format(argc[0],argc[1])
            try:
                value = m_obj[key]
                print(value)
            except KeyError:
                print("no instance found")

    def do_destroy(self, argv):
        """ delete the specific model from the model """
        argc = shlex.split(argv)
        argc = shlex.split(argv)
        if len(argc) == 0:
            print("** class name missing **")
        if len(argc) == 1:
            print("** instance id missing **")

        if len(argc) > 1:
            sh_name = argc[0]
            sh_id = argc[1]
            store_model.reload()
            obj_dict = store_model.all()
            try:
                eval(sh_name)
            except NameError:
                print("** class doesn't exist **")
            key = "{}.{}".format(sh_name,sh_id)
            try:
                del obj_dict[key]
            except KeyError:
                print("** no instance found **")
            storage.save()


    def do_all(self, argv):
        """ show all current models """
        argc = shlex.split(argv)
        if len(argc) == 0:
            pass
        if len(argc) > 0:
            try:
                all_c = argc[0]
                print(eval(all_c)())
            except:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ update model """
        print(arg)

    def do_EOF(self, arg):
        """End of file"""
        return True

    def do_quit(self, arg):
        """ quit syntax for exit the program """
        return True

    def help_quit(self):
        """ help documentation for quit """
        print("Quit cmaand to exit the program")
        return False

    def default(self, argv):
        """ all the action of function list """
        actions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        argv = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
