# apache-beam-demo

This repository is a demo of a simple beam pipeline, illustrating some of the core concepts and how to run them.

### Setup

I strongly recommend running beam jobs in a clean virtual environment - I have run into significant versioning issues, or issues using the Dataflow runner when not doing this. Full detailed instructions on how to set up a python virtual environment can be found [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), but the quick summary (for Mac/Linux users) is:

1) Install virtualenv package if you have not already done so with `python3 -m pip install --user virtualenv`
2) In terminal, navigate to the project where you want to create a virtual environment
3) Run `python3 -m venv env` to create a virtual environment named "env" - you can change this name if you wish, but in general you won't have multiple environments in the same project so there is no need
4) Run `source env/bin/activate` to activate the environment. You're now operating in the virtual environment, and any packages you install will only be reflected here

Once the virtual environment is setup, you must install any packages you need. The packages required for this demo are in the requirements.txt file, which can be installed with `pip install -r requirements.txt`. In fact there is only one dependency (apache-beam[gcp]), but a real project probably has more (e.g sklearn)
