# Torn check list
GUI application that is using your [Torn City](https://www.torn.com/2531272) API to generate a list of task that you should perform.  

![image](https://user-images.githubusercontent.com/59464917/137616451-2ab048af-c2de-426a-a9ac-85767e2fff9d.png)

# Installation 

This package uses [Pipenv](https://realpython.com/pipenv-guide/#example-usage) to manage dependencies. You first need to install Pipenv :

```pip install --user pipenv```

Then to install all dependencies, in the torn-check-list directory:

```pipenv install --ignore-pipfile```

# Usage

Once the the dependencies are installed, you can run the program with :

```pipenv run python .\torn-task-list.py``` (on Windows).

Alternatively you can use, in the torn-check-list directory:

```pipenv shell```

then run ``torn-task-list.py`` as you would normally do (such as with ``python .\torn-task-list.py`` on Windows).

The file to run is torn-task-list.py 

When you run the app there will be a text field where you put your API and then you just press the only button that exists there. This will automatically generate task that you are yet to complete.
If the API key is invalid you will be informed about it. When the API key is valid it will be saved to setting.json and auto-inserted in to the field next time. You will be still required to press the button.

## Number of API calls
Right now the app updates every 30 seconds making 3 API calls.

# List of all generated task. 

- Reminder to take drugs 
- Reminder to use up your Medical cooldown
- Reminder to use up your Booster cooldown
- Reminder to use your energy refill
- Reminder to go spend your energy on something 
- Reminder to do crimes 
- Reminder to pay your fees
- Reminder to go racing 
- Reminder to go to rehab 
- Reminder to do your daily mission 
- Reminder to bust people from jai
- Reminder to spin wheel of fortune
- Reminder to go buy stuff from NPC shop

