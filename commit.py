#!/usr/bin/python3

# become a better commiter
# author doneskandari@gmail.com

import os
import sys
import subprocess
import git
from termcolor import colored
from art import text2art

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
        print("\tCurrent Branch\t\t\t\t", colored(branch, 'white'))
        
        if len(changed_files) == 0:
            print("\n\tNo Changes.")
            exit()

        # Print the list of changed files with colors
        print(f"\n\tChanges (Untracked, Not Staged)")
        for i, file in enumerate(changed_files):
            colored_num = colored(i+1, "green")
            colored_filename = colored(file, "green")
            print(f"\t\t\t\t\t\t {colored_num}. {colored_filename}")


        print("\n\t----------------------------------------------------")

        # Prompt the user to select files to add to the staging area
        while True:
            selection = input("\tEnter Number(s) (e.g. 1,2) Or 'all' Or 'exit': ")

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
                    print("\n\t----------------------------------------------------")
                    print("\n\tEntered Stage Area",colored(f"\t\t\t {filename}", "green"))
                break
            else:
                print(colored("\tInvalid Selection. Please Try Again.", "red"))

    except Exception as e:
        print("An Error Occurred:", e)

def git_commit():
    try:
        # Open the Git repository in the current working directory
        repo = git.Repo(".")

        # Get a list of files in the staging area
        staged_files = [item.a_path for item in repo.index.diff('HEAD')]

        # Get the current Git branch
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

        # Print the branch name
        print("\tCurrent Branch\t\t\t\t", colored(branch, 'white'))

        if len(staged_files) == 0:
            print("\n\tNo Changes.")
            exit()
        else:
            print(f"\n\tStaged Changes")
            for i ,file in enumerate(staged_files):
                print(colored(f"\t\t\t\t\t\t {i+1}. {file}", 'green'))

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

            print(f"\n\tValid Tags")
            for key, value in valid_tags.items():
                print(colored(f"\t\t\t\t\t\t {key}. {value['tag']}: {value['explanation']}", "green"))

            print("\n\t----------------------------------------------------")
            # Prompt user for input and validate against valid tags
            while True:
                commit_tag_num = input("\tEnter Commit Tag: ")
                if commit_tag_num in valid_tags:
                    commit_tag = valid_tags[commit_tag_num]["tag"]
                    break
                else:
                    print("\tInvalid Tag. Please Try Again.")
            
            header_message += commit_tag
            header_message += ": "

            # Prompt user for commit message header
            while True:
                commit_message = input("\tEnter Commit Message: ")
                if commit_message:
                    break
                else:
                    print(colored("\tCommit Message Cannot Be Empty. Please Try Again.", 'red'))

            header_message += commit_message

            # Prompt user for commit smessage body
            commit_body = input("\tEnter Commit Body: ")

            # Prompt user for commit metadata
            while True:
                commit_metadata = input("\tEnter Commit Metadata: ")
                if commit_metadata:
                    break
                else:
                    print(colored("\tCommit Metadata Cannot Be Empty. Please Try Again.", 'red'))

            print("\n\tyour commit message looks like:\n")
            if commit_body != "":
                print(colored(f"\t{header_message}\n\n\t{commit_body}\n\n\t{commit_metadata}", 'white'))
            else:
                print(colored(f"\t{header_message}\n\n\t{commit_metadata}", 'white'))

            while True:
                confirm = input("\n\tConfirm? Y/N: ")
                if confirm.lower() == "y":
                    print("\n\t----------------------------------------------------")
                    # Commit changes with tag and message
                    if commit_body != "":
                        subprocess.run(["git", "commit", "-m", f"{header_message}\n\n", "-m", f"{commit_body}\n\n", "-m", f"{commit_metadata}\n\n"])
                        print("Changes Has Been Committed.")
                    else:
                        subprocess.run(["git", "commit", "-m", f"{header_message}\n\n", "-m", f"{commit_metadata}\n\n"])
                        print("Changes Has Been Committed.")
                    break
                elif confirm.lower() == "n":
                    print(colored("\tRun The Commit Action Again.", 'red'))
                    exit()
                else:
                    print(colored("\tInvalid Input. Please Try Again.", 'red'))

    except Exception as e:
            print("An error occurred:", e)

def git_push():
    repo = git.Repo('.')

    # Get the current Git branch
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

    # Print the branch name
    print("\tCurrent Branch\t\t\t\t", colored(branch, 'white'))

    os.system(f"git push")
    # Run the `git log` command with the `-n 1` option to get the latest commit
    output = subprocess.check_output(['git', 'log', '-n', '1'])
    print("\n----------------------------------------------------")
    # Print the output to the console
    print(f"{output.decode()}")

def git_branch():
    repo = git.Repo('.')

    # Get the current Git branch
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

    # Print the branch name
    print("\tCurrent Branch\t\t\t\t", colored(branch, 'white'))

    print("\n\tNote: Use Descriptive, Consistent, Short Name.")
    print("\n\tNote: Use Only Alphanumeric Characters && Dashes (-)")

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
        "10": {"tag": "revert", "explanation": "undo or revert previous changes"},
        "11": {"tag": "service", "explanation": "a new service"}
    }

    print(f"\n\tValid Tags")
    for key, value in valid_tags.items():
        print(colored(f"\t\t\t\t\t\t {key}. {value['tag']}: {value['explanation']}", "green"))

    print("\n\t----------------------------------------------------")
    # Prompt user for input and validate against valid tags
    while True:
        branch_tag_num = input("\tEnter Branch Tag: ")
        if branch_tag_num in valid_tags:
            branch_tag = valid_tags[branch_tag_num]["tag"]
            break
        else:
            print("\tInvalid Tag. Please Try Again.")

    # get the new branch name from user input
    branch_name = input("\tEnter The Name For The New Branch: ")
    branch_name = f"krz/{branch_tag}/{branch_name}" 
    repo.git.checkout('-b', branch_name)

    print(f"\n\tBranch Created\t\t\t\t", colored(f"{branch_name}", 'green'))
    print(f"\n\tCheckout To\t\t\t\t", colored(f"{branch_name}", 'green'))

    
def generate_logo(action):
    logo = text2art(action.upper(), font='rd')

    # Split the string into a list of lines
    logo_lines = logo.splitlines()

    # Add a tab character to the beginning of each line
    logo_lines_with_tabs = [f"\t{logo_line}" for logo_line in logo_lines]

    # Join the modified lines back into a single string
    final_logo = "\n".join(logo_lines_with_tabs)

    print()
    print(f"{final_logo}")
    print()

# Get the action to take from the command line argument
if len(sys.argv) > 1:
    action = sys.argv[1]
else:
    print("\tPlease Specify Action (e.g. 'add', 'commit', 'push').")
    exit()


if action == "add":
    generate_logo(action)
    git_add()
elif action == "commit":
    generate_logo(action)
    git_commit()
elif action == "push":
    generate_logo(action)
    git_push()
elif action == "branch":
    generate_logo(action)
    git_branch()
else:
    print("\tAction Not Supported.")
    exit()