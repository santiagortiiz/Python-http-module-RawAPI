# Guide

## 1. Install

+ Create the virtual environment with the command:
    python -m venv venv
+ Install all dependencies with the command:
    pip install -r requirements.txt

## 2. Setup Environment Variables

+ If you use a database other than the dummy database, set the credentials in the .env file

## 3. Setup Plugable Controllers and Storage

+ In /api/books you will see the index.py file, you must set the variable "store"
  with the DummyDb database, or the Postgres database.

## 3.a If you decide to use PostgreSQL
+ Download PgAdmin
+ Connect to your localhost server
+ Create a database
+ Open the query tool
+ Open "books.sql" and "pages.sql" files. You can find them on the /mocks directory
+ Run Both Scripts to generate dummy data

## 4 Start the server

+ Start the server with the command:
    python main.py

## 4.a Requests exec

+ You need a REST CLIENT. I suggest you to install rest-client from vscode becouse here
you will find a directory called "rest-client", which has the "books.http" file and there
you have the endpoints that you need for tests 

+ List books: 
    http://localhost:8000/books
+ Retrieve a book: 
    http://localhost:8000/books/<book_id>
+ Retrieve the content of one page of the book:
    http://localhost:8000/books/<book_id>/<page>

Notes: I do not have enough time to include the format in the last endpoint


