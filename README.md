#On Call Reporter

This module makes it easy (basically almost automatic) to send On-Call reports by taking all the relevant screenshots and placing them under one folder. You can make any other use if you want.  Compatible with Python 2.xx

##Installation
This is pretty straight forward. Run with python2:
> python oncallReportInstaller.py

Wait for the install to compelte. This does nothing but, installs selenium and PIL libs. Also along with that, it also copies webdriver for gecko (used with selenium for clearning proxies) and webdriver for Chrome. Note: By default selenium uses Firefox, but we have made this for chrome as it is widely used here. Please headover to seleniumHQ to know more about different web browsers supported, their usage and webdrivers sources (for chrome, we got this from google's cloud and is the lates update as on 5-Jun-2017).


##Usage
Run with python:
> python onCallReporter.py

This will sequentially open all webpages mentioned in the python list. The flow is as follows (that you would see):
- Triggers a web page in the browser
- Waits for 10secs (script goes to sleep mode while the page loads)
- Takes a screenshot, and places in the 'ss' folder
- After script ends, sequentially prints the relevant heading of the page fetched.

Note: For some cases there is a significant time that is required (either page loading such as in Splunk or credentials such as in Nagios). 
They have already been specified in the 'exceptions_substrings' list. For these exceptions, the python terminal will wait for you to press ENTER whenever you feel is the correct time (by adjusting zoom size and looking that everything has loaded). Once ENTER is pressed, the screenshot is grabbed and automation proceeds as it has to. Currently we only have Splunk and Nagios in this list and the script will wait until you press ENTER to proceed.

PS: For all future usage, please keep on adding URLs to the main list (i.e. reports_for) and if you feel that this is time consuming (> 10sec loadtime), then please specify a distinct substring of this URL in the exceptions list.

##Whats next?
We will use PIL to resize image to a smaller size, the exception probably being Nagios. Also a mailto config will be added to add them as attachments to a new mail window.
