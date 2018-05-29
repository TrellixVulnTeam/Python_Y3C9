


"""

Python 3 - Sending Email using SMTP

Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending an e-mail and routing e-mail between mail servers.

Python provides smtplib module, which defines an SMTP client session object that can be used to send mails to any Internet machine with an SMTP or ESMTP listener daemon.

Here is a simple syntax to create one SMTP object, which can later be used to send an e-mail −

import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
Here is the detail of the parameters −

host − This is the host running your SMTP server. You can specifiy IP address of the host or a domain name like tutorialspoint.com. This is an optional argument.

port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.

local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost the option.

An SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters −

The sender − A string with the address of the sender.

The receivers − A list of strings, one for each recipient.

The message − A message as a string formatted as specified in the various RFCs.

Example
Here is a simple way to send one e-mail using Python script. Try it once −


"""

import smtplib

sender = 'jm.kagaya@gmail.com'
receivers = ['jm.kagaya25@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"



"""

Here, you have placed a basic e-mail in message, using a triple quote, taking care to format the headers correctly. An e-mail requires a From, To, and a Subject header, separated from the body of the e-mail with a blank line.

To send the mail you use smtpObj to connect to the SMTP server on the local machine. Then use the sendmail method along with the message, the from address, and the destination address as parameters (even though the from and to addresses are within the e-mail itself, these are not always used to route the mail).

If you are not running an SMTP server on your local machine, you can the use smtplib client to communicate with a remote SMTP server. Unless you are using a webmail service (such as gmail or Yahoo! Mail), your e-mail provider must have provided you with the outgoing mail server details that you can supply them, as follows −

mail = smtplib.SMTP('smtp.gmail.com', 587)


"""


