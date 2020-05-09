# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:49:03 2020

@author: malat
"""
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
    
    image_name = 'current_progress_'+str(datetime.now())
    image_name = image_name.replace(" ", "")
    image_name = image_name.replace(":", "_")
    image_name = image_name.replace("-", "_")
    image_name = image_name.replace(".", "_")
    
    if(save_image):
        cv2.imwrite('hour_logs/'+image_name+'.jpg', image)
        print('Screenshot taken!')
        
    time.sleep(1)
    
    if(return_image):
        return image


def click_on_screen(coordinates_touple):
    # Record the initial mouse position
    current_mouse_position = pyautogui.position()
    
    # Off course stop at the middle of the movement, randomness implemented
    off_course_stop = [((current+moveTo)/2) * random.uniform(0.7, 1.4) for current, moveTo in zip(current_mouse_position, coordinates_touple)]
    pyautogui.moveTo(off_course_stop[0], off_course_stop[1], duration = random.uniform(0.8, 1.2))
    time.sleep(random.uniform(0.1, 0.4))

    # Random overshoot/undershoot based on final location
    overshoot_coordinates = [coordinate + random.uniform(-40, 40) for coordinate in coordinates_touple]
    pyautogui.moveTo(overshoot_coordinates[0], overshoot_coordinates[1], duration = random.uniform(0.5, 0.9))
    time.sleep(random.uniform(0.3, 0.6))

    # Correction to exact position
    pyautogui.moveTo(coordinates_touple[0], coordinates_touple[1], duration = random.uniform(0.2, 0.6))
    time.sleep(random.uniform(0.1, 0.4))

    # Click on final location
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
    problem = image[250:320, 780:1120]          # Good
    first_choice = image[350:400, 780:1120]     # Good
    second_choice = image[420:470, 780:1120]    # Good
    third_choice = image[490:545, 780:1120]     # Good
    fourth_choice = image[565:610, 780:1120]    # Good
    
    # make a list out of it
    image_list = [first_choice, second_choice, third_choice, fourth_choice]
    word_list = []
    text_problem = pytesseract.image_to_string(problem, lang='eng')
    text_problem = text_problem.split()
    word_list.append(text_problem[0])
    
    for image in image_list:
        text = pytesseract.image_to_string(image, lang='eng')
        word_list.append(text)
    
    
    print(word_list)
    return word_list
#time.sleep(3)
#get_choices(take_screenshot(True))