Task Manager System:

    A simple Python backend-style project to manage and validate tasks using a modular folder structure.

Project Structure:
    This project is organized into separate folders to keep the logic clean:

    src/api/task.py: Contains the data (list of tasks).
    src/utils/validator.py: Contains the logic to check if data is correct.
    src/main.py: The main file that runs the entire program.

How To Run:
    Open your terminal in the python-practice folder.
    Run the following command:
        python src/main.py  
        
Features:
    Data Retrieval: Fetches a list of tasks with id, title, and status.
    Validation: Uses if and for loops to ensure every task has the required information.
    Modular Design: Demonstrates how to import functions from different folders.

Tech Used:
    Language: Python 3
    Version Control: Git & GitHub

GitHub Workflow: 

  create New Repository Name: python-practice in GitHub.com 
    git init — Starts tracking your files.
    git remote add origin <url> — Connects your computer to GitHub.
    Create a New Branch:
    git checkout -b feature/task-manager-system — Creates a "workspace" for your new code.
    Save Your Work (Commit):
    git add . — Picks up all your files (api, utils, main).
    git commit -m "added task manager logic" — Saves the files with a note.
    Push to GitHub:
    git push -u origin feature/task-manager-system — Sends your branch to the cloud.
    Finish with a Pull Request:
    Go to your GitHub page.
    Click the "Compare & pull request" button.
    Click "Create pull request" to send it for review.

