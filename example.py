import messages

# create a new instance of a MessageCarrier
mb = messages.MessageCarrier("example@gmail.com","password")

# sends message
mb.sendMessage("message","1234567890@vtext.com")

# prints out the newest message in inbox
print(mb.get_newest_message())
