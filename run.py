import main
import quickstart
import google_apis
import importlib
import sys
import PIL
import os

commands = ["/streamer", "/login", "/clear", "/graphics", "/help", "/quit"]

def run():
  while True:
    input_command = input(str)
    
  
    
    if commands[0] == input_command[:9]:
     main_obj = main.main(input_command[9:])
     main_obj.login_bool()

    if commands[1] == input_command:
      print("...screen should appear")
      importlib.reload(google_apis)
      importlib.reload(quickstart)

    if commands[3] == input_command:
      main_obj1 = main.main(None)
      main_obj1.user_set_emotes()
      
    
    if commands[2] == input_command: os.system("clear")
    
    if commands[4] == input_command : print(*commands, sep = " ") 
    
    if commands[5] == input_command : quit()
  
    
   
        


run()
