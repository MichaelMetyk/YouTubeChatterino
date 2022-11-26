import main
import config
import quickstart
import google_apis
import importlib
import sys

commands = ["/streamer", "/login", "/quit"]

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

    if commands[2] == input_command:
         print("...exiting program")
         sys.exit(0)

run()
