import shutil


def nan_form(directory, event):
    """Deploys a blank Nights Away Notification (NAN) form for the camp"""
    print("Copying blank NAN form to camp directory...")

    # copy template file from config to camp directory
    try:
        nan = 'NAN form - ' + event.camp + ' ' + event.campYear + '.doc'
        print("Copying:", nan)
        shutil.copyfile('config/nanFormTemplate.doc', directory + nan)
        print("")
    except:
        print("Failed to copy " + nan, end="\n\n")

    print("Don't forget to fill in and submit the Nights Away Notification (NAN) form!")
