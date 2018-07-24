import os

def restore_defaults():
    """Restore default setting files"""
    try:
        # check if config directory exists and, if not, create it
        directory = "config"
        if not os.path.exists(directory):
            os.makedirs(directory)

    except:
        print("Failed to create config directory")
        quit()
    
    # write new default settings files
    default_equip()
    default_kit()
    default_risk()


def default_equip():
    """Write default equipment to disk"""
    equip = """{
    "equipment": {
        "sleeping": [
            "Family tents",
            "Patrol tents",
            "Hike tents"
        ],
        "catering": [
            "Dining shelter",
            "Dining shelter side poles",
            "Gas stove - double",
            "Gas regulator",
            "Gas splitter",
            "Trangias",
            "Meths",
            "Altar fires",
            "Altar fire stands",
            "Hot plates",
            "Grills",
            "Fire buckets",
            "Dutch ovens",
            "Dutch oven tripods",
            "Water containers - aqua roll",
            "Aqua roll handle",
            "Water containers - square",
            "Drainers",
            "Bowls - washing up",
            "Burco",
            "Kitchen stands",
            "Merlins",
            "Cooking pot - large with lid",
            "Collander - large",
            "Tray - deep with lid",
            "Tray - carrying",
            "Crate",
            "Kettle - large",
            "Teapot - large",
            "Cool boxes",
            "Matches",
            "Lighters",
            "Fire steels",
            "Patrol boxes"
        ],
        "hygiene": [
            "Water containers - latrine",
            "Bowls - latrine",
            "Bowls - washing",
            "Lat screen",
            "Lat screen poles",
            "Latrine tent",
            "Elsan"
        ],
        "central": [
            "Marquee (30ft)",
            "W tents",
            "Benches",
            "Tables",
            "Gas bottle",
            "Ground sheets",
            "Spare pegs",
            "Mast and ensign",
            "First aid kit - main",
            "First aid kit - exped",
            "Rope",
            "Cord",
            "Maps",
            "Compasses",
            "Leader patrol boxes"
        ],
        "light": [
            "Tilley lamps",
            "Tilley starters",
            "Tilley mantles",
            "Gas light - large"
        ],
        "sharps": [
            "Axe - hand",
            "Axe - felling",
            "Billhook",
            "Saw - bow",
            "Saw - folding",
            "Knife"
        ],
        "tools": [
            "Shovel",
            "Spade",
            "Fork",
            "Pick axe",
            "Trenching tool",
            "Sledgehammer",
            "Mallet - marquee",
            "Mallet - standard",
            "Mallet - rubber"
        ],
        "water activities": [
            "Buoyancy aids",
            "Dry bags",
            "Kayaks",
            "Kayak paddles",
            "Spray decks",
            "Canoes",
            "Canoe paddles",
            "Double kayaks",
            "Throw lines",
            "Tow lines",
            "Gig",
            "Bag of gig crutches, bungs, bailers",
            "Coypus",
            "Bags of coypu crutches, bungs, bailers",
            "Picos",
            "Pico masts",
            "Pico rudders and tillers",
            "Pico main sails",
            "Pico jibs",
            "Wayfarers",
            "Wayfarer sails",
            "Drascombe",
            "Jaffa",
            "Jaffa engine",
            "RIB",
            "Fuel",
            "Flares",
            "Charts"
        ]
    }
  }"""
    try:
        with open('config/equipment.json', 'w') as outfile:
            outfile.write(equip)
    except:
        print("Failed to write default equipment data to config directory")


