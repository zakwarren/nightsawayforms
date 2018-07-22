import os, platform, argparse
import campDeets, configuration, defaults, equipment, header, kitList, menu, programme, riskAssessment

def setUp():
    """Check local environment and set up as necessary"""
    try:
        # check if config directory exists and, if not, create it
        directory = "config"
        if not os.path.exists(directory):
            os.makedirs(directory)

    except:
        print("Failed to create config directory")
        quit()
    
    # check if data files are present and, if not, write defaults
    try:
        if not os.path.isfile('config/equipment.json'):
            defaults.defaultEquip()
        if not os.path.isfile('config/kitList.json'):
            defaults.defaultKit()
        if not os.path.isfile('config/risks.json'):
            defaults.defaultRisk()
    
    except:
        print("Failed to search config directory")


def campDirectory():
    """Check directory for camp forms and create as necessary"""
    directory = input("What directory do you want to save the camp paperwork in? (Leave blank for this directory) ")
    try:
        # if nothing entered, set as blank string for this directory
        if not directory:
            directory = ""

        # else check if camp directory exists and, if not, create it
        elif not os.path.exists(directory):
            os.makedirs(directory)
        
        # set up path
        if directory != "" and not directory.endswith("/"):
            directory = directory + "/"

        return directory
    
    except:
        print("Failed to create directory:", directory)


def blankDoc(directory, myGroup, event):
    """Produces a blank document using the standard header for the camp"""
    print("Generating blank document...")
    doc, docName = header.wordHeading(myGroup, event)
    
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
    setUp()

    # get required data
    if config == "ignore":
        myGroup = campDeets.getGroup()
    else:
        myGroup = configuration.configReader()
    event = campDeets.getCamp()
    leader = campDeets.getLeader()
    print("")
    directory = campDirectory()
    print("")

    # write programme
    doc, docName = header.wordHeading(myGroup, event)
    programme.programme(doc, docName, directory, event)
    print("")

    # write kit list
    doc, docName = header.wordHeading(myGroup, event)
    kitList.kitList(doc, docName, directory, event)
    print("")

    # write group equipment list
    wb, ws, bookName = header.excelHeading(myGroup, event)
    equipment.equipment(wb, ws, bookName, directory, leader, myGroup, event)
    print("")

    # write menu, if applicable
    if event.catering:
        doc, docName = header.wordHeading(myGroup, event)
        menu.menu(doc, docName, directory, event)
        print("")
    
    # write risk assessment
    doc, docName = header.wordHeading(myGroup, event)
    riskAssessment.riskAssessment(doc, docName, directory, event)
    print("")

    print("-" * 40)
    print("Don't forget to fill in and submit a Nights Away Notification (NAN) form!")
    print("Don't forget to collect health and emergency contact details!")
    print("-" * 40, end="\n\n")
    print("Have a good camp!")



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
        myGroup = campDeets.getGroup()
        configuration.configWriter(myGroup)
    
    # ignore any existing Scout Group configurations
    elif args.ignore:
        ops("ignore")
    
    # restore default settings files
    elif args.default:
        defaults.restoreDefaults()
    
    # generate a blank document with a camp header
    elif args.blank:
        # get required data
        if args.ignore:
            myGroup = campDeets.getGroup()
        else:
            myGroup = configuration.configReader()
        event = campDeets.getCamp()
        print("")
        directory = campDirectory()
        print("")
        # produce blank document
        blankDoc(directory, myGroup, event)
    
    # run normal nights away form generator
    else:
        ops("include")


if __name__ == '__main__':
    main()