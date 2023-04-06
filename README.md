# __HANGMAN__

Hangman is a Python based game played in the terminal.

The live website can be found [here](https://pp3-charlie-hangman.herokuapp.com/).

![Responsive Mockup](images/amiresponsivePython.png)
<br>
<br>

## __How to play__
1. The computer chooses a random word and displays a series of dashes on the screen to represent each letter of the word.
2. The player then guesses a letter that they think might be in the word.
3. If the guessed letter is in the word, the computer replaces the appropriate dash(es) with that letter. If the letter is not in the word, the computer keeps track of the wrong guesses and displays a part of the hangman figure.
4. The player continues to guess letters until they either guess the word correctly or they have made six incorrect guesses, causing the hangman figure to be completed and the game to be over.
5. If the player guesses the word correctly before the hangman is completed, they win the game. If the hangman figure is completed before the player guesses the word, they lose the game.
<br>
<br>

## __Features__

### __Existing Features__

- __Start__

  - Nice header showing what kind of game it is and it asks for the users name.

![Start](images/start.png)

- __Game Start__

  - Small info about the rules.
  - Press enter to start the game.

![Game-Start](images/startgame.png)

- __Guesses__

  - The computer randomly selects a city from the words.py list.
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
<br>
<br>

## __Testing__ 

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Tested in my local terminal and the Code Institute Heroku Terminal.

![PEP8 Validator](images/pep8Validator.png)
<br>
<br>

## __Bugs__

### __Solved Bugs__
- Indentation and white-spacing problems.
- Some code was to long, 81 characters, had to slim it down.

### __Unfixed Bugs__
- No reports of bugs.
<br>
<br>

## __Deployment__

### __Heroku__
1. Go to the Heroku Dashboard.
2. Click New.
3. Select to create a new app.
4. Add Config Var's for Creds and Port
5. Set the buildbacks to Python and NodeJS in that order.
6. Link the Heroku app to the repository.
7. Click on Deploy, you can choose manually or automatically.
<br>
<br>

### __Forking the GitHub Repository__

To make a copy of a GitHub repository without affecting the original, you can fork it by following these steps:
1. Locate the repository in your GitHub account and log in.
2. Click on the 'Fork' button located on the top right of the repository page.
3. A copy of the repository will then be available in your own GitHub account.
<br>
<br>

### __Making a Local Clone__

To create a local clone of the repository, follow these steps:
1. Find the repository in your GitHub account and log in.
2. Click on the 'Code' button located next to 'Add file'.
3. Under the 'Clone with HTTPS' option, copy the link.
4. Open Git Bash.
5. Navigate to the directory where you want to create the cloned repository.
6. In your IDE's terminal, type 'git clone' followed by the URL you copied.
7. Press Enter.
8. The local clone of the repository will now be created.
<br>
<br>

## __Technologies Used__

### __Languages Used__

Python.

### __Libraries & Programs Used__

- [Gitpod](https://www.gitpod.io/) - For version control.

- [Github](https://github.com/) - To save and store the files for the website.

- [Heroku](https://www.heroku.com/) - To deploy the project.

- [Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

- [ASCII art](https://ascii.co.uk/art/hangman) was used for the Hangman header.

### __3rd party libraries__

- Coloroma - I wanted to give the user visual feedback and a more fun experience with changing the color of certain text.

## __Credits__

- I followed the tutorial from [Kite](https://youtu.be/m4nEnsavl6w).
- Slack for troubleshooting code.
- Code Institute for the deployment terminal.