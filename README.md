# Jamie Boyd Photography

[![Build Status](https://travis-ci.com/jboyd8/jamieboydphotography.svg?branch=master)](https://travis-ci.com/jboyd8/jamieboydphotography)

# Milestone Project 4
## Description
---


[Deployed Website](https://jamieboydphotography.herokuapp.com/)

## UX/UI
---


### User Stories
* User Stories here


### Wireframes

![]()
![]()
![]()
![]()
![]()
![]()


## Features
---
#### Current Features



#### Future Features



## Technologies/Support Used
---
Below is a list of technologies I used to build my dashboard.
* HTML - HTML5 provided the structure of my website. I tried to use semantic elements where possible to ensure the best structure.
* CSS - Used to style my page.
* [Bootstrap](https://getbootstrap.com/) - Used primarily for the grid system. I find this a really good way to position my elements where I want them.
* [VSCode](https://code.visualstudio.com) - This is my text editor. It has a built in terminal so I could do everything I needed to from one environment.
* [Git](https://git-scm.com) - Git was used for version control. Allowing me to create backups whenever significant changes were made to my code.
* [GitHub](https://github.com/) - This is where my repository is held externally. I will also use GitHub pages to deploy my website.
* [Google Fonts](https://fonts.google.com/) - Used to import specific fonts I wanted to use on my website.
* [Python](https://www.python.org/) - Python was the language used to build the backend of the website.
* [Django]() - Python framework used in order to build out the routes/views of my website.
* [PostGres]() - 
* [typewriter.js]() - 


## Testing
---

Firstly, i made use of some automated tests towards the end of the development process. I have created a separate python 
file to store some unit tests i have written. I made use of Python's unittest library in order to write my tests. This made 
checking that everything was working a lot easier and that all my functions were working as expected. I also made use of a CSS and HTML 
validator to make sure it was all valid working correctly.

The bulk of my testing was done manually all the way throughout the development process. I constantly checked my website in the browser to make
sure everything was working as expected. I also periodically checked the website in other browsers to make sure everything was working the same 
there too. I also monitored the network using the Chrome dev tools and checked the requests and responses with the API calls. 
I made use of the dev tools to help develop the styles as well before implementing them into the actual code. I consistently checked 
the MongoDB GUI to make sure that my entries were being created/read/updated and deleted properly from the database.

Additionally, I also sent my deployed website to friends and family and had them create an account and test all the functionality 
to ensure firstly it was working with different browsers, but also to make sure they saw it as a responsive website and their different 
devices. I also used the dev tools to test this throughout development, using a mobile first approach.

## Notable Bugs
---
The website doesn't render very well on IE. The footer isn't recognized and there are a few buttons that dont work. I am trying 
to find a solution to fix this.

Footer appearing over about content and blog. About not showing in dev tools so hard to fix

## Deployment
---
My website was created using VSCode. VSCode is a text editor with a built in terminal. I chose to use a text editor/IDE 
outside of AWS Cloud9 to gain experience working outside of a browser. Once I had created my file structure and first 
HTML page, i initiated a local repository using GIT which was downloaded onto my machine previously. I then created an 
external repository in GitHub and linked the local and external repositories. This allowed me to version control 
throughout the lifespan of the development.

* I created a new environment in VS Code
* Created a new virtual environment.
* In the bash terminal, entered 'git init'
* Created all my folders and files.
* Entered 'git add .' into the bash terminal
* Entered 'git commit' into the bash terminal and created my initial commit
* I then linked my local git repository to a GitHub repository.
* I then followed the below steps to deploy the site to Heroku.

To deploy the website to Heroku, I followed the below steps:
* Created an Heroku Account.
* Created a new project.
* From the deployment method section of the Deploy tab, I selected GitHub, and then entered my github repo link in the 
field provided.
* Every time I push to GitHub it will automatically send the updates across to Heroku.
* I then also had to create some Config Vars in the settings tab, to reflect the environment variables created 
in the .flaskenv file that is in .gitignore.
* [Website Link](https://jb-milestone-project-3.herokuapp.com/)

### To run this project locally

* Follow this link to the [GitHub Repository](https://github.com/jboyd8/milestone-project-3)
* Click on the 'Clone or Download' button.
* Copy the URL provided.
* Open a bash terminal, move to your desired directory.
* Type 'git clone' and paste in the URL.
* Create a .flaskenv file and store three environment variables. (API_KEY, MONGO_URI and SECRET_KEY)
* In order to complete this you will need a MongoDB Atlas account and an account with API Football.


## Credits
---
* To my mentor, [Reuben Ferrante](https://github.com/arex18), for guiding me through the process and offering assistance when necessary to point me in the right direction.
* The Slack community. The help a student is able to receive from the other students is a really great tool to have.
* [HTML Color Code](https://htmlcolorcodes.com/) - Used this website in order to obtain hex codes whilst styling my pages.
* [W3C Validator](https://validator.w3.org/#validate_by_input) - A validator used to check my HTML and CSS structure and format periodically throughout the build.
* [CSS Autoprefixer](https://autoprefixer.github.io/) - Used to prefix CSS for browser support.
* Concepts iOS app - Used to build wireframes.

