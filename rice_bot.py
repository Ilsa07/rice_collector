import pyautogui 
import time
from datetime import datetime
from supporting_functions import hour_passed, take_screenshot, click_on_screen, is_synonym, get_choices

# If you move the mouse to the top left of the screen it will abort the program
pyautogui.FAILSAFE = True





# Button positions:
first_choice = (730, 280)
second_choice =(730, 340)
third_choice = (730, 400)
fourth_choice = (730, 450)

refresh_button_position = (997, 17)

# Not used in Ganyolas
#out_of_boxes = (55,400)

# Delay to switch to the browser
# and make it full size
time.sleep(5)

# Initial screenshot when the program starts
take_screenshot()

# Define the number of hours you want
# the algorithm to run
number_of_hours_to_run = 1

# Record the start time
start_time = datetime.now()

while(number_of_hours_to_run>0):
    #Check if an hour has passed
    if(hour_passed(start_time)):
        # If an hour has passed take a screenshot and reduce the iterator
        take_screenshot()
        number_of_hours_to_run -=1
        
        # Reset the start time
        start_time = datetime.now()
        
        # Refresh the page
        click_on_screen(refresh_button_position)
        time.sleep(8)
        print('An hour has passed!')
        
    else:
        # Screenshot without saving the image
        screenshot = take_screenshot(False, True)
        
        # Get list of words
        choices = get_choices(screenshot)
        
        # Check which option matches
        if(is_synonym(choices[0], choices[1])):
            print('First choice')
            click_on_screen(first_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            time.sleep(1)

        elif(is_synonym(choices[0], choices[2])):
            print('Second choice')
            click_on_screen(second_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            time.sleep(1)

        elif(is_synonym(choices[0], choices[3])):
            print('Third choice')
            click_on_screen(third_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            time.sleep(1)

        elif(is_synonym(choices[0], choices[4])):
            print('Fourth choice')
            click_on_screen(fourth_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            time.sleep(1)
        
        else:
            # If no matches were found click
            # on the third choice
            print('Could not find a match..')
            click_on_screen(third_choice)
            
            # Move mouse out of the box
            pyautogui.moveTo(100, 200, 1)
            time.sleep(1)

# Take a screenshot once the algorithm
# has finished        
take_screenshot()