## Questioner

Questioner is a web app that enables users to create meetups and post questions and comments on the meetups and do basic log monitoring via the user's profile. Users can monitor upcoming meetups and even go further to have a curated list of top questions on upcoming meetups accessible right in their profile.

**build score**
[![Build Status](https://travis-ci.org/wachiranduati/Questioner.svg?branch=develop)](https://travis-ci.org/wachiranduati/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/wachiranduati/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/wachiranduati/Questioner?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/640293f83f49c685503a/maintainability)](https://codeclimate.com/github/wachiranduati/Questioner/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/640293f83f49c685503a/test_coverage)](https://codeclimate.com/github/wachiranduati/Questioner/test_coverage)

## The required API Endpoints that enable one:
 1. create a meetup record.
 2. Create a question record.
 3. Get a specific meetup record
 4. Get all meetup records.
 5. Upvote or downvote a question.
 6. Rsvp for a meetup.

## The list of the functioning API Endpoints

Method        | EndPoint      | Functionality |
------------- | ------------- | ---------------
POST  | api/v1/auth/signup  | Register a user   |
POST  | api/v1/auth/login  | Login a user   |
GET  | /api/v1/questions   | Fetch all questions   |
GET  | /api/v1/questions/<questionId> | Fetch a specific question   
POST  | /api/v1/questions | Post a question   |
Delete  | /api/v1/questions/<questionId>| Delete a question   |
POST | /api/v1/<questionId>/answers| Post an answer to a question   |
PUT | /api/v1/questions/<questionId>/answers/<answerId>| Mark an answer as accepted or update an answer. |


### Requirements Building blocks.
- ```Python3``` - A programming language that lets us work more quickly (The universe loves speed!).

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment

 
 ### Requirements Building blocks.
- ```Python3``` - A programming language that lets us work more quickly (The universe loves speed!).

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment


## Technologies used
- Python 3.6
- Flask framework

## Author: Nicholas Nduati