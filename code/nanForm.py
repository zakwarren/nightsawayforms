import os
import shutil


def nan_form(directory, event):
    """Deploys a blank Nights Away Notification (NAN) form for the camp"""
    print("Copying blank NAN form to camp directory...")
    
    # copy template file from config to camp directory
    try:
        nan = 'NAN form - ' + event.camp + ' ' + event.campYear + '.doc'
        print("Copying:", nan)
        shutil.copyfile('config/nanFormTemplate.doc', directory + nan)
    except:
        print("Failed to copy " + nan)

    print("-" * 40)
    print("Don't forget to fill in and submit the Nights Away Notification (NAN) form!")
    print("-" * 40, end="\n\n")

