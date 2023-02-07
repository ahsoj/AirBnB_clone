#!/usr/bin/python3
""""
    cli handling class for executing \
        EOF,quit,help ...\
    like automate task
"""
import sys
import cmd


class HBNBCommand(cmd.Cmd):
    """ CLI handling script """

    # intro = "introduction before start ``prompt`` "
    prompt = "(hbnb) "
    lastcmd = "Bye"

    def emptyline(self):
        """ call when emptyLine + Enter execute """
        pass

    def do_EOF(self, arg):
        """ End_Of_File script """
        return True

    def do_quit(self, arg):
        """ Quit script """
        return True

    def help_quit(self):
        """ help text for quit """
        print("Quit command to exit the program\n")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
