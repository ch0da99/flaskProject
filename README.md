This is a simple web market application featuring multiple functionalities:
  - User register/login
  - Money system (virtual dollars)
  - Access to all items for buying
  - Opportunity to sell previously bought items back to market
  
This is full-stack application that was built using Flask framework for 
Back-end part and html with help of Bootstrap and Jinja templates for Front-End.

Originally the application was built with Sqlite database. If you want to change
it you can create .env file which will contain variable SQL_DATABASE where you are
supposed to store your connection string to new database.

Example context of .env file:
DATABASE_URL = 'sqlite:///market.db'

If you don't add this file, by default you will be connected to your local sqlite 
database if it exists.
