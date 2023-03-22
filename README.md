# Colourful Semantics Speech Therapy Web App
#### Video Demo:  <URL https://youtu.be/mKqsqo1KdIU>
#### Description:
Colourful Semantics Web App is a digital implementation of the colourful semantics speech and language therapy tool. Colourful semantics is a colour-coded language system that has been shown to improve sentence structure, vocabulary, comprehension, and other issues in children with speech delays. This app aims to widen accessibility to this fantastic therapy tool, which is currently generally offered in physical pack form following professional consultation and not widely available to parents. It also aims to make the process more efficient for learners by reducing the time spent setting up physical cards, increasing engagement and making learning time more effective.

#### Table of Contents
Features
User Experience
Technologies
Installation
Running the Project Locally
Dependencies
Customization
Components
Challenges
Known Limitations
Additional Resources
Contributing


#### Features
Interactive web app with randomized scenes and answer choices
Easy addition of new cards and scenes
Feedback on user's answer selections
Compatible with multiple devices, optimized for iPad

#### User Experience
The user loads up the web app through the site davebrunskill.pythonanywhere.com or via flask run, this presents a random scene and loads up a random selection of "who" options that include the correct answer along with five incorrect options in a randomised order. Users then click on their answer choices for each category (who, doing, what, where) and can submit their answer to receive feedback on their selections. After submitting, a new random scene is presented, allowing the user to rapidly move on to the next scene without the delay of setting up the physical pack.

Users can add new cards by creating images of the word with the correct background color and saving the file path in the appropriate folder (e.g., 'cat'.jpg in the /static/who folder).

#### Technologies
Languages and Frameworks used in the project:

Python: Server-side programming logic
Flask: Web application framework
Bootstrap: Framework used for styling the site
HTML/CSS: Structuring the front end of the site

#### Installation
The app can be ran install free via the web using: davebrunskill.pythonanywhere.com. Alternatively to run a local version refer to the running this project locally section below.

#### Running the Project Locally
Clone the repository: git clone https://github.com/brunskid23/colourfulsemantics.git
Change to the project directory: cd colourfulsemantics
Install Flask and Flask-Session: pip install Flask Flask-Session
Run the app: flask run

#### Dependencies
The project requires Flask, Flask-Session, and Python to run.

#### Customization
Additional images can be added without adjusting the code. Users can add new cards or scenes by following the instructions under local install section above then add new cards by creating images of the word with the correct background color and saving the file in the appropriate folder (e.g., 'cat'.jpg in the /static/who folder). The project is not built to be customized beyond this but see collaboration section if you would like to develop further.

#### Components
Main components or modules in the project:

index(): Handles the main functionality and processes user selections
logout(): Clears user data and handles the 'reset' function
submit(): Compares users selections against the correct answers
check_answer(): Shuffles the cards and checks that the correct answer is among the options presented

#### Challenges
The biggest challenges encountered during development were obtaining copyright-free images and hosting the project. To generate the images, DALLE was used, which required manual work to match the background colors and add text. Hosting was initially attempted on Heroku, but it did not support the required file system storage for session data. The project was eventually hosted on PythonAnywhere, which required adjustments to file paths and setup.

#### Known Limitations
Some browsers, like Chrome, may experience issues with the checking of answers in the web version, but the app functions correctly on iPad, the main target use case and also work fine when locally run. In the future, cookies or another file storage or database system may be implemented to address these issues.

#### Additional Resources
Please refer to the YouTube video demo for more information about the project: (https://youtu.be/mKqsqo1KdIU)

#### Future development
Additional features and improvments are likely these may include:
Upload functionality - user submitted words and scences via the site
Database - collect answer data and capture metrics for parents and therapist feedback
Dynamically adjusting difficulty – User levels which adjust scenes and vocabulary to a users ability

#### Contributing
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome, please see the future development ideas and feel free to contact me on david.brunskill@icloud.com if you are interested in working on developing this or a similar app further.
