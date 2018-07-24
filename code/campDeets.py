import datetime

class campDeets:
    """Holds the camp details, calculating a range of data from the initialisation parameters"""
    def __init__(self, camp, location, startDate, endDate, catering, sharps, waterActivities):
        # camp basics
        self.camp = camp.capitalize()
        self.location = location

        # conver camp dates to datetime
        self.startDate = datetime.datetime.strptime(startDate, "%d-%m-%Y")
        self.endDate = datetime.datetime.strptime(endDate, "%d-%m-%Y")

        # apply date functions to get extra data
        self.campYear = str(self.startDate.year)
        self.dateRange = self.date_worder()
        self.nightsAway = self.date_diff()
        self.daysCamping = self.days_on_camp()

        # key activities
        self.catering = catering
        self.sharps = sharps
        self.waterActivities = waterActivities


    def __str__(self):
        return self.camp + " at " + self.location + " from " + self.dateRange


    def date_diff(self):
        """Calculate the number of night's away from the start and end date"""
        return abs((self.endDate - self.startDate).days)


    def day_suffix(self, day):
        """Work out day suffix"""
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return suffix


    def date_worder(self):
        """Build natural language date range"""
        # extract date parts
        startDay = self.startDate.day
        endDay = self.endDate.day
        endMonth = self.endDate.strftime("%B")
        endYear = self.endDate.year

        # work out day suffix
        startSuffix = self.day_suffix(startDay)
        endSuffix = self.day_suffix(endDay)

        dateRange = str(startDay) + startSuffix + " to " + str(endDay) + endSuffix + ' ' + endMonth + ' ' + str(endYear)
        return dateRange


    def days_on_camp(self):
        """Get a list of all the days on camp"""
        date = self.startDate
        campDays = []
        for i in range(self.nightsAway + 1):
            i += 1
            day = date.strftime("%A")
            campDays.append(day)
            if date == self.endDate:
                break
            else:
                date += datetime.timedelta(days=1)
        return campDays


class campLeader():
    """Holds the camp leader's details"""
    def __init__(self, name, position): # memberNo, telephone, email
        # leader identifiers
        self.name = name
        self.position = position
        #self.memberNo = str(memberNo)

        # contact details
        #self.telephone = str(telephone)
        #self.email = email
    
    def __str__(self):
        return "Camp leader: " + self.name


class groupDeets():
    """Holds the Scout Group and section details"""
    def __init__(self, group, logo, established, charity, rnNumber, district, section):
        # group details
        self.group = group
        self.logo = logo
        self.established = established
        self.charity = charity
        self.rnNumber = rnNumber

        # district details
        self.district = district
        
        # section details
        self.section = section
    
    def __str__(self):
        if self.rnNumber == 'na':
            rn = ''
        else:
            rn = "\nAdmiralty recognised group number: " + str(self.rnNumber)
        return self.group \
            + "\n\nEstablished in: " + str(self.established) \
            + "\nRegistered charity number: " + str(self.charity) \
            + rn \
            + "\nSection: " + self.section + "\n"


def get_camp():
    """Capture camp details from the user"""
    print("Please provide your camp details", end="\n\n")

    # get camp basics
    camp = input("What's the camp called (e.g. summer camp)? ")
    location = input("Where is the camp? ")

    # get camp dates
    startDate = input("What's the start date (in format dd-mm-yyyy)? ")
    endDate = input("What's the end date (in format dd-mm-yyyy)? ")

    # get key activities
    food = input("Will you be catering (y/n)? ")
    if food == 'y':
        catering = True
    else:
        catering = False
    axe = input("Will you be using knives, axes and saws (y/n)? ")
    if axe == 'y':
        sharps = True
    else:
        sharps = False
    water = input("Will there be water activities (y/n)? ")
    if water == 'y':
        waterActivities = True
    else:
        waterActivities = False

    # create camp details object
    print("")
    event = campDeets(camp, location, startDate, endDate, catering, sharps, waterActivities)
    return event


def get_leader():
    """Capture camp leader details from the user"""
    print("Please provide your camp leader details", end="\n\n")

    # get leader identfiers
    name = input("What's the camp leader's name? ")
    position = input("What's the camp leader's position (e.g. SL, ASL)? ")
    #memberNo = input("What's the camp leader's Scout membership number? ")

    # get leader contact details
    #telephone = input("What's the camp leader's telephone number? ")
    #email = input("What's the camp leader's email address? ")

    # create leader object
    print("")
    leader = campLeader(name, position) # memberNo, telephone, email
    return leader


def get_group():
    """Capture group details from the user"""
    print("Please provide your group details", end="\n\n")

    # get group details
    group = input("What's the name of your Scout Group? ")
    established = input("When was the group established? ")
    charity = input("What's the group's charity number? ")
    rnNumber = input("What's the group's RN recognition number? (type na if not applicable) ")
    logo = input("What's the file path to the group logo? (e.g. config/logo.png) ")

    # get district details
    district = input("What's the name of your district? ")

    # get section details
    section = input("What's your section? ")

    # create group object for use in rest of programme
    print("")
    myGroup = groupDeets(group, logo, established, charity, rnNumber, district, section)
    return myGroup

