import pyautogui 
import time
import random
import cv2
import numpy as np
from datetime import datetime
import requests
import pytesseract

# On windows you have to install Tesseract and provide a PATH to it
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\malat\tesseract.exe'





def hour_passed(datetime_object):
    # Get the current time
    current_time = datetime.now()

    # Calculate the time difference between the two datetime objects
    time_diff = (current_time-datetime_object)

    # Calculate the number of secondsd passed
    duration_in_s = time_diff.total_seconds()  
    
    # One hour in seconds
    hour_in_sec = 60*60
    
    # Check if an hour has passed
    if(duration_in_s>hour_in_sec):    
        return True
    else:
        return False


def take_screenshot(save_image = True, return_image = False):
    # Wait before screenshot so the page can show the new problem
    time.sleep(5)
    image = pyautogui.screenshot()

    # Convert the image to an OpenCV image object
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Format the name of the picture
    date = str(datetime.now())[:10] + '_' +str(datetime.now())[11:16]
    image_name = 'current_progress_'+date
    image_name = image_name.replace(" ", "_")
    image_name = image_name.replace(":", "_")
    image_name = image_name.replace("-", "_")
    image_name = image_name.replace(".", "_")
    
    if(save_image):
        # Save the image in the hour_logs folder
        cv2.imwrite('hour_logs/'+image_name+'.jpg', image)
        print('Screenshot taken!')
    
    if(return_image):
        # Return the image object
        return image


def click_on_screen(coordinates_touple):
    # Move to the location in 1 second
    pyautogui.moveTo(coordinates_touple[0], coordinates_touple[1], duration = 1)
    
    # Click on the specified location
    pyautogui.click(coordinates_touple[0], coordinates_touple[1])


def is_synonym(searched_word, input_word):
    # Send a get request to datamouse and save the response
    response = requests.get("https://api.datamuse.com/words?ml="+searched_word)

    # Print the the response in JSON format
    #print(response.json())
    
    # Save the response in a list
    data_list = response.json()

    # Store the synonyms in a list
    new_list = []
    for element in data_list:
        new_list.append(element['word'])
    
    # Check if the input word is a sysnonym of the searched word 
    if(input_word in new_list):
        print(f'The sysnonym was: {input_word}')
        return True
    else:
        return False
#is_synonym('vanish', 'disappear')


def get_choices(image):
    # Create sub images of the screenshot containing 
    # the problem and the four choices

    problem = image[400:500, 1150:1750]
    #cv2.imwrite('hour_logs/problem.jpg', problem)

    first_choice = image[520:600, 1150:1750]
    #cv2.imwrite('hour_logs/first_choice.jpg', first_choice)
    
    second_choice = image[640:720, 1150:1750]
    #cv2.imwrite('hour_logs/second_choice.jpg', second_choice)

    third_choice = image[760:840, 1150:1750]
    #cv2.imwrite('hour_logs/third_choice.jpg', third_choice)

    fourth_choice = image[870:950, 1150:1750]
    #cv2.imwrite('hour_logs/fourth_choice.jpg', fourth_choice)
    

    # Create a list of images of the possible choices
    image_list = [first_choice, second_choice, third_choice, fourth_choice]

    # Create an empty list to which the OCR will append the words
    # in the images
    word_list = []

    # The problem has to be read in first, since the sentence must be split
    # in order to get the problem word
    text_problem = pytesseract.image_to_string(problem, lang='eng')
    text_problem = text_problem.split()

    # Try to append the fist word in the problem, the OCR might fail
    try:
        word_list.append(text_problem[0])
    except:
        print('OCR could not read in problem')
        word_list.append('None')
    
    # Append the choices the the word list
    for image in image_list:
        text = pytesseract.image_to_string(image, lang='eng')
        word_list.append(text)
    
    
    print(word_list)
    return word_list