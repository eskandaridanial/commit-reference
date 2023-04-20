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
        print("\tCurrent Branch:", colored(branch, 'white'))
        
        if len(changed_files) == 0:
            print("\n\tNo Change.")
            exit()

        # Print the list of changed files with colors
        print(f"\n\tChanges (untracked_files && not_staged_files):")
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
                    print(colored(f"\t{filename} is now in staging area.", "green"))
                break
            else:
                print(colored("\nInvalid selection. Please try again.", "red"))

    except Exception as e:
        print("An error occurred:", e)

def git_commit():
    try:
        # Open the Git repository in the current working directory
        repo = git.Repo(".")

        # Get a list of files in the staging area
        staged_files = [item.a_path for item in repo.index.diff('HEAD')]

        if len(staged_files) == 0:
            print("Nothing added to the staging area.")
            exit()
        else:
            print("The following files has been added to the staging area:")
            for i ,file in enumerate(staged_files):
                print(colored(f"\t{i+1}. {file}", 'green'))

            print("\n-------------------------------------")
            header_message = ""
            # Define valid tags and their explanations
            valid_tags = {
                "1": {"tag": "feature", "explanation": "a new feature"},
                "2": {"tag": "fix", "explanation": "bug fix"},
                "3": {"tag": "refactor", "explanation": "code restructuring"},
                "4": {"tag": "test", "explanation": "test-related changes"},
                "5": {"tag": "doc", "explanation": "documentation updates"},
                "6": {"tag": "style", "explanation": "code formatting"},
                "7": {"tag": "perf", "explanation": "improve performance"},
                "8": {"tag": "config", "explanation": "change the configuration file"},
                "9": {"tag": "security", "explanation": "improve securiy"},
                "10": {"tag": "revert", "explanation": "undo or revert previous changes"}
            }

            for key, value in valid_tags.items():
                print(colored(f"\t{key}. {value['tag']}: {value['explanation']}", "green"))

            # Prompt user for input and validate against valid tags
            while True:
                commit_tag_num = input("Enter commit tag: ")
                if commit_tag_num in valid_tags:
                    commit_tag = valid_tags[commit_tag_num]["tag"]
                    break
                else:
                    print("Invalid tag number. Please try again.")
            
            header_message += commit_tag
            header_message += ": "

            # Prompt user for commit message header
            while True:
                commit_message = input("Enter commit message: ")
                if commit_message:
                    break
                else:
                    print(colored("Commit message cannot be empty. Please try again.", 'red'))

            header_message += commit_message

            # Prompt user for commit smessage body
            commit_body = input("Enter commit body: ")

            # Prompt user for commit metadata
            while True:
                commit_metadata = input("Enter commit metadata: ")
                if commit_metadata:
                    break
                else:
                    print(colored("Commit metadata cannot be empty. Please try again.", 'red'))

            print("\n\tyour commit message looks like:\n")
            print(colored(f"\t{header_message}\n\n\t{commit_body}\n\n\t{commit_metadata}", 'white'))
            confirm = input("\nConfirm? (Y/N): ")
            while True:
                if confirm.lower() == "y":
                    # Commit changes with tag and message
                    subprocess.run(["git", "commit", "-m", f"{header_message}\n\n", "-m", f"{commit_body}\n\n", "-m", f"{commit_metadata}\n\n"])
                    print(colored("\tChanges has been committed.", 'green'))
                    break
                elif confirm.lower() == "n":
                    print(colored("Run the commit action again.", 'red'))
                    exit()

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