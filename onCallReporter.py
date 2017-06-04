'''
Automatic Browser screenshots - v1.0
Automatically takes screenshots of all pages (urls) supplied
after 10secs or ENTER press (if in exception list)
@Author: jswarnakar, 2017
'''

# Requires selenium for monitor and dispatching
# Time, os for usual manipulation
# PIL (pillow) for image resizing.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import PIL
from PIL import Image
import os

#trying to use Chrome. If you want to use another browser
#please download the driver and export its path to env variables
browser = webdriver.Chrome()

'''
add all reporting urls here with settings premade in the URL itself
(In order):
- Google
- facebook
- amazon.in
'''
reports_for=['https://www.google.com',
            'https://www.facebook.com',
            'https://www.amazon.in']

reports_title=[]    #get titles dynamically from webpage loaded, will be used when emailing

#Place all your URL exceptions here, for which you want to wait until page
#is loaded. For example when waiting till enter uname/pwd or page components loading.
exceptions_substrings=['amazon', 'splunk']
exception_at='' #donot touch this

SCREEN_SHOT_PFIX="screenshot_report_"

'''
Does the checkstring belongs to an exceptional URL?
If yes then say True
'''
def isAnExceptionForAutomation(checkString):
    index = 0
    while index < len(exceptions_substrings):
        if exceptions_substrings[index] in checkString:
            exception_at = exceptions_substrings[index]
            return True
        index = index + 1
    return False


'''
Method to get the screen shot at an index
'''
def getSS(index):
    if index < len(reports_for):
        url = reports_for[index]
        #open web page and wait for 10secs to load completely
        browser.get(url)
        time.sleep(10)

        #if this webpage was in exceptions list, then wait for user to press any
        #key to confirm that the page has loaded:
        if(isAnExceptionForAutomation(url)):
            print "Trying to load: "+str(exception_at)+"."
            os.system('read -p "Press ENTER to continue with screenshot when all elements have fully loaded"')

        #get screenshot
        browser.save_screenshot("./ss/"+SCREEN_SHOT_PFIX+str(index)+".png")
        reports_title.append(str(browser.title))
        #push webpage title

        return True
    else:
        print "Index out of range"
        return False


'''
Entry point to start recording reports
'''
def startReports():
    each_index=0
    while each_index < len(reports_for):
        dataGrabbed = getSS(each_index)
        if dataGrabbed == False:
            print "Exiting script at index: "+str(each_index)
            break
        each_index = each_index + 1


'''
Method to start emailing the reports
'''
def sendReports():
    index=0
    while index < len(reports_title):
        print reports_title[index]
        index = index + 1

'''
Cleanup method to remove disk files to avoid
cluttering.
'''
def cleanup():
    index = 0
    while index < len(reports_title):
        os.system('rm '+SCREEN_SHOT_PFIX+str(index)+'.png')
        index = index + 1


'''START PROGRAM'''
startReports()
#Close window
browser.close()
sendReports()
# cleanup()
