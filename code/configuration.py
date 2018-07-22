import json, os
import campDeets

def configReader():
    """Reads a pre-defined config file and passes its data to the main programme"""
    # check if config file exists
    if os.path.isfile('config/config.json'):
        try:
            with open('config/config.json') as infile:
                c = json.load(infile)
        
            # extract data
            config = c['config']
            
            group = config['group']
            logo = config['logo']
            established = config['established']
            charity = config['charity']
            rnNumber = config['rnNumber']
            district = config['district']
            section = config['section']

            myGroup = campDeets.groupDeets(group, logo, established, charity, rnNumber, district, section)
            return myGroup
        
        except:
            print("Failed to read config file", end="\n\n")
            new = input("Would you like to save Scout Group details to a new file (y/n)? ")
    
    else:
        print("Failed to find config file", end="\n\n")
        new = input("Would you like to save Scout Group details to file (y/n)? ")

    # if user wants to write new config
    if new == 'y':
        myGroup = campDeets.getGroup()
        configWriter(myGroup)
    elif new != 'y':
        temp = input("Would you like to enter Scout Group details, but not store them (y/n)? ")
        if temp == 'y':
            myGroup = campDeets.getGroup()
            return myGroup
        else:
            quit()


def configWriter(myGroup):
    """Writes a config file with group data to ease use for subsequent camps"""
    print("Setting up a new configuration...")
    config = {}

    try:
        # build configuration file in correct format
        print("Building configuration file...")
        cDict = {}
        cDict['group'] = myGroup.group
        cDict['logo'] = myGroup.logo
        cDict['established'] = myGroup.established
        cDict['charity'] = myGroup.charity
        cDict['rnNumber'] = myGroup.rnNumber
        cDict['district'] = myGroup.district
        cDict['section'] = myGroup.section

        config['config'] = cDict

        # write configuration to JSON file
        print("Saving configuration file...")
        with open('config/config.json', 'w') as outfile:
            json.dump(config, outfile)
        print("Configuration saved successfully!", end="\n\n")
    
    except:
        print("Failed to write Scout Group configuration to file")

