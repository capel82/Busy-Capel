## Introduction
The initial idea of this project was originated from my personal view of keeping a recipe diary of high protein diets for my busy lifestyle.  Therefore I have created an online cookbook web application for me to share high protein recipes to users as well as allowing them to store and edit their own recipes.   
This incorporating skills in particular Python, Flask and Mongo DB Atlas learned from modules taught by Code Institute.

### A. Objectives
The objectives of creating this cookbook are:
* to allow users to try out high protein recipes posted on online cookbook.
* to allow users to select meal categories for easier viewing of recipes.
* to allow users to save their own recipes.
* to allow users to modify their own recipes in their account through the functions of  edit or delete.

### B. Wireframes

[wireframes1](.../mobile.pdf)

[wireframes2](.../wireframe1.png)

[wireframes3](.../wireframe2.png)

[wireframes4](.../wireframe3.png)

### C. User Stories
**Homepage**
The Jumbotron image shows a picture of food indicated to me that I have landed on a web application about food. The caption of *’High Protein Recipes’* gives me the impression that it is all about recipes made with high protein contents.  Below the title,  I am made aware the benefits of high protein content diets.
The button ‘Browse Recipes’ with hover effect prompts me to click on it which leeds me to all the recipes posted by Editor.

Below the jumbotron, there are few images of recipes displayed, which also linked to individual recipes through its recipe name.  The title of *’Be inspired’* encouraged me to venture more into recipes posted. The cookbook can also be easily navigated with the button *More Recipes Here* without me needing to scroll to the top.

The bottom footer shows that I could follow the Editor on her Facebook, Twitter, Instagram or Pinterest.

**All Recipes page**
This page displays all recipes in the database with links to individual recipe page.  The pagination is clearly indicated on the bottom.  In addition, I can also filter the categories of meals  through the category dropdown menu shown above the recipes.

**Starters Page/Mains Page/Desserts Page**
Each of these pages shows all recipes in categories of Starters, Mains or Desserts.  The dropdown menu for meal categories is also available on these pages for me to easily navigate between different categories.  Each recipes brings me to individual recipe content.

**Register Page**
I can register my own account by clicking on Register on the navbar which brings me to a Create A New Account Page.  The form is easy to fill as only required three inputs.  If any fields I do not fill in, it will prompt me to enter details.  It also alerts me if my confirmed password does not match with password I entered for accuracy.  If I have successfully register, a message will flash out to tell that I have successfully registered an account.  If an email address has already being used before, it will also informed me that the email has been taken and to try another one.

I also noticed that the navbar changed that I have the options of Add recipes, My recipes and Logout option in addition to view the Editor’s recipes.

**Login page**
Login page is also simple as I only need to enter the email address and password. Email address is actually easier to remember than username. I will know that I have logged into my account from message of *Login successful for ‘email'*. The navbar changes with the options of Add recipes, My recipes and Logout option in addition to view the Editor’s recipes.

**Account page**
This page only displays the account holder’s recipes.  

**My Recipe page**
Each recipe saved is linked to individual recipe with the buttons of Edit or Delete at the bottom of the recipe.  The bright and contrast colours of the buttons made me aware of the different functions in addition to the displayed words.  The Edit button brings me to the form I have filled in before.

**Add Recipes Page**
This form is for me to add in my own recipe or any recipes I wish to be saved into my account.  There is special notes section for me to note down any information i want such as reminder or source of recipes.  Once i click on submit button, I will know my recipe is successfully saved to my account with the message of ‘Your New Recipe has been added to your account.’.

**Edit Page**
This form allowing me to modify my recipes easily.  The data I inserted before in Add Recipes form is automatically pre-filled. If i click on the delete button, my chosen recipe will be deleted with a message flashing out that the recipe has been deleted.

###  D. FEATURES
-**Navbar** - This features uses Bootstrap Navbar toggles and collapsible features which allow when in smaller screen to toggle and collapse, featuring  like a dropdown for easier navigation. It is fixed top in feature to allows users to switch between pages easily. In addition, if user is logged in, the navbar changes with the options of My Recipes, Add Recipes and Logout appear on the right side.  This incorporating the if else statement and Jinja in the navbar.html page.

-**Footer** - The footer is simple with ‘Follow Me’ wording which clearly indicates to users that they can also follow the Editor on social medias. This uses font awesome social media icons.

-**Homepage** - Bootstrap 4 Jumboton with responsive heading used in the top section as shoutout to inform user the main content of this online cookbook. Button feature is used so user can click on ‘Browse Recipes’ which leads to All Recipes page.

