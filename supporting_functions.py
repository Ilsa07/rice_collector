import pyautogui 
import time
import random
import cv2
import numpy as np
from datetime import datetime
import requests
import pytesseract
from global_variables import positions

# On Windows you have to install Tesseract and provide a PATH to it:
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\username\tesseract.exe'



def hour_passed(datetime_object) -> bool:
    """
    DOCSTRING: this function calculates if an hour has passed compared to the input
        datetime object.
    INPUT: datetime object.
    OUTPUT: boolean variable, True if an hour has passed and False if not.
    """
    # Get the current time
    current_time = datetime.now()

    # Calculate the time difference between the two datetime objects
    time_diff = current_time - datetime_object

    # Calculate the number of secondsd passed
    duration_in_s = time_diff.total_seconds()  
    
    # One hour in seconds
    hour_in_sec = 60 * 60
    
    # Check if an hour has passed
    if(duration_in_s > hour_in_sec):    
        return True
    else:
        return False


def take_screenshot(save_image: bool = True, return_image: bool = False):
    """
    DOCSTRING: the function takes a screenshot and depending on the parameters
        saves and or returns the image
    INPUT: save_image is a boolean variable, which if True will save the image
        in the hour_logs folder.
        return_image is a boolean variable which if True will return the image.
    OUTPUT: an image if the return_image parameter was True and nothing if not.
    """
    # Wait before screenshot so the page can show the new problem
    time.sleep(5)
    image = pyautogui.screenshot()

    # Convert the image to an OpenCV image object
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Format the name of the picture
    date = str(datetime.now())[:10] + '_' + str(datetime.now())[11:16]
    image_name = 'current_progress_' + date

    # Remove the invalid characters from the string and format it
    invalid_characters = [' ', ':', '-', '.']
    for character in invalid_characters:
        image_name = image_name.replace(character, "_")
    
    if(save_image):
        # Save the image in the hour_logs folder
        cv2.imwrite('hour_logs/' + image_name + '.jpg', image)
        print('Screenshot taken!')
    
    if(return_image):
        # Return the image object
        return image


def click_on_screen(coordinates:tuple) -> type(None):
    """
    DOCSTRING: move the mouse to a specified location and left click
    INPUT: tuple containing the x and y coordinates of the position
        in the form of (x_position, y_position)
    """
    # Move the mouse to the location in 1 second
    pyautogui.moveTo(coordinates[0], coordinates[1], duration = 1)
    
    # Click on the specified location
    pyautogui.click(coordinates[0], coordinates[1])


def is_synonym(searched_word: str, input_word: str) -> bool:
    """
    DOCSTRING: The function schecks if the searches word is a synonym of the imput
        word by using the datamouse API.
    INPUT: searched_word is the word for which we are trying to find the sysnonym of.
        input_word is the word that is being tested if it is the synonym of the searched_word
    OUTPUT: boolean variable, True if the input_word is the synonym of the searched word
        and false if it is not.
    """
    # Send a get request to datamouse and save the response
    response = requests.get("https://api.datamuse.com/words?ml=" + searched_word)

    # Store the response in a list
    data_list = response.json()

    # Store the synonyms in a list
    new_list = [element['word'] for element in data_list]
    
    # Check if the input word is a sysnonym of the searched word 
    if(input_word in new_list):
        print(f'The sysnonym of {searched_word} was: {input_word}')
        return True

    else:
        return False


def get_choices(image) -> list:
    """
    DOCSTRING: converts a screenshot into a list of words containing the problem
        and the possible solutions to it.
    INPUT: OpenCV image object
    OUTPUT: a list containing the problem (at index 0) and the possible answers
    """
    # Create sub images of the screenshot containing 
    # the problem and the four choices

    problem = image[positions['prob_y_top_bound']: positions['prob_y_bottom_bound'],
                    positions['prob_x_left_bound']: positions['prob_x_right_bound']
                    ]
    # Save the image for debugging
    #cv2.imwrite('hour_logs/problem.jpg', problem)

    first_choice = image[positions['first_y_top_bound']: positions['first_y_bottom_bound'],
                         positions['first_x_left_bound']: positions['first_x_right_bound']
                         ]
    # Save the image for debugging
    #cv2.imwrite('hour_logs/first_choice.jpg', first_choice)
    
    second_choice = image[positions['second_y_top_bound']: positions['second_y_bottom_bound'],
                          positions['second_x_left_bound']: positions['second_x_right_bound']
                          ]
    # Save the image for debugging
    #cv2.imwrite('hour_logs/second_choice.jpg', second_choice)

    third_choice = image[positions['third_y_top_bound']: positions['third_y_bottom_bound'],
                         positions['third_x_left_bound']: positions['third_x_right_bound']
                         ]
    # Save the image for debugging
    #cv2.imwrite('hour_logs/third_choice.jpg', third_choice)

    fourth_choice = image[positions['fourth_y_top_bound']: positions['fourth_y_bottom_bound'],
                          positions['fourth_x_left_bound']: positions['fourth_x_right_bound']
                          ]
    # Save the image for debugging
    #cv2.imwrite('hour_logs/fourth_choice.jpg', fourth_choice)
    

    # Create a list of images of the possible choices
    image_list = [first_choice, second_choice, third_choice, fourth_choice]

    # Create a list containing the possible answers
    word_list = [pytesseract.image_to_string(image, lang = 'eng') for image in image_list]

    # Convert the problem to a string and split it, since we are
    # looking for the sysnonym of the first word in the sentence
    text_problem = pytesseract.image_to_string(problem, lang = 'eng')
    problem_list = text_problem.split()

    # Try to insert the fist word in the problem, the OCR might fail
    try:
        word_list.insert(0, problem_list[0])
    except:
        print('OCR could not read in problem')
        word_list.insert(0, 'None')
    
    print(f'The problem is: {word_list[0]} and the possible answers are {word_list[1:]}')
    return word_list
