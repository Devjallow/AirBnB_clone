#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ a simple command line interreter """
    prompt = "(hbnb)"
    def do_quit(self, line):
         """ quit the program if we type it """
         print("quit")
    def d0_EOF(self, line):

        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
