#Nights Away Forms Generator

Welcome to the user guide for the Nights Away Forms Generator! This 
was designed and developed by Scout Leaders for Scout Leaders (and 
all other leaders in Scouting) who want a quick and easy way to 
manage all the paperwork that comes with running a nights away event. 

The Nights Away Forms Generator (or just nightsawayforms) takes all 
the boring, repetitive tasks and automates them for you. It asks a set 
of simple questions and uses your answers to fill in the details. 

Some leaders like to use this app after they've had their planning 
meetings with their leader team and have all the answers. Others like 
to use it as a prompt during those meetings. Whichever works for you, 
use nightsawayforms to take the pain away and let you focus on the fun. 

##Getting started

Run nightsawayforms to begin. This will open a clear terminal window 
and run a few checks on its local environment. It will then ask you a 
series of questions about your group and your camp. This is used to 
generate the relevant paperwork. 

It can generate most of the suite of paperwork required to complete a 
Scout Association nights away permit and for running any nights away 
activity. Based on the user's input, this app will generate a:
* programme
* menu
* kit list to issue to young people
* risk assessment
* group equipment list (request form)
Currently, it can't generate a nights away notification (NAN) form. If 
there is demand, we'll try to include this in a future version. 

It also doesn't generate a health and emergency contact details form 
to give to parents to complete. This is because most Scout Groups 
we've met seem to use Online Scout Manager (OSM) or Google Forms for 
this, which is much easier than paper forms! 

###First run

The first time it runs, nightsawayforms will write default settings to 
the config directory. These are: 
* equipment.json for group equipment
* kitList.json for personal kit lists
* risks.json for risk assessments

It will then ask you a number of questions about your Scout Group and 
section. Your answers will be stored in the config directory, in 
config.json. This is used each time nightsawayforms is run to customize 
the headers of your camp documents. 

A resized logo will also be stored in the config directory for use by 
headers. 

###Camp-specific questions

Every time nightsawayforms runs, it will ask you a series of 
camp-specific questions. These cover the name of the camp, where it 
is, the dates of the camp, and the leader in charge's details. It also 
asks about some key activities. 

These are used to customize headers and a range of factors about each 
of the forms. For example, the dates are used to work out the days on 
camp, which are used to pre-populate the programme and menu. If the 
event has at least one night away, then key data is pre-populated in 
the kit list and risk assessment. 

Finally, this section asks what directory you'd like to save this 
camp's forms in. Typing "Summer camp" will place the forms in a folder 
called "Summer camp" within the same directory as nightsawayforms. 
Typing "C:\Users\PoignantWizard\Desktop\Summer camp" will place the 
forms in a folder called "Summer camp" on the desktop. If the folder 
doesn't exist, nightsawayforms will attempt to create it first. 

###Programme

The programme uses the dates provided to pre-populate the days of the 
week to a table. It then asks for the details of the programme. 

For example: 
1. nightsawayforms asks: "How many activities will there be on Saturday?"
2. you answer: "2"
3. nightsawayforms prompts: "Saturday's activity 1:" 
4. You respond: "Kayaking"
5. nightsawayforms prompts: "Saturday's activity 2:" 
6. You respond: "Cooking on fires"

These responses are pushed into a table and written out into a 
document, saved in the specified directory. 

###Menu

The menu is only generated if say "y" when nightsawayforms asks if 
you will be providing catering. Otherwise it assumes you are relying 
on an alternate provision, such as if the site provides meals. 

The menu uses the dates provided to pre-populate the days of the 
week to a table. It then asks for the details of the menu. 

For example: 
1. nightsawayforms asks: "How many meals will there be on Saturday?"
2. you answer: "3"
3. nightsawayforms prompts: "Saturday's meal 1:" 
4. You respond: "Bacon sandwiches"
5. nightsawayforms prompts: "Saturday's meal 2:" 
6. You respond: "Bacon sandwiches"
7. nightsawayforms prompts: "Saturday's meal 3:"
8. You respond: "Bacon and eggs" 

