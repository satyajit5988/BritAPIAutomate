# Code Repository -

__https://github.com/satyajit5988/BritAPIAutomate__

# Python Packages Required To Run The Tests -

The project root location contains the __requirement.txt__ file which lists all the packages required to run the test after cloning the repository in the local system. Base python version is __3.13.XX__.

Few of the major libraries that are used in this project are:

1) ```pip install requests```

2) ```pip install json```

3) ```pip install jsonpath```

4) ```pip install pytest```

5) ```pip install pytest-xdist```

6) ```pip install pytest-html```

7) ```pip install pytest-json-report```

8) ```pip install pytest-cov```

9) ```pip install openpyxl```

10 ) ```pip install allure-pytest```

# Cloning Code Repository - 

In order to clone the repository on your local system, create a folder to store the code, open __GitBash__ terminal and redirect to the created folder location and run below commands:

```cd <Path of folder>```

```git clone https://github.com/satyajit5988/BritAPIAutomate.git```

# Setting Up GIT For Source Code Management -

__Git__ can be used for pushing or pulling your code. Steps to set up remote GIT repository is as follows:

1) Create a remote repository by login to GitHub. 
   Note the HTTP's URL to connect to it - __git@github.com:XYZ/ABC.git__

2) Now go to the folder where all your automation code is written.
   Create a local repository by initializing git = __git init__

3) Check status of untracked file by running below command - 
   __git status__
4) Add these files to staging area - 
   __git add <filename> or git add .__
5) Commit these changes -
   __git commit -m "Updating project Files"__
6) Then connect the local and remote repository by running the command - 
   __git remote add origin git@github.com:XYZ/ABC.git__
7) Set the branch to which code is to be pushed - 
   __git branch -M main__
8) Finally push your code using below command - 
   __git push -u origin main__

# Setting Up CI Pipeline Using GitHub Actions -

__GitHub Actions__ can be used for pushing or pulling your code. Steps to set up remote GIT repository is as follows:

1) In our project repository, create the folders: 

   Open GitBash and run the below commands:

   ```cd /path/to/your/repo```

   ```mkdir -p .github/workflows```

2) Create a ```.yml``` file and add the below code to it:

   ```yaml
      name: Python CI Pipeline (Github Actions)

      on:
        push:
          branches:
            - main
        pull_request:
          branches:
            - main

      jobs:
        test:
          runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.13'

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt

         - name: Create Reports Folder
           run: |
             mkdir -p Reports

         - name: Run tests
           run: |
             pytest TestCases/test_EndToEnd.py -v --html=Reports/report.html --capture=no --disable-warnings

         - name: Upload HTML report
           uses: actions/upload-artifact@v4
           with:
             name: TestReportHTML
             path: Reports/report.html

3) Commit this file and push to repo:

   ```git add .github/workflows/ci.yml```

   ```git commit -m "Adding CI pipeline yml file"```

   ```git push origin main```   
          
4) Go to Actions tab in GitHub repository and check if the workflow ran, and it is successful or not - https://github.com/satyajit5988/BritAPIAutomate/actions
