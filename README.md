# AirBnB_clone
This repository is a clone of the AirBnB website 

:: The Aim of the project is a create a  website that provides residence to people in a need of one.

website Features
================

* STORAGE: user data, client data and it's interactions will be needed to be developed 
* COMMNAND INTERPRETER: It is a prompt in CLI, always in a loop, waiting for a command
 to be parsed to the STDIN. After a command is received, it parses ton the interpreter and executed.
 the interpreter consist of a (cmd)class in python standard library.
HOW TO START
============
A python file which contains a inherited (cmd) class is executed and the prompt shows up

HOW TO USE
==========
Methods in this class are the interpreters of a command use in the CI
example:
cmd/_int.py
<<<
Class my_cmd/_interpreter(cmd.CMD):
	prompt = ':) '
	def do_greet(self, line):
		if line:
			print ('hi', line)
		else:
			print 'hi'
	def do_EOF(self, line)
		print ('goodbye')
		return TRUE
if __name__ == "__main__":
	my_cmd_interpreter.cdmloop()
>>>
executing cmd_int.py will show a prompt :) continiously blinking.

<do> is an inherited syntax in the cmd.CMD class
<greet> is the command
<EOF> is a command handler that returns a true value. any interpreter that returns true will terminate the prompt
<cmdloop>  is an inherited method used to keep the prompt runnning
<help> is a method inherited from the cdm.CDM class, it shows you how to use the commands
example:
./cmd_int.py 
:) help 
will output:
<<<
Documented commands (type help <topic>):
========================================
help

Undocumented commands:
======================
EOF  greet 
>>>
this help, shows us the command we can use in this prompt, the help is documented from the inherited cdm.CMD class, while
the customised one (EOF, greet) isnt documented why?, becasue we didnt put it in comment on how to use it.
NOTE: It automatically uses the comment as its how-to-use help and it must be immediately after the method definition..


