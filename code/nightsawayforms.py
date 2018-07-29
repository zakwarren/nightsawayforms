import os
import platform
import argparse
import urllib.request

# import nightsawayforms code
import campdeets
import configuration
import defaults
import equipment
import header
import health
import kitlist
import menu
import programme
import riskassessment
import nanform


def set_up():
    """Check local environment and set up as necessary"""
    # check if config directory exists and, if not, create it
    try:
        directory = "config"
        if not os.path.exists(directory):
            os.makedirs(directory)

    except:
        print("Failed to create config directory")
        quit()
    
    # check if data files are present and, if not, write defaults
    try:
        if not os.path.isfile('config/equipment.json'):
            defaults.default_equip()
        if not os.path.isfile('config/kitList.json'):
            defaults.default_kit()
        if not os.path.isfile('config/risks.json'):
            defaults.default_risk()
    
    except:
        print("Failed to search config directory")
    
    # check if NAN form template exists and, if not, create it
    try:
        if not os.path.isfile('config/nanFormTemplate.doc'):
            url = r"https://members.scouts.org.uk/documents/activities/Form%20NAN_Feb%202015%20Fix.doc"

            # download the NAN form and save it to the config directory
            with urllib.request.urlopen(url) as response, open("config/nanFormTemplate.doc", 'wb') as outFile:
                data = response.read()
                outFile.write(data)
            
    except:
        print("Failed to download NAN form template")


def camp_directory():
    """Check directory for camp forms and create as necessary"""
    directory = input("What directory do you want to save the camp paperwork in? (Leave blank for this directory) ")
    try:
        # if nothing entered, set as blank string for this directory
        if not directory:
            directory = ""

        # else check if camp directory exists and, if not, create it
        elif not os.path.exists(directory):
            os.makedirs(directory)
        
        return os.path.join(directory, '')
    
    except:
        print("Failed to create directory:", directory)


def blank_doc(directory, myGroup, event):
    """Produces a blank document using the standard header for the camp"""
    print("Generating blank document...")
    doc, docName = header.word_heading(myGroup, event)
    
    # save document
    try:
        docName = 'Blank document' + docName
        print("Saving:", docName)
        doc.save(directory + docName)
    except:
        print("Failed to save " + docName)


def ops(config):
    """Runs the primary operations"""
    # check local set up
    set_up()

    # get required data
    if config == "ignore":
        myGroup = campdeets.get_group()
    else:
        myGroup = configuration.config_reader()
    event = campdeets.get_camp()
    leader = campdeets.get_leader()
    print("")
    directory = camp_directory()
    print("")

    # write programme
    doc, docName = header.word_heading(myGroup, event)
    programme.programme(doc, docName, directory, event)
    print("")

    # write kit list
    doc, docName = header.word_heading(myGroup, event)
    kitlist.kit_list(doc, docName, directory, event)
    print("")

    # write group equipment list
    wb, ws, bookName = header.excel_heading(myGroup, event)
    equipment.equipment(wb, ws, bookName, directory, leader, myGroup, event)
    print("")

    # write menu, if applicable
    if event.catering:
        doc, docName = header.word_heading(myGroup, event)
        menu.menu(doc, docName, directory, event)
        print("")
    
    # write risk assessment
    doc, docName = header.word_heading(myGroup, event)
    riskassessment.risk_assessment(doc, docName, directory, event)
    print("")

    # write health and emergency contact form if required
    hf = input("Do you want to create a health and emergency contact form (y/n)? ")
    if hf == 'y':
        doc, docName = header.word_heading(myGroup, event)
        health.health_and_emergency(doc, docName, directory, event)
    print("")

    # copy blank NAN form into the camp directory
    nanform.nan_form(directory, event)
    print("")

    print("-" * 40)
    print("Have a good camp!")
    print("-" * 40, end="\n\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="set up a new Scout Group configuration", action="store_true")
    parser.add_argument("-i", "--ignore", help="ignores existing configuration", action="store_true")
    parser.add_argument("-d", "--default", help="restore settings files to default", action="store_true")
    parser.add_argument("-b", "--blank", help="generate a blank document with a camp header", action="store_true")
    args = parser.parse_args()

    # clear the terminal and show welcome screen
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    print("-" * 40)
    print("The Nights Away Form Generator")
    print("-" * 40, end="\n\n")

    # set up a new Scout Group configuration
    if args.config:
        myGroup = campdeets.get_group()
        configuration.config_writer(myGroup)
    
    # ignore any existing Scout Group configurations
    elif args.ignore:
        ops("ignore")
    
    # restore default settings files
    elif args.default:
        defaults.restore_defaults()
    
    # generate a blank document with a camp header
    elif args.blank:
        # get required data
        if args.ignore:
            myGroup = campdeets.get_group()
        else:
            myGroup = configuration.config_reader()
        event = campdeets.get_camp()
        print("")
        directory = camp_directory()
        print("")
        # produce blank document
        blank_doc(directory, myGroup, event)
    
    # run normal nights away form generator
    else:
        ops("include")


if __name__ == '__main__':
    main()
