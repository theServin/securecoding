def read_file(file_path):
   with open(file_path, 'r') as file:
   return file.read()

def execute_command(command):
   os.system(command)  # Potentially unsafe

def process_user_input(user_input):
   # This concatenation is vulnerable to command injection
   command = "echo " + user_input
   execute_command(command)