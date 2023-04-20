# become a better commiter
# author doneskandari@gmail.com

import os
import sys
import subprocess
import git
from termcolor import colored

def git_add():
    try:

        repo = git.Repo('.')  # Replace '.' with the path to your repository

        # Get untracked files
        untracked_files = repo.untracked_files

        # Get not staged files
        not_staged_files = [diff.a_path for diff in repo.index.diff(None)]

        # Merge untracked and not staged files
        changed_files = []
        changed_files.extend(untracked_files)
        changed_files.extend(not_staged_files)

        # Get the current Git branch
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

        # Print the branch name
        print(f"\tCurrent branch is", colored(branch, 'red'))
        
        if len(changed_files) == 0:
            print(f"\n\tNo file has been changed in the current directory.")
            exit()

        # Print the list of changed files with colors
        print(f"\n\tThe following files has been changed in the current directory:")
        for i, file in enumerate(changed_files):
            colored_num = colored(i+1, "green")
            colored_filename = colored(file, "green")
            print(f"\t{colored_num}. {colored_filename}")

        # Prompt the user to select files to add to the staging area
        while True:
            selection = input("\nEnter the file number(s) to add (e.g. 1,2), or enter 'all' to add all files, or enter 'exit' to exit: ")

            # Handle special commands
            if selection == "exit":
                exit()
            elif selection == "all":
                selected_files = set(range(1, len(changed_files) + 1))
                break

            # Parse the user's selection
            selected_files = set()
            for sel in selection.split(","):
                try:
                    file_number = int(sel)
                    if file_number < 1 or file_number > len(changed_files):
                        raise ValueError
                    selected_files.add(file_number)
                except ValueError:
                    selected_files = set()
                    break
                    

            # Add the selected files to the staging area
            if selected_files:
                for i in selected_files:
                    filename = changed_files[i-1]
                    subprocess.run(["git", "add", f"{filename}"])
                break
            else:
                print(colored("\nInvalid selection. Please try again.", "red"))

    except Exception as e:
        print("An error occurred:", e)

def git_commit():
    try:
        
        # Prompt user for commit tag
        commit_tag = input("Enter commit tag: ")

        # Prompt user for commit message header
        commit_message = input("Enter commit message: ")

        # Prompt user for commit message body
        commit_body = input("Enter commit body: ")

        # Prompt user for commit metadata
        commit_metadata = input("Enter commit metadata: ")

        # Create commit message string in proper format
        commit_message_str = f"fix: {commit_message}"

        # Commit changes with tag and message
        subprocess.run(["git", "commit", "-m", f"{commit_message_str}", "-m", f"{commit_body}", "-m", f"{commit_metadata}"])

    except Exception as e:
        print("An error occurred:", e)

# Get the action to take from the command line argument
if len(sys.argv) > 1:
    action = sys.argv[1]
else:
    print("Please specify an action (e.g. 'add', 'commit', 'push').")
    exit()

if action == "add":
    git_add()
elif action == "commit":
    git_commit()
elif action == "push":
    os.system(f"git {action}")
    # Run the `git log` command with the `-n 1` option to get the latest commit
    output = subprocess.check_output(['git', 'log', '-n', '1'])
    # Print the output to the console
    print(output.decode())
