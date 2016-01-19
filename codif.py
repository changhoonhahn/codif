#!/usr/bin/python
username        = 'changs.code@gmail.com'
passwd          = 'Changh37'

import sys,os
import optparse
import pylab as pl
import re
from numpy import array,random,argsort, where
import smtplib
from datetime import datetime

def notif(toaddr='changh20@gmail.com', subject=None, message=None):
    """
    Sends an email notification through GMail .
    """
    fromaddr='changs.code@gmail.com'

    # Initialize SMTP server
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,passwd)

    # Send email
    senddate=datetime.strftime(datetime.now(), '%Y-%m-%d')
    if subject is None: 
        subject="Notification"
    m = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "Subject: %s\r\n" % subject + "\r\n" 
    if message is None: 
        msg = '''
        Notification. 
        '''
    else: 
        msg = message

    server.sendmail(fromaddr, [toaddr], m+msg)
    server.quit()
