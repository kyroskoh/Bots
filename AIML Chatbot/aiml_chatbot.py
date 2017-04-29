import aiml
import os

kernel=aiml.Kernel()
kernel.learn("./basic.xml")
kernel.respond("load aiml b")

if os.path.isfile("bot_brain.brn"):
	kernel.bootstrap(brainFile="bot_brain.brn")
else:
	kernel.bootstrap(learnFiles="./basic.xml",commands="load aiml b")
	kernel.saveBrain("bot_brain.brn")

while True:
	message=raw_input("Enter your message:")
	if message=="quit" or message=="exit":
		exit()
	elif message=="save":
		kernel.saveBrain("bot_brain.brn")
	else:
		print kernel.respond(message)