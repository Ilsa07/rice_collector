import pyautogui 
import time
from datetime import datetime
from supporting_functions import hour_passed, take_screenshot, click_on_screen, is_synonym, get_choices
from global_variables import positions

# If you move the mouse to the top left of the screen it will abort the program
pyautogui.FAILSAFE = True





# Delay to switch to the browser and make it full size
time.sleep(5)

# Initial screenshot when the program starts
take_screenshot()

# Record the start time
start_time = datetime.now()

while(positions['num_of_hours_to_run'] > 0):

    #Check if an hour has passed
    if(hour_passed(start_time)):
        # If an hour has passed take a screenshot and reduce the iterator
        take_screenshot()
        positions['num_of_hours_to_run'] -= 1
        
        # Reset the start time
        start_time = datetime.now()
        
        # Refresh the page
        click_on_screen(positions['refresh_page'])
        time.sleep(8)
        print('An hour has passed!')
    
    else:
        # Screenshot without saving the image
        screenshot = take_screenshot(False, True)
        
        # Get list of words
        choices = get_choices(screenshot)
        
        # Check which option matches
        if(is_synonym(choices[0], choices[1])):
            click_on_screen(positions['first_choice'])

            # Move mouse out of the box for the next screenshot
            pyautogui.moveTo(positions['resting_position'][0], positions['resting_position'][1], 1)
            time.sleep(1)

        elif(is_synonym(choices[0], choices[2])):
            click_on_screen(positions['second_choice'])
            
            # Move mouse out of the box for the next screenshot
            pyautogui.moveTo(positions['resting_position'][0], positions['resting_position'][1], 1)
            time.sleep(1)

        elif(is_synonym(choices[0], choices[3])):
            click_on_screen(positions['third_choice'])
            
            # Move mouse out of the box for the next screenshot
            pyautogui.moveTo(positions['resting_position'][0], positions['resting_position'][1], 1)
            time.sleep(1)

        elif(is_synonym(choices[0], choices[4])):
            click_on_screen(positions['fourth_choice'])
            
            # Move mouse out of the box for the next screenshot
            pyautogui.moveTo(positions['resting_position'][0], positions['resting_position'][1], 1)
            time.sleep(1)
        
        else:
            # If no matches were found click on the third choice
            print('Could not find a match..')
            click_on_screen(positions['third_choice'])
            
            # Move mouse out of the box for the next screenshot
            pyautogui.moveTo(positions['resting_position'][0], positions['resting_position'][1], 1)
            time.sleep(1)

# Take a screenshot once the algorithm has finished  
take_screenshot()