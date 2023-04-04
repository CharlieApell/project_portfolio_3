# HANGMAN

Hangman is a Python based game 

The live website can be found [here](https://pp3-charlie-hangman.herokuapp.com/).

![Responsive Mockup](images/amiresponsivePython.png)

## Features 

### Existing Features

- __Start__

  - Nice header showing what kind of game it is and it asks for the users name.

![Start](images/start.png)

- __Game Start__

  - Small info about the rules.
  - Press enter to start the game.

![Game-Start](images/startgame.png)

- __Guesses__

  - The user will get 6 guesses to guess the right European City.
  - Input validation and error checking.
    - You cannot enter the same word or letter twice.
    - You must enter letters.
    - You can guess the city right away.

![Same Letter](images/sameletter.png)
![Same Word](images/sameword.png)
![Wrong Word](images/wrongword.png)

- __Win or Lose__
  - Text shown if the user guesses right or run out of tries.

![Lose](images/lose.png)
![Win](images/win.png)


## Testing 

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Tested in my local terminal and the Code Institute Heroku Terminal.

![PEP8 Validator](images/pep8Validator.png)


## Bugs

### Solved Bugs
- Indentation problems.
- Some code was to long, 81 characters, had to slim it down.

### Unfixed Bugs
- No reports of bugs.

## Deployment

- Go to the Heroku Dashboard.
- Click New.
- Select to create a new app.
- Add Config Var's for Creds and Port
- Set the buildbacks to Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy, you can choose manually or automatically.


## Technologies Used

### Languages Used

Python.

### Libraries & Programs Used

- Gitpod - For version control.

- Github - To save and store the files for the website.

- Heroku - To deploy the project.

- [Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

- [ASCII art] (https://ascii.co.uk/art/hangman) was used for the Hangman header.


## Credits 

### Content

- I followed the tutorial from [Kite](https://youtu.be/m4nEnsavl6w).
- Slack