Below the jumbotron is a section which uses bootstrap 4 grid system and card deck features for responsiveness and displaying the individual recipe’s image and title which also links to the individual recipe. Only 4 recipes displayed in the homepage so that homepage will not be overcrowding with informations.  ‘More Recipes Here’ button is used under the card-deck to allow user to navigate to all recipes page which displays all recipes in the Editor’s database.

-**All Recipes Page** - This page uses card decks group components from Bootstrap 4 to display all Editor’s recipes in the database.  It also uses Bootstrap 4 dropdown menu for filtering meal categories.  Each card shows the recipe image and title fetched from the database. The recipe title is a link to individual recipe page. Bootstrap 4 Pagination is used here.

-**Starters/Mains/Desserts Recipes Page** - Each of these pages showed all the menu displayed by categories.  The features used similar to All Recipe Page where Bootstrap 4 card deck group and dropdown menu have been used.


-**Login page and Registration page** - This pages uses form features of Bootstraps and Flask WTForms for validations and responsiveness. Data Required function is used to ensure user fills in all fields.  If user is created a new account, a flash message will appear to inform user that his or her account has been created.  This is the same when user successfully logged into his or her accounts.  A flash message will also appears if user’s email address had been taken before.

-**Add/Edit Recipe Page** - This page also uses Bootstrap 4 and Flask WTForms features that allow user to enter recipes and inserted into user’s database.  A field for note allows user to enter remarks or information related to their recipes. Flash message will inform user whether their recipe has been saved or updated.

-**My Recipe Page** - This page only displays user’s saved recipes using the Bootstrap 4 card deck group feature.  A default image is used here. Each recipe’s title is linked to individual recipe page.

-**Individual Recipe Page for user’s recipes** - This displayed individual user’s recipe quite similar to the single editor’s recipe page apart from the ‘Edit’ and ‘Delete’ buttons at the end of the page.  The buttons are in contrasting colour so that user will not click on the wrong button.
Flash messages will appear if the recipe has been deleted.

**_Features to implement in future_**

1. To design search filter to allow user to search by keywords.
2. To design more filters such as by preparation time or cooking time.
3. A modal of confirmation for delete button to double check if user intentionally wanting to delete the recipe.
4. To design a blog page to allow Editor’s to post new discovery and opinions of his or her recipes.

### E.Technologies Used