These responses are pushed into a table and written out into a 
document, saved in the specified directory. 

###Kit list

The kit list uses a JSON file to provide it with all the possible 
options that could be included. These are grouped into several 
categories. The kit list function of nightsawayforms reads these 
categories, asks if you want to include them, and takes action 
based on your response. 

Some categories are automatically added based on the data collected 
when nightsawayforms first starts. For example, if you say "y" when 
it asks whether there will be water activities, the kit list will 
add the "water activities" category to the kit list document. This 
includes information for young people on what to wear afloat for 
activities like sailing. 

nightsawayforms comes with a default kit list JSON file, which it 
deploys on startup if the file doesn't already exist. This can be 
edited with your own categories and kit list. Details on this can 
be found under the advanced usage section. 

###Risk assessment

The risk assessment uses a JSON file to provide it with all the 
possible options that could be included. These are grouped into 
several categories. The risk assessment function of nightsawayforms 
reads these categories, asks if you want to include them, and 
takes action based on your response. 

Some categories are automatically added based on the data collected 
when nightsawayforms first starts. For example, if you say "y" when 
it asks whether you will be using sharps, the risk assessment will 
add the "sharps" category to the risk assessment document. This 
includes mitigations and contingencies based on using knives, axes 
and saws on camp. 

The risk assessment JSON file includes a number of dynamic fields. 
These are denoted with a [XXX] and indicate that this is variable 
between events. When it reaches a risk that contains this marker, 
it will ask for your input. For example, the "first response and 
prescription medication" risk has a [XXX] for the nearest hospital. 
This gives you the opportunity to find out the details of the 
nearest hospital to your camp and add it in. 

nightsawayforms comes with a default risk assessment JSON file, 
which it deploys on startup if the file doesn't already exist. 
This can be edited with your own categories and risk assessments. 
Details on this, and adding your own dynamic fields, can be found 
under the advanced usage section. 

###Group equipment list

The equipment list generates a spreadsheet with a list of group 
equipment. This is produced as a request form as local Scout Groups 
have a central team to manage group equipment who use a request 
system. However, this form can just as easily be used for your own 
reference if your group operates differently. 

The equipment list uses a JSON file to provide it with all the 
possible options that could be included. These are grouped into 
several categories. The equipment function of nightsawayforms reads 
these categories, asks if you want to include them, then goes through 
a list of items and asks if you want to take each one. If so, it will 
ask how many. Finally, it will add this information to the spreadsheet. 

