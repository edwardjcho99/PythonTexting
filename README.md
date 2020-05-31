# PythonTexting
PythonTexting is a package I created that assists in easy SMS texting to and from a gmail account. This package uses the built in smtplib and imaplib libraries to process these simple SMS requests. Although this project uses only a fraction of these libraries' capabilities, it is perfect for quickly setting up SMS texting in my projects. You only need the messages.py module for this to work, but I put it in a package in case you want to mess around with the example.py module, too.

# How To Use
In the example.py module, I perform the two functions that this package can do.

First, you must make a MessageCarrier object, inputing your gmail username and password:  
`<MessageCarrierObjectName> = messages.MessageCarrier("example@gmail.com","password")`

To send a message, simply:  
`<MessageCarrierObjectName>.send_message("your message here","1234567890@carrier.com")`

To get the most recent message in your gmail account:  
`<MessageCarrierObjectName>.get_newest_message()`

# Caveats
In order for this to work, you must turn on "Allow Less Secure Apps" in your gmail account. Note this security vulnerability, and make sure to turn off the setting when you are done using PythonTexting.
