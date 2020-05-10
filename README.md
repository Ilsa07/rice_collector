# Rice collector BOT
A fun project automating the [FreeRice](https://freerice.com/categories/english-vocabulary) game, where rice is donated every time you match a word with its synonym. Witht he use of OpenCV, Tesseract and PyAutoGui, the game can be fully automated!

## Getting Started
1.  Create a folder an a virtual environment.
2.  Clone the project into the created folder and environment.
3.  Install the required packages:
    ```
    pip3 install -r requirements.txt
    ```
4.  Install Tesseract
    With Homebrew (Mac):
    ```
    brew install tesseract
    ```
    Or on Windows download the installer [here](https://github.com/UB-Mannheim/tesseract/wiki), in this case you will have to set the PATH in supporting_functions.py.

## Runing the script and playing the game
1.  The script was written to play on a **Mac** in a **full screen Safari** window, where **multiple tabs are open**.       Depending on your machine, you will have to **adjust the variables in the global_variables.py** file so the problem,    options and button locations as well as the refresh page button location is accurate.
2.  Open the choice of your browser and navigate to: https://freerice.com/categories/english-vocabulary.
3.  Set the number of hours for which the script will run in global_variables.py
4.  Run the rice_bot.py script
5.  You have 5 seconds to switch to the browser and make it full screen.
6.  If you want to abort the program, move your mouse to the top left of the screen (you might have to "fight"              PyAutoGui, but this will abort the program).