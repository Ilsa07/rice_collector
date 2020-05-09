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
    # Calculate the time difference between the two objects
    time_diff = (current_time-datetime_object)
    # Get the number of secondsd passed
    duration_in_s = time_diff.total_seconds()  
    
    # One hour in seconds
    hour_in_sec = 60*60
    
    # Check if an hour has passed
    if(duration_in_s>hour_in_sec):    
        return True
    else:
        return False


def take_screenshot(save_image = True, return_image = False):
    time.sleep(5)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    date = str(datetime.now())[:10] + '_' +str(datetime.now())[11:16]

    image_name = 'current_progress_'+date
    image_name = image_name.replace(" ", "_")
    image_name = image_name.replace(":", "_")
    image_name = image_name.replace("-", "_")
    image_name = image_name.replace(".", "_")
    
    if(save_image):
        cv2.imwrite('hour_logs/'+image_name+'.jpg', image)
        print('Screenshot taken!')
    
    if(return_image):
        return image


def click_on_screen(coordinates_touple):
    # Move to the location
    pyautogui.moveTo(coordinates_touple[0], coordinates_touple[1], duration = 1)
    time.sleep(1)

    # Click on the specified location
    pyautogui.click(coordinates_touple[0], coordinates_touple[1])


def is_synonym(searched_word, input_word):
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response = requests.get("https://api.datamuse.com/words?ml="+searched_word)
    # Print the the response in JSON format
    #print(response.json())
    
    # Put it in a list
    data_list = response.json()

    # This list will only contain the synonyms
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
    problem = image[400:500, 1150:1750]          # Good
    #cv2.imwrite('hour_logs/problem.jpg', problem)

    first_choice = image[520:600, 1150:1750]     # Good
    #cv2.imwrite('hour_logs/first_choice.jpg', first_choice)
    
    second_choice = image[640:720, 1150:1750]    # Good
    #cv2.imwrite('hour_logs/second_choice.jpg', second_choice)

    third_choice = image[760:840, 1150:1750]     # Good
    #cv2.imwrite('hour_logs/third_choice.jpg', third_choice)

    fourth_choice = image[870:950, 1150:1750]    # Good
    #cv2.imwrite('hour_logs/fourth_choice.jpg', fourth_choice)
    
    # make a list out of it
    image_list = [first_choice, second_choice, third_choice, fourth_choice]
    word_list = []

    # The problem has to be read in first, since the sentence must be split
    # in order to get the problem word
    text_problem = pytesseract.image_to_string(problem, lang='eng')
    text_problem = text_problem.split()

    try:
        word_list.append(text_problem[0])
    except:
        print('OCR could not read in problem')
        word_list.append('None')
    
    for image in image_list:
        text = pytesseract.image_to_string(image, lang='eng')
        word_list.append(text)
    
    
    print(word_list)
    return word_list
#time.sleep(3)
#get_choices(take_screenshot(True))