Some categories are automatically assumed to be included based on the 
data collected when nightsawayforms first starts. For example, if you 
say "y" when it asks whether you will be catering (instead of using a 
site's provision), the equipment list will move directly to the 
catering category, asking you what equipment you wish to take and how 
much of each. 

nightsawayforms comes with a default equipment JSON file, which it 
deploys on startup if the file doesn't already exist. This can be 
edited with your own categories and equipment. Details on this, and 
can be found under the advanced usage section. 

###Conclusion

Once nightsawayforms has written all the documents to the desired 
directory, you're free to edit them with a word processor or spreadsheet 
software. When you're happy, you can distribute them as appropriate. 

Don't forget to ask parents for health and emergency contact information 
for their young people. This isn't currently included because most Scout 
Groups we've met seem to use Online Scout Manager (OSM) or Google Forms 
for this, which is much easier than paper forms! 

You also need to remember to complete a Nights Away Notification (NAN) 
form and send it to the relevant commissioner. If there is demand, we'll 
try to include the automatic generation of NAN forms in a future version. 

Finally, enjoy your camping trip! 

##Private data

nightsawayforms is designed to be a stand-alone application. It doesn't 
transmit any of the data it collects. After it completes a run, data 
collected internally is dropped. 

The only data that persists is stored locally on the machine that's 
running the app. This data is stored in JSON files in the config 
directory, which is created in the same directory as the app runs. 
This includes group data to provide convenience across multiple 
sessions. It can also include any data you add to the settings files 
as described in the advanced usage section. 

##Advanced usage

nightsawayforms has been designed to be easy and intuitive to use out 
of the box. For most situations, this will be all that's needed. 
However, the app has a number of advanced features that can be used to 
expand its functionality. 

###Command line options

The app has several command line options. Use: 
* "-c" or "--config" to set up a new Scout Group configuration 
* "-i" or "--ignore" to ignore the existing configuration, saving you 
  having to write a new config just for a session 
* "-d" or "--default" to restore the settings files to defaults 
* "-b" or "--blank" to generate a blank document with a camp header 

Not entering any options will run nightsawayforms normally, as 
described in the getting started section. 

###Custom settings

There are three settings files, which are stored in the config 
directory, which is created in the same directory as the app is run. 
These are in JSON format as its an easy method of providing 
structured data to the app. 

The settings files are: 
* equipment.json
* kitList.json
* risks.json

All three of these can be customised with your preferred editor. 
As long as the fundamental structure of each one is maintained, 
you can be confident in adding data, or changing the existing 
data, without fear of causing an error in the app. 

####equipment.json

The top level key is "equipment" and needs to be maintained. The 
categories below this can safely be added to, changed, or removed  
as needed to fit your circumstances. 

Among the default categories, there are a number of special 
categories. The app treats these differently based on certain 
conditions. 

If the dates of your camp mean there is at least one night away, 
the following categories are automatically accepted: 
* sleeping 
* hygiene 
* light 

If you indicated that you would be catering, using sharps, or 
taking part in water activities, the following categories are 
automatically accepted as relevant: 
* catering 
* sharps 
* water activities 

You can safely add, change, or remove items from the list beneath 
any of the categories. 

####kitList.json

The top level key is "kit" and needs to be maintained. The categories 
below this can safely be added to, changed, or removed as needed to 
fit you circumstances. 

Among the default categories, there are a number of special categories. 
The app treats these differently based on certain conditions. 

If the dates of your camp mean there is at least one night away, the 
following categories are automatically included: 
* bags 
* clothing 
* sleeping 
* hygiene 

If you indicated that you would be catering or taking part in water 
activities, the following categories are automatically included as 
relevant: 
* catering 
* water activities 

The exclude category is another special case. Any items stored under 
this category are included in a paragraph asking young people not to 
bring them. 

The web category contains one item. This is a URL where parents and 
their young people can go to find more information about camping, kit 
and purchasing new kit. Many Scout Groups hold this on their own 
websites, for example. 

You can safely remove the exclude and web categories. If you do, the 
app won't write the paragraphs that include these details. 

You can safely add, change, or remove items from the list beneath 
any of the categories. 

####risks.json 

The top level key is "risks" and needs to be maintained. The categories 
below this can safely be added to, changed, or removed as needed to 
fit you circumstances. 

Each of the categories then contain a number of "risks", which each have 
a "mitigation" and a "contingency". This structure needs to be 
maintained, even if a category only contains one risk. 

Among the default categories, there are a number of special categories. 
The app treats these differently based on certain conditions. 

If the dates of your camp mean there is at least one night away, the 
following categories are automatically included: 
* health 
* environmental 

If you indicated that you would be catering, using sharps, or 
taking part in water activities, the following categories are 
automatically included as relevant: 
* catering 
* sharps 
* water activities 

You can safely add, change, or remove risks from the list beneath 
any of the categories. 

Some risks contain the indicator [XXX] in their mitigation or 
contingency. The [XXX] indicates a dynamic field. If the app finds 
one of these, it prints the section to the terminal and requests 
user input. The user data is used to replace the [XXX]. 

You can add a [XXX] to any mitigation or contingency if these are 
variable between camps and so need user input. 

##Libraries used

nightsawayforms is written in python 3.6 and makes use of several 
libraries. These are: 
* argparse
* datetime
* json
* openpyxl
* os
* pillow
* platform
* python-docx
