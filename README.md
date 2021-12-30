# IMGDictionary -- CS50_FinalProject
### Video Demo: https://youtu.be/JY3hqycnIe4
### Heroku app URL: https://cs50-myvoc.herokuapp.com/
### Description

This is a web application aims for helping vocabulary learning by searching for images on the web and register them as a vocabulary book. You can register any vocabularies you want to remember with meanings and images so you can refer to it anytime you want to  memorize words you may frequently forget.You can learn how to use by watching video demo.

The features of this app are as follows:

- User Registration
- Register vocabuluary with meaning and an image 
- Search for Images via Bing Image Search API and show them as a html template
- Limit how many times a user can use search function (Due to API's limitation)
- List vocabularies the user registered 
- Pagination for the list
- Delete registered vocabulary

#### Configuration of this app are as follows
Frontend: Bootstrap, HTML
Backend: Flask
ORM: SQLAlchemy
DB: PostgreSQL
infrastructure: Heroku
API: Bing Image Search API (Free Subscription Plan)

##### Background of design choices
For this project, I set it as technical challenge to deploy a web application to the infrastructure other than CS50 IDE.
CS50 IDE did everything for me but deploying a web app on Heroku takes many efforts which CS50 didn't require such as creating Procfile, preparing for requirements.txt, etc. Even so, Heroku seemsed the best choice for beginners. To deploy this application on Heroku, there are other two technical challenges I have to face with:
- Use Database language other than SQLite which I am familiar with thanks to CS50 courses.
- Upload any images searched for on the web

- Use Database language other than SQLite which I am familiar with thanks to CS50 courses.
Heroku does not support SQLite. When I had to use another SQL language, ORM(SQLAlchemy) became the 1st choice for me. Since I want to continue coding even after finishing this course, I want to choose something universal. ORM allows us to write same code regardless any SQL direct so this is the reason why I chose to learn ORM.
- Heroku do not support uploading any images on the app
When I decided the design of final project which needs the first thing came to my mind is uploading images searched for on the app server. However, Heroku does not support uploading any files. Due to this restriction, I decided to link images directly even though I know it might not be recommended. Due to this reason I made this application for mainly my personal use. So that, users can search for images only 10 times.


Also, for this application, user should be able to access images linked with vocabulary with ease. So that I decided to use API provided by Search engine. I chose API provided by Bing because it provides me with best for free subscription plan.

#### How each file functions

- application.py -- main application. It handles with login, listing vocabulary, add vocabulary, search Images, delete vocabulary from the list, etc.
- helpers.py -- handles with errors and requests users to log in.
- modules.py -- Specifies all requirements for ORM.
- Myapplication.db -- SQLite Database, it is used for local validation.
- Procfile -- Heroku needs this
- requirements.txt -- lists things to run on another environment rather than my local one.
- README.md -- this file
- static 


#### When Launching application

If you deploy