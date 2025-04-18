## Olivia Soppa Cs 178 Project 1

Credit: chatgbt was used to help write html code and troubleshooting errors 

This Flask App allows for users to view country population for RDS SQl
An Dynamodb table is used to allow for users to input reviews and year of visit
The app supports CRUD functions for the COuntryNotes DynamoDB table 

CRUD Routes 
- Add rating
- Display ratings
- Delete Rating
- Update Rating

Due to numerous errors completing the project, the dynamo CRUD functions do not work. There were errors trying to connect the table to my app.  However, the CRUD functions and routes are avaliable and implimented and buttons on the front end of the website display show potential functionality.

## Files
templates (html)
- add_rating - takes in username, rating and yearvisited to add rating to CountryNotes
- delete_rating - takes in username to delete rating from CountryNotes
- update_rating - takes in username, new rating and new yearvisited to add upsating rating to CountryNotes
- display_rating - takes country to display ratings from CountryNotes
- index - main homepage for website with buttons for CRUD and top 15 countries table
dbCode.py
- contains functions to be called and used within files (ex. execute query, connect)

FlaskApp.py
- contains all app routes to direct connections and impliment CRUD functions
- try/except blocks are used to handle errors and raise exceptions 
