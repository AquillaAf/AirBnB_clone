#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    prompt = '(bhnb) '

    def do_quit(self, line):
        """This interpreter terminates the prompt returns true"""
        return True

    def do_EOF(self, line):
        """this interpreter exits the prompt returns true"""
        return True
    
    def emptyline(self):
        pass
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it 
            (to the JSON file) and prints the id"""
        if not line:
            print('class name missing')
        elif line != 'BaseModel':
            print('class doesnt exist')
        else:
            self.var = BaseModel()
            var.save()
            print(var.id)
    
    def do_show(self, line):
        """Prints the string representation of an instance
            based on the class name and id"""
        arg = line.split()
        if not line:
            print('class name missing')
        elif  len(arg) < 2 and arg[0] != 'BaseModel':
            print('class doesn\'t exist')
        elif len(arg) < 2 and arg[0] == 'BaseModel':
            print('instance id missing')
        elif arg[1] != BaseModel().id:
            print('no instance found')
        elif arg[1] == BaseModel().id:
            print(BaseModel().__str__)

    def do_destroy(self, line):
        arg = line.split()
        if not line:
            print('class name missing')
        elif  len(arg) < 2 and arg[0] != 'BaseModel':
            print('class doesn\'t exist')
        elif len(arg) < 2 and arg[0] == 'BaseModel':
            print('instance id missing')
        elif arg[1] != BaseModel().id:
            print('no instance found')
        elif arg[1] == BaseModel().id:
            print(BaseModel().__del__)

    def do_all(self, line):
            print(self.var.to_dict)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
