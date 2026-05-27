#This is an app that send periodic notifications to the user. It is a simple app that can be used to remind the user of something important.

#You can use this app to remind yourself to drink water, take a break, meditate, exercise, turn off your screen, scroll through Instagram, or stand up. You can customize the notifications in the code by changing the title and message for each notification.

import time
from plyer import notification  

notifications = {
    "drink_water": {
        "title": "Drink Water",
        "message": "Don't forget to drink water!"
    },
    "take_break": {
        "title": "Take a Break",
        "message": "It's time to take a break and stretch!"
    },
    "meditate": {
        "title": "Meditate",
        "message": "Take a moment to meditate and relax!"
    },
    "exercise": {
        "title": "Exercise",
        "message": "Time for some exercise to stay healthy!"
    },
    "turn-off-screen": {
        "title": "Turn Off Screen",
        "message": "It's time to turn off your screen and rest your eyes!"
    },
    "Scroll-Instagram": {
        "title": "Scroll Instagram",
        "message": "Take a moment to scroll through Instagram and relax!"
    },
    "stand-up": {
        "title": "Stand Up",
        "message": "It's time to stand up and move around!"
    }
}

if __name__ == "__main__":
    print("Welcome to the Pythonic Notification App")
    print("This app will send you periodic notifications to remind you of important things!")
    print("You can customize the notifications in the code!")
    
    while True:
        for key, value in notifications.items():
            notification.notify(
                title=value["title"],
                message=value["message"],
                timeout=10
            )
            time.sleep(3600)  # Wait for 1 hour before sending the next notification     