[Adobe](:https://www.adobe.com/ie/products/xd.html?promoid=PYPVQ3HN&mv=other/)

Why it is being used:  Recommended by my mentor and it gives a good idea of wireframes even to the details of colours and images.

[Bootstrap v 4.4](https://getbootstrap.com/)

Why it is being used: As mobile digitals are increasing and so widely used, Bootstraps has been chosen for mobile first -approach for the design of the webpages so that it can be easily made responsive with many different features offered.

[Bootstrap own Javascript, jQuery and Popper.js](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

 Why it is being used: As many of bootstrap v4.3 required use of Javascript, jQuery and Popper.js, these technologies were also incorporated into this project.    
     
**HTML5**
 
 Why it is being used: Using up-to-date features offered which is HTML5 through Cloud9 IDE for programming languages.

**CSS3**

Why is being used: Using the latest Cascading Style Sheets to support for responsive designs and styling.


[W3C Markup Validation Service](https://validator.w3.org/)
Why it is being used: to help to validate codes


[google fonts](http://fonts.google.com)
why it is being used: use to style the fonts in all the pages


[Font awesome](https://fontawesome.bootstrapcheatsheets.com/)
why it is being used: to add icons

[Python 3](https://www.python.org/downloads/)
why it is being used: back-end programming languages
 
[Flask-Pymongo 2.3.0](https://api.mongodb.com/python/current/)
why it is being used: extension tool for Python to work with MongoDB.

[Flask 1.1.1](https://palletsprojects.com/p/flask/)
why it is being used: popular framework for easier start-up in making the web application.

[Werkzeug 0.16.1](https://palletsprojects.com/p/werkzeug/)
why it is being used: for generating and verifying password hashing.

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try1?utm_source=google&utm_campaign=gs_emea_ireland_search_brand_atlas_desktop&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&gclid=EAIaIQobChMI3J2C6P-o6AIVA7DtCh0YZgVVEAAYASAAEgKxp_D_BwE)
why it is being used: to store database

[Jinja 2.11.x](https://jinja.palletsprojects.com/en/2.11.x/)
why it is being used: templating languages for Python for fetching backend data to the front-end.

[Heroku](https://www.heroku.com/)
why it is being used: cloud based application allowing me to build and run my application.

#### **Manual testings:**
In addtion to Chrome Development Tools, manual testings were done with *iphone SE* and *MacBook Air*.

**Navbar** - clicking on all pages to ensure they are all properly linked to the right page.  Toggle ability was tested in iphone SE.

**Buttons** - all manually tested with workable links. When I clicked on the buttons, background color and font-color changed indicating the hover effect worked.

**Recipes Titles** - clicking on the recipe titles on All Recipes and My Recipe pages directed me to individual recipe page.

**Register form** - tried out by entering email and password.  Also tried out with missing field that the message prompt out to ask to fill in.  New account created with message saying account is successfully created.

**Login Form** - tried out with the email and password registered. Message came out saying I am successfully login.  

**Dropdown Menu for Categories** - Manually selecting Starters, Mains and Desserts. All displayed correctly categories of recipes in the database.

**Edit Form** - Button for Edit worked correctly and the form fetched the correct recipe information.  Update route also worked correctly when submitting the form.

**Delete button** - My recipe that was chosen to be deleted was successfully deleted with a message flashed out to inform me.

### G. Deployment to Heroku
1. I used Gitpod as my IDE to write my codes.  I cloned **Code Institute Gitpod-Full-Template** from Github by clicking on the green button *Use this template*  that brought me to create a new repository.  This helped to copy all the information in the template to my own Github account. Then I clicked on Gitpod green button on the top right corner to start my IDE.

2. In Gitpod, I created `run.py`, `Procfile` and  `requirement.txt` files.

3. Using Gitpod terminal, I then `git add .`, `git commit -m` and `git push` them to my repository.

4. Next, I installed Flask, flask-pymongo and dnspython with terminal commands (`pip3 install Flask`, `pip3 install flask-pymongo`, `pip3 install dnspthon`).

5. Then, I registered a new account in [Heroku](www.heroku.com).

6. After that, I installed Heroku in IDE with terminal command ` npm install -g heroku` and login with the command of `heroku login-i`.

7. I opened up [Heroku](www.heroku.com) and logged into my account which i created beforehand.  On the top right corner, I clicked on ‘New’ button to create a new app. 

8. I chose an app name and select the Europe Region.

9. In the *Deployment method* in Heroku, under *Deploy section*, I have chosen [Github](www.github.com) and I also ensure my App connected to Github appeared on it.

10. I have also selected automatic deploys from my Github Master branch.

11. Under *Overview* in Heroku, I set the *dynos* to `web python run.py`.

12. Under *settings* in Heroku, I clicked on *reveal config var* to enter information for:

	IP = 0.0.0.0

	PORT = 5000

	MONGO_URL = value

	SECRET KEY = value

13. Now, any codes pushed from my IDE to Github would automatically deploy to Heroku and I can open the app with the button *Open App* on the top right corner of the app in my heroku account

### G. Local Deployment

1. An IDE will be needed to run this project locally.

2. In [Github] https://github.com/capel82/Busy-Capel, choose the Busy Capel repository and on the right top corner, click on *clone or download* green button to clone the codes. 

3. Copied the URL  *https://github.com/capel82/Busy-Capel.git*and at the IDE terminal type in `git clone https://github.com/capel82/Busy-Capel.git` to clone into chosen working directory.

4. All requirements.txt, Procfile, run.py files need to be installed and ensuring IP (0.0.0.0) and PORT (5000), Mongo URL and secret key are updated.

5. The app can be initiated now with command `python3 run.py`.

### H.Credits
a. **Codes :**- taken and adjusted

Corey Schafer Flask Python Series at [youtube](www.youtube.com) - especially in using Flask-WTForms and flash messages.

Pretty Printed at Flask Pymongo at [youtube](www.youtube.com)

@2BN-Chris_alumnus in Slack Community posted about codes for route update recipe.

b. **Photos and recipes contents used:** - All  are taken from 
[BBC Good Food](www.bbcgoodfood.com), 

[Sainsbury](https://recipes.sainsburys.co.uk/recipes/healthy-eating/chargrilled-chicken-shawarma-with-smashed-chickpeas) and 

[Jenniferbanz](https://jenniferbanz.com/).

### I. Acknowledgement

A special thanks to my mentor **Maranatha Ilesanmi** who has very kindly encouraged, guided and taught me with so much patience towards me in finishing this third milestone project.

Working from home in this COVID-19 crisis was not easy but I am thankful for my husband and kids who are very considerate whenenever I tried to work through this project.

Not forget the tutors in Code Institute who have been faithfully helping to solve any problems arising in completing this project.