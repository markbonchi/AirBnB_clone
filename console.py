#!/usr/bin/python3
"""Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """To exit the program"""
        return True

    def do_EOF(self, line):
        """exit prgram with ctrl + D"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
