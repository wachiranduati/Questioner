# Questioner

Questioner is a web app that enables users to create meetups and post questions and comments on the meetups and do basic log monitoring via the user's profile. Users can monitor upcoming meetups and even go further to have a curated list of top questions on upcoming meetups accessible right in their profile.

[![Build Status](https://travis-ci.org/wachiranduati/Questioner.svg?branch=develop)](https://travis-ci.org/wachiranduati/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/wachiranduati/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/wachiranduati/Questioner?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/640293f83f49c685503a/maintainability)](https://codeclimate.com/github/wachiranduati/Questioner/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/640293f83f49c685503a/test_coverage)](https://codeclimate.com/github/wachiranduati/Questioner/test_coverage)

## Features Currenctly supported by the api
 1. create a meetup record.
 2. Create a question record.
 3. Get a specific meetup record
 4. Get all meetup records.
 5. Upvote or downvote a question.
 6. Rsvp for a meetup.

## Functional Api Endpoints
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/16214aa917050d5b8926)

Method        | EndPoint      | Functionality |
------------- | ------------- | ---------------
POST  | /api/v1/meetups  | Create a meetup record   |
GET  | /api/v1/meetups/<meetup-id>  | Fetch a specific meetup record.   |
GET  | /api/v1/meetups/upcoming   | Fetch all upcoming meetup records   |
GET  | /api/v1/questions/<questionId> | Fetch a specific question   
POST  | /api/v1/questions | Create a question for a specific meetup.   |
PUT  | /api/v1/questions/<question-id>/upvote | Upvote (increase votes by 1) a specific question.   |
PUT | /api/v1/questions/<question-id>/downvote | Downvote (decrease votes by 1) a specific question.   |
POST | /api/v1/meetups/<meetup-id>/rsvps| Respond to meetup RSVP. 

[View the Questioner documentation](https://documenter.getpostman.com/view/6358115/RznLHGqe)

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

###### Typical test on an end point on Questioner
*This is how a correct payload to the `create meetup endpoint` [here](https://questionerplus.herokuapp.com/api/v1/meetups)* looks like.
>{
"location" : "Kasabun",
"images" : ["https://test.materia.io", "https://doesitwork.com"],
"topic" : "Purely testing this",
"happeningOn" : "12-23-2010",
"Tags" : ["Grand Turismo", "Nduthify", "Sleep"],
"details": "lorem ipsum and some other mumbo jumbo all foall in here"
}

###### Expected success response

>{
    "status": 201,
    "data": "The meetup *Purely testing this* was created successfully"
}

##### Response should an error arise
*This was due to a missing **location** field*
{
    "status": 400,
    "error": "Error with the request field the location field should not be longer than 100 nor smaller than 4 or does not exist"
}

*This was trying to send the same payload again **recreate the same meetup** *
{
    "status": 409,
    "error": "Sorry the meetup already exists"
}

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
* Jackline Muthoni
* Nbo-36 members
