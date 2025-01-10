import subprocess

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def execute_command(command_args):
    # Use subprocess.run for safer command execution
    subprocess.run(command_args, check=True)

def process_user_input(user_input):
    # Secure handling of user input
    sanitized_input = subprocess.list2cmdline([user_input])
    command = ["echo", sanitized_input]
    execute_command(command)