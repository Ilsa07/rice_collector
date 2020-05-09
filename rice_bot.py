# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:52:15 2020

@author: malat
"""
import pyautogui 
import time
import random
from datetime import datetime
from supporting_functions import hour_passed, take_screenshot, click_on_screen, is_synonym, get_choices

# If you move the mouse to the top left of your screen it will abort the program
pyautogui.FAILSAFE = True





# Button positions:
first_choice = (991, 372)
second_choice =(981, 429)
third_choice = (984, 515)
fourth_choice = (988, 588)
refresh_button_position = (107, 59)


time.sleep(5)

take_screenshot()
number_of_hours_to_run = 5
start_time = datetime.now()

while(number_of_hours_to_run>0):
    #Check if an hour has passed
    if(hour_passed(start_time)):
        # If an hour has passed take a screenshot and reduce the iterator
        take_screenshot()
        number_of_hours_to_run -=1
        
        # Also reset the timer
        start_time = datetime.now()
        
        # Also, refresh the page
        time.sleep(2)
        click_on_screen(refresh_button_position)
        time.sleep(8)
        print('An hour has passed!')
        
    else:
        # Screenshot, but dont save image
        screenshot = take_screenshot(False, True)
        
        # get list of words
        choices = get_choices(screenshot)
        
        # Check which option matches
        if(is_synonym(choices[0], choices[1])):
            print('First choice')
            click_on_screen(first_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            
            time.sleep(random.uniform(1.8, 2.2))
        elif(is_synonym(choices[0], choices[2])):
            print('Second choice')
            click_on_screen(second_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            
            time.sleep(random.uniform(1.8, 2.2))
        elif(is_synonym(choices[0], choices[3])):
            print('Third choice')
            click_on_screen(third_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            
            time.sleep(random.uniform(1.8, 2.2))
        elif(is_synonym(choices[0], choices[4])):
            print('Fourth choice')
            click_on_screen(fourth_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            
            time.sleep(random.uniform(1.8, 2.2))
        else:
            print('Could not find a match..')
            click_on_screen(third_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            
            time.sleep(random.uniform(1.8, 2.2))

        
take_screenshot()