def default_kit():
    """Write default kit to list"""
    kit = """{
    "kit": {
        "bags": [
            "Rucksack or holdall to pack kit",
            "Bin bags / dry bags (to line pack with to keep kit dry and dirty clothes separate)"
        ],
        "clothing": [
            "Long sleeved tops and/or T-shirts",
            "Trousers (avoid jeans)",
            "Warm tops (jumpers/sweatshirts/fleeces)",
            "Underwear",
            "Socks (including thick pairs)",
            "Warm sleeping clothes (pyjamas/tracksuit)",
            "Sunhat and warm hat (also good for keeping warm in bed)",
            "Waterproof coat and trousers",
            "Footwear (walking boots or stout shoes)"
        ],
        "water activities": [
            "Kit for going afloat (non-cotton top/rash vest, shorts, old trainers/wet shoes, etc.)"
        ],
        "uniform": [
            "Uniform (excluding hat)"
        ],
        "sleeping": [
            "Sleeping bag (3 seasons or two sleeping bags, one inside the other)",
            "Blanket",
            "Roll mat (no air beds as, when inflated, they take up too much room in the tent)",
            "Pillow (or just bring an empty pillowcase and stuff some dry clothes in it overnight)"
        ],
        "hygiene": [
            "Wash kit (containing flannel, toothbrush, toothpaste, etc.)",
            "Towel",
            "Sun cream",
            "Insect repellent",
            "Handkerchiefs/tissues",
            "Personal medication (must be handed in at the start of camp)"
        ],
        "catering": [
            "Water bottle",
            "Mug (with handle and not breakable)"
        ],
        "accessories": [
            "Wind up torch or torch / head torch and spare batteries",
            "Pair of heavy-duty gardening gloves (for working with cooking fires and fire wood)",
            "Penknife (not to be used until passing the knife and axe test)",
            "Notepad and pencil"
        ],
        "extras": [
            "Cake in a container (labelled with your Scout’s name if you want the container back)"
        ],
        "exclude": [
            "mobile phones",
            "music players",
            "games players"
        ],
        "web": [
            "https://members.scouts.org.uk/nightsawayresources"
        ]
    }
  }"""
    try:
        with open('config/kitList.json', 'w') as outfile:
            outfile.write(kit)
    except:
        print("Failed to write default kit data to config directory")


