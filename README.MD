# Questioner

Questioner is a web app that enables users to create meetups and post questions and comments on the meetups and do basic log monitoring via the user's profile. Users can monitor upcoming meetups and even go further to have a curated list of top questions on upcoming meetups accessible right in their profile.


## Features Currenctly supported by the api
 1. create a meetup record.
 2. Create a question record.
 3. Get a specific meetup record
 4. Get all meetup records.
 5. Upvote or downvote a question.
 6. Rsvp for a meetup.


## Getting Started

### Prerequisites

- ```Python3``` - A programming language that lets us work more quickly (The universe loves speed!).

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment

### Installing

First install python3 into your machine.
Clone this repository and cd into it.
> $ git clone https://github.com/wachiranduati/Questioner.git 
> $ cd Questioner
- Install a virtual Environment and activate it

> $ python3 install virtualenvironment
> $ virtualenv env	
> $ source venv/bin/activate
- Install all the dependencies using

>$ pip install -r requirements.txt

- run the app
> $ export FLASK_ENV=development
> $ export FLASK_APP=run.py
> $ flask run

## Running the tests


To run tests on this application simply run pytest in the root folder of the application

> $ pytest


## Built With

- ```Python3``` - Python is an object-oriented, high-level programming language with integrated dynamic semantics primarily for web and app development

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment
- ```Flask-restplus``` - A tool

## Authors

* **Nicholas Nduati** - *Initial work* - [WachiraNduati](https://github.com/wachiranduati)

## License

This project is licensed under the MIT License

## Acknowledgments

* *Nbo-36 #Team3*
* Solomon Macharia
* Kelyn Paul
* Nbo-36 members
