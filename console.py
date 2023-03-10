#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ a simple command line interreter """
    prompt = "(hbnb) "
    
    def do_quit(self, line):
         """ Quit command to exit the program  """
         return True
        
    def emptyline(self):
        """ Not to do nothing with empty line and enter """
        pass

    def do_EOF(self, line):
        """ EOF will also exit the program """
        print()
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
