# Trip Planner

This repository is a polished version of the app "Trip Planner" developed along the Codecademy's course "Learn Flask". It serves as my final project for assessement of the module "Introduction to Software Engineering" at CODE University of Applied Sciences.

## Every Time You Develop on Your Project

Every time you restart your computer or reopen VSCode, you'll have to do a few things. Instructions for macOS and Linux distributions assume you are using a Bash shell. Instructions for Windows assume you are using the Command Prompt. Instructions for other shells can be found online.

- Activate your virtual environment for this project:

    macOS/Linux: `source venv/bin/activate`

    Windows: `venv\Scripts\activate.bat`

- Point Flask to your application:

    macOS/Linux:  `export FLASK_APP=run.py`

    Windows: `set FLASK_APP=run.py`
- Enable hot reloading, debug mode, and other useful features for local development:

     macOS/Linux: `export FLASK_ENV=development`

    Windows: `set FLASK_ENV=development`
- run your flask application:

    `flask run`


# Installation Instructions
This will be a quick overview of steps for how to use this template on your own project, but will not be a line-for-line cookbook. You can find deeper explanations, tips, and instructions in the [Foundation's main class repository](https://github.com/DrAdamRoe/foundations-sample-website), used for homework assignments.

## Before you start...
You should have:
- Python 3.8.x installed on your computer
- Visual Studio Code (or another IDE of your choosing) installed on your computer
- A GitHub account

### Make This Your Own

Ready to go? Start by making this project your own:
- Fork this repository into your GitHub account. This is a good time to rename the repository to have the name of your project - but you can do it later, too.
- Choose (or create) a working directory on your own computer and change directory into it
- Clone _your_ version onto your computer in that working directory.

Now you should be ready to get the starter template running on your computer!

### Get Set Up for Local Development:
- Open Visual Studio Code, and open the folder containing your locally cloned repository. Before editing the code, make sure everything works as expected, locally at least.
- Open a terminal in VS Code, too. This should automatically be in the same directory as your repository, if not, you should change directory to be in there.
- In the terminal, create a new virtual environment for this project, using Python 3.8.x. The exact command will depend on your operating system and setup, but the idea is the same: call the Python executable at the command line (e.g. `python` or `python3.8` or `python3` or maybe `\Python38\python` on Windows). Normally, that will open the Python REPL interface, but we don't want that this time - we want it to create a virtual environment for us. To do that, pass the argument `-m venv`, which tells Python "run the venv module". Then, give it one more argument which is the path to a folder name where the virtual environment will live. For ease and consistency, this should be called `venv` and live in the repository root folder. This command could look like this, in the end, depending on your setup:

    > python3.8 -m venv venv

- Activate your virtual environment (instructions can be found at the top of this readme)
- Download the Python modules listed in requirements.txt using pip. In case you are running Windows, uwsgi isn't availiable, so uncomment it in the requirements.txt. (uWSGI==2.0.19.1 => #uWSGI==2.0.19.1) before you execute the following command:

    > pip install -r requirements.txt

### Configure Visual Studio Code

A lot can be said here, but there are a few things that will make your life much easier, and are highly recommended:

- Enable the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), which will immediately give you coding suggestions and show warnings.
- Set the linter to `flake8`, the same one we are using at the command line and when we build on Google Cloud (CTRL+SHIFT+P / ⇧⌘P). This will give you visual feedback (yellow and red squiggly lines)
- Set the version of Python (or "interpreter") to be the virtual environment you have just created. (CTRL+SHIFT+P / ⇧⌘P). This will help you to identify mismatches in your setup, especially when importing modules.

### A Few Notes...
Some pieces of this repository may require explaining. Here goes.

#### Environment Variables
This setup is designed to allow you t use environment variables if you need them. There are many ways to set this up with Python, and for this repository, I chose a method which allows for relatively simple integration with our GitHub Actions and Google App Engine workflow, but it does not scale very well. A more scalable system using the library `python-dotenv`. If you start working with many secrets, for example, many API keys, it makes sense to switch to that instead. The current system as implemented in this repository is described below.

Environment Variables can be found in the file `config.py`, as can more explanation. In order to use an environment variable - a value which you expect to be different in local development from our production system - it should be added to that file. In the cases of the Python variable `DATABASE_PASSWORD`, Python will look for an environment variable (on the computer running your website) called `DB_PASSWORD`, and assign its value to the Python variable. This is then usable by the Flask app. It is essential that anything which should remain a secret, like a database password, is never added to your GitHub repository. This makes your password public - giving anyone access to your database. Instead, we can use GitHub Secrets to securely add a password to the production environment. In other words: we can create a database password, add it to GitHub Secrets, and then GitHub can pass it on to App Engine. The last step requires one more trick, though. The App Engine environment is configured by the file `app.yaml`, which does not support reading in environment variables dynamically. Instead, the GitHub Action has a step in it called `Prepare Deployment`, which can add a GitHub Secret to the `app.yaml` file. In this case, the code expects GitHub to have a variable called `PRODUCTION_DATABASE_PASSWORD`. A line of code in `.github/workflows/main.yaml` then adds this password to the file `app.yaml` dynamically, setting to have the name `DB_PASSWORD`. This, in turn, is read in by the flask app. Note that the environment variables can all have the same name, but I have made them different to make it clearer what is what.
