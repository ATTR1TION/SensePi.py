# SensePi.py

This project is taken by a tutorial made by James Bruce for the Raspberry Pi [located here.](https://www.makeuseof.com/tag/scare-trick-treaters-diy-motion-activated-soundbox/)

Using a simple PIR sensor connected to a Raspberry Pi, you can make a motion detector spooky noise machine.

I bought mine from [Amazon](https://www.amazon.com/gp/product/B00L11K4RQ/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1) or you can buy it on Ebay. Just search for "PIR Sensor".

# Setup

Connect your sensor to the Ground, 5v, and GPIO4 (pin 7). 

Power on the raspberry and set it up. Using your editor of choice, create the script and copy the code. 

Test it out using the Python command

>python (codename).py

# Finishing it up

Set up a cron job to automatically run the script at startup. 

>sudo crontab -e

>@reboot python (script file path)