def default_risk():
    """Write default risk assessment to disk"""
    risk = r"""{
    "risks": {
        "health": {
            "hygiene": {
                "mitigation": "Health and safety briefing on importance of cleanliness, its consequences and what to do if something happens. Areas to cover:\nToilets\nCooking and Dining\nWashing and cleaning teeth\nSite inspection and reinforce message",
                "contingency": "If an outbreak occurs assess individual and group situation and act based on assessment from isolation, individual returning home to abandoning camp."
            },
            "allergies and intolerances": {
                "mitigation": "Seek information from the health & permission form and plan accordingly, including meal ingredient planning",
                "contingency": "Assess the situation and seek medical help if appropriate. Reassess menus etc. that caused the problem"
            },
            "food poisoning": {
                "mitigation": "Perishables to be stored in cool box or food purchased immediately prior to use.\nFood stuffs to be securely stored to prevent insect and animal infestation.\nAppropriate facilities for disposal of waste to be established.\nEnsure adequate clean drinking water supply.\nEnsure food is cooked thoroughly.\nEnsure clean equipment, facilities & hand washing.\nEnsure food is within date",
                "contingency": "All involved to ensure food is properly stored, prepared and cooked\nFresh food to be purchased when necessary by appropriate adults\nAssess situation and use of first aid, NHS services as required"
            },
            "first response and prescription medication": {
                "mitigation": "Adequate first aid supplies should be available centrally. First aid kits to be taken on trips away from the main site.\nMedication should be handed over to the leadership team in a labelled container with name, dose and timings.\nEnsure first aid box is fully equipped prior to departure and seek consent for administration of basic first aid.\nComplete accident book in the event of injury or accident occurring\nNearest hospital is: [XXX]",
                "contingency": "Assess situation and use of first aid, NHS services as required"
            },
            "hyperthermia": {
                "mitigation": "Use of hats and natural shaded areas in strong sunlight.\nLong sleeves, long trousers and sun hats or shelter may be appropriate in the strongest sunlight.\nHigh factor sun block to be applied to exposed skin which cannot be covered.\nPlenty of cool drinks to be available in hot weather.\n",
                "contingency": "All adults are to ensure that both sun cream and drinks are readily available\nCamp Leader to ensure that appropriate kit list is issued prior to camp"
            },
            "hypothermia": {
                "mitigation": "Appropriate wet and cold weather clothing to be provided and worn as necessary\nWarm drinks and meals to be available in cold weather.",
                "contingency": "All adults to keep a watch for the signs of hypothermia\nCamp Leader to ensure that appropriate kit list is issued prior to camp"
            }
        },
        "environmental": {
            "trip hazards": {
                "mitigation": "Include as part of the health and safety briefing to raise awareness and confirm that there is to be no running around the tents. Ongoing supervision by adults and more experienced young people.\nUse of sturdy boots or shoes when going on hikes.",
                "contingency": "Assess situation and use of first aid, NHS services as required."
            },
            "manual handling": {
                "mitigation": "Remind everyone to work together to lift heavy objects and to practice good manual handling techniques (bend knees and keep a straight back). Adults available to help where needed. Lead by example. Ongoing supervision by adults and more experienced young people.",
                "contingency": "Assess situation and use of first aid, NHS services as required."
            },
            "adverse weather": {
                "mitigation": "Central shelter for cooking and activities\nSite inspection to ensure tents are pitched correctly",
                "contingency": "All leaders to ensure tents are pitched correctly\nCall off camp if necessary"
            },
            "members of the public": {
                "mitigation": "Leaders to know where young people are and young people to know where leaders are\nSupervision by adults if required\nHighlight the importance of sticking together",
                "contingency": ""
            }
        },
        "catering": {
            "fires": {
                "mitigation": "Health and safety briefing to confirm how we will be using gas and the safety precautions and use of fire buckets\nInitial patrol cooking will be in the central area with greater adult supervision\nInspection to include inspection of cooking shelter and preparation and to reinforce message\nHealth and safety briefing about fires and use of gloves and fire buckets on days when using fires\nOngoing supervision by SPL/PLs/APLs, Young Leaders and Leaders",
                "contingency": "Assess situation and use of fire buckets, first aid, NHS/emergency services as required."
            }
        },
        "sharps": {
            "knife, axe and saw": {
                "mitigation": "Health and safety briefing on first day of using these tools to confirm how we will be using knife and axe and safety precautions:\nSafe areas\nNot to use until trained\nOn camp training and assessment\nMark out chopping and sawing areas\nSite inspection to include inspection of knife and axe area and preparation and to reinforce message\nOngoing supervision by more experience young people, young leaders and leaders",
                "contingency": "Assess situation and use of first aid, NHS services as required."
            }
        },
        "land activities": {
            "camp gadgets and pioneering": {
                "mitigation": "Leaders, young leaders and more experienced young people to monitor young people. Experienced leaders should check all knots and lashings before any large structures are raised and/or climbed upon.",
                "contingency": "Assess situation and use of first aid, NHS services as required."
            }
        },
        "water activities": {
            "water activities": {
                "mitigation": "Follow the group generic and activity specific risk assessments\nSite specific mitigations include:\n[XXX]",
                "contingency": "Assess situation and use of first aid, NHS/emergency services as required."
            },
            "night activities on the water": {
                "mitigation": "Brief participants on signals and what they mean (recommended one whistle blast for stop and three for return to base)\nMaintain suitable safety cover with supervising leaders on the banks and afloat\nEnsure all young people have glow sticks attached to their buoyancy aids to aid in counting and locating individuals\nAll boats to have suitable lighting – a head torch per boat is recommended",
                "contingency": "Leaders competent in the water activities to be safety cover on the water\nAssess situation and use of first aid, NHS/emergency services as required"
            }
        },
        "expeditions": {
            "patrol leader expedition": {
                "mitigation": "Participants to be briefed beforehand on route, camping arrangements, cooking using Trangias, expected behaviour, etc.\nParticipants observed and assessed in preceding days to ensure they are competent and safe enough to go unsupervised (otherwise decide whether to send adults or cancel activity)\nAt least one phone to go with the group with leader contact details\nLeaders to check up with the group on arrival and before departure\nEnsure relevant permits and nights away passport are issued as necessary",
                "contingency": "Leaders available to pick up young people and return them to base camp by car or boat as necessary"
            }
        }
    }
  }"""
    try:
        with open('config/risks.json', 'w') as outfile:
            outfile.write(risk)
    except:
        print("Failed to write default risk assessment data to config directory")

