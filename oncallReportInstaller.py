import os

print "# # # # # # # # # # OnCallReporter Installer # # # # # # # # # #"
print ""
print ""

print "Installing dependencies.."

print "\t--Selenium"
# Install and upgrade selenium
os.system('sudo pip install -U selenium')

print "\t--PIL"
#install PIL (now pillow umbrella)
os.system('sudo pip install Pillow')

print ""

print "Copying drivers - gecko and chrome"
#copy drivers to /usr/sbin - requires sudo
os.system('sudo cp ./geckodriver /usr/sbin')
os.system('sudo cp ./chromedriver /usr/sbin')

print ""
print "# # # # # # # # # # Install Complete # # # # # # # # # # "
