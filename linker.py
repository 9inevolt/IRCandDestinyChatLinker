#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests, sys, traceback, re, json, time, select, socket
from websocket import create_connection
from colorama import init, Fore, Back, Style

'''
LinkerBot
This operates one echobot in Rizon's IRC network that repeat text from Destiny's website's chat.
Many thanks to "djahandarie", a Rizon admin who allowed me bypass the flood limiters, hence the censored password.
A disadvantage is that if irc.siglost.com goes down, the bot will cease to function, but that's an acceptable consequence.
A future update will rejoin other servers to send messages if/when irc.siglost.com goes down.
Could also use some significant DRYing up.
'''

init()
pingcount = 0
ggtime = datetime.datetime.utcnow()
fo = open("rizonlog.txt", "a")
HOST="irc.siglost.com"
NICK = IDENT = REALNAME = "II"
PORT=6667
channel = "#destinyecho"
mydict = {"\u003e":">","\u003c":"<","\\\"":"\"","\\\\":"\\"}

# colors & timestamps console output
def log(c,s):
	print(Fore.BLUE + Style.BRIGHT + time.asctime() + Fore.RESET + " " + c + s + Fore.RESET + Back.RESET + Style.NORMAL)

# connects to chat servers
def s1connect():
	global s1
	s1=socket.socket( )
	s1.connect((HOST, PORT))
	s1.send("PASS MYLOVELYFLOODBYPASSPASSWORD\r\n")
	s1.send("NICK %s\r\n" % NICK)
	s1.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s1.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s1 connect")
def wsconnect():
	global ws
	ws = create_connection("ws://www.destiny.gg:9998/ws", header={"Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "ws connect")
def dharmaggconnect():
	global dharmagg
	dharmagg = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "dharma connect")
def woopggconnect():
	global woopgg
	woopgg = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "woop connect")
def bronzerggconnect():
	global bronzergg
	bronzergg = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "bronzer connect")
def slugconnect():
	global slug
	slug = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "slug connect")
def salvageconnect():
	global salvage
	salvage = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "salvage connect")
def asoconnect():
	global aso
	aso = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "aso connect")
def sharkconnect():
	global shark
	shark = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "shark connect")
def szconnect():
	global sz
	sz = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "sz connect")
def opconnect():
	global op
	op = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "op connect")
def chrisconnect():
	global chris
	chris = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "chris connect")
def bubbleconnect():
	global bubble
	bubble = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "bubble connect")
def fruitconnect():
	global fruit
	fruit = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "fruit connect")
def xxconnect():
	global xx
	xx = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "xx connect")
def lemonconnect():
	global lemon
	lemon = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "lemon connect")
def jpconnect():
	global jp
	jp = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: authtoken=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "jp connect")

#sends to IRC
def s1msg(msg):
	try:
		s1.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
	except (UnicodeDecodeError, UnicodeEncodeError):
		s1.send("PRIVMSG " + channel + " :" + msg + "\n")

# connects to chat
s1connect()
wsconnect()
dharmaggconnect()
slugconnect()
salvageconnect()
asoconnect()
sharkconnect()
szconnect()
opconnect()
chrisconnect()
bubbleconnect()
fruitconnect()
xxconnect()
lemonconnect()
bronzerggconnect()
woopggconnect()
jpconnect()

# primary loop
log(Fore.BLUE + Back.RED , "microversion #gamma" )
s1msg("Carrier has arrived.")
while 1:
	
	# encapsulating try ensures the script still runs even if an error occurs.
	try:
		
		# handles multiple connections
		(r, w, x) = select.select([s1, ws, dharmagg, woopgg, slug, salvage, aso, shark, sz, op, chris, bubble, fruit, xx, bronzergg, lemon, jp], [], [])
		for sock in r:
			
			# handles IRC connection
			if (sock == s1):
				data = sock.recv(1024).strip('\r\n')
				if data[:4] != "PING":
					log(Fore.RESET, data)
				m = re.search(':(.*?)!(.*?) PRIVMSG #(.*?) :(.*)', data)
				if m is not None:
					origin = m.group(4)
					mystr = m.group(4)
					for k, v in mydict.iteritems():
						mystr = mystr.replace(v, k)
					
					# admin commands
					if "@head.against.the.heart" in m.group(2) and origin[0] != "<":
						if mystr[0] == "~":
							woopgg.send('MSG {"data":"' + mystr[1:] + '"}')
						elif origin.find("!switch") == 0:
							a = ""
							for x in range(0,randint(3, 30)):
								a = "I" + a
							s1.send("NICK %s\r\n" % a)
						elif origin.find("!reset") == 0:
							s1.send("NICK II\r\n")
						elif origin.find("!mute") == 0:
							dharmagg.send('MUTE {"data":"' + origin.strip().split(" ")[1] + '", "duration":' + str(int(origin.strip().split(" ")[2])*60000000000) + '}')
						elif origin.find("!unban") == 0:
							dharmagg.send('UNBAN {"data":"' + origin.strip().split(" ")[1] + '"}')
						elif origin.find("!unmute") == 0:
							dharmagg.send('UNMUTE {"data":"' + origin.strip().split(" ")[1] + '"}')
						elif origin.find("!ipban") == 0:
							dharmagg.send('BAN {"nick":"' + origin.strip().split(" ")[1] + '", "duration":' + str(int(origin.strip().split(" ")[2])*60000000000) + ', "reason":"' + str(origin.strip().split(" ",3)[3:][0]) + '", "banip":true }')
						elif origin.find("!ban") == 0:
							dharmagg.send('BAN {"nick":"' + origin.strip().split(" ")[1] + '", "duration":' + str(int(origin.strip().split(" ")[2])*60000000000) + ', "reason":"' + str(origin.strip().split(" ",3)[3:][0]) + '"}')
						else:
							dharmagg.send('MSG {"data":"' + mystr + '"}')

					# other users, generally identified by their vmask or IP address
					elif "@vee.hoast" in m.group(2) and origin[0] != "<":
						bronzergg.send('MSG {"data":"' + mystr + '"}')
					elif "@28E293F6.8D0AAF9A.B646B4DE.IP" in m.group(2) and origin[0] != "<":
						slug.send('MSG {"data":"' + mystr + '"}')
					elif "@no.ipaddress.here" in m.group(2) and origin[0] != "<":
						salvage.send('MSG {"data":"' + mystr + '"}')
					elif "AsoSako" == m.group(1) and origin[0] != "<":
						aso.send('MSG {"data":"' + mystr + '"}')
					elif "@ooh.ha.ha" in m.group(2) and origin[0] != "<":
						#shark.send('MSG {"data":"' + mystr + '"}')
						s1msg("Sharkbait, your SID is no longer valid, please consult the topic. If you wish to continue forwarding, I'll need the \"key\".")#unmsged
					elif "@sztanpet.fake" in m.group(2) and origin[0] != "<":
						sz.send('MSG {"data":"' + mystr + '"}')
					elif "@sup.bros" in m.group(2) and origin[0] != "<":
						op.send('MSG {"data":"' + mystr + '"}')
					elif "@i.am.the.hentai.prince" in m.group(2) and origin[0] != "<":
						chris.send('MSG {"data":"' + mystr + '"}')
					elif "@just.keep.swimming" in m.group(2) and origin[0] != "<":
						#bubble.send('MSG {"data":"' + mystr + '"}')
						s1msg("i3ubbles, your SID is no longer valid, please consult the topic. If you wish to continue forwarding, I'll need the \"key\".")
					elif "@fruit.of.doom" in m.group(2) and origin[0] != "<":
						fruit.send('MSG {"data":"' + mystr + '"}')
					elif "@xxtphty.host" in m.group(2) and origin[0] != "<":
						#xx.send('MSG {"data":"' + mystr + '"}')
						s1msg("xxtphty, your SID is no longer valid, please consult the topic. If you wish to continue forwarding, I'll need the \"key\".")#unmsged
					elif "@stay.noided" in m.group(2) and origin[0] != "<":
						lemon.send('MSG {"data":"' + mystr + '"}')
					elif "@goodDeals.jpham9210" in m.group(2) and origin[0] != "<":
						jp.send('MSG {"data":"' + mystr + '"}')

				# disconnect detected
				elif data == "":
					s1connect()

				elif data.find('PING') != -1:
					sock.send('PONG ' + data.split() [1] + '\r\n')
			
			# handles websocket connections
			else:
				
				# encapsulating try reports websocket errors
				try:
					ggtime = datetime.datetime.utcnow() #reconnect time initializer
					data = sock.recv().strip('\r\n')
					
					# determines where error occured.
					if data[:3] == "ERR":
						if sock == ws:
							socky = "ws"
						elif sock == dharmagg:
							socky = "dharma"
						elif sock == woopgg:
							socky = "woop"
						elif sock == bronzergg:
							socky = "bronzer"
						elif sock == slug:
							socky = "slug"
						elif sock == salvage:
							socky = "salvage"
						elif sock == aso:
							socky = "aso"
						elif sock == shark:
							socky = "shark"
						elif sock == sz:
							socky = "sz"
						elif sock == op:
							socky = "op"
						elif sock == chris:
							socky = "chris"
						elif sock == bubble:
							socky = "bubble"
						elif sock == fruit:
							socky = "fruit"
						elif sock == xx:
							socky = "xx"
						elif sock == lemon:
							socky = "lemon"
						elif sock == jp:
							socky = "jp"
						else:
							socky = "unknown sock"
						s1msg("<CHAT_ERROR> " + socky + ":" + data)
					
					# pingpong
					if data[0:4] == "PING":
						sock.send("PONG" + data[4:])
					
					# primary websocket connection that sends messages to IRC via s1msg
					if sock == ws:
						a = data.split(' ',1)
						command = a[0]
						try:
							payload = json.loads(a[1])
						except (KeyboardInterrupt, SystemExit):
							raise
						except:
							s1msg("<JSON_ERROR> Probable disconnect. " + data)
							log(Fore.RED, "Json error: " + data )
						if command == "MSG":
							mystr = payload["data"]
							for k, v in mydict.iteritems():
								mystr = mystr.replace(k, v)
							s1msg( "<" + payload["nick"] + "> " + mystr)
						elif command == "MUTE":
							s1msg( "<" + payload["nick"] + "> <=== just muted " + payload["data"])
						elif command == "UNMUTE":
							s1msg( "<" + payload["nick"] + "> <=== just unmuted " + payload["data"])
						elif command == "SUBONLY":
							if payload["data"] == "on":
								s1msg( "<" + payload["nick"] + "> <=== just enabled subscribers only mode.")
							else:
								s1msg( "<" + payload["nick"] + "> <=== just disabled subscribers only mode.")
						elif command == "BAN":
							s1msg( "<" + payload["nick"] + "> <=== just banned " + payload["data"])
						elif command == "UNBAN":
							s1msg( "<" + payload["nick"] + "> <=== just unbanned " + payload["data"])
						elif command == "PING":
							sock.send("PONG" + data[4:])
						elif command == "NAMES" or command == "QUIT" or command == "JOIN":
							pass
						elif command != "":
							s1msg( "<UNKNOWN_COMMAND> " + data)
				
				# reconnects on error, typically a websocket disconnect
				except:
					try:
						time.sleep( 2 )
						if sock == ws:
							s1msg("Websocket disconnect, attempting reconnect...")
							wsconnect()
						elif sock == dharmagg:
							dharmaggconnect()
						elif sock == woopgg:
							woopggconnect()
						elif sock == bronzergg:
							bronzerggconnect()
						elif sock == slug:
							slugconnect()
						elif sock == salvage:
							salvageconnect()
						elif sock == aso:
							asoconnect()
						elif sock == shark:
							sharkconnect()
						elif sock == sz:
							szconnect()
						elif sock == op:
							opconnect()
						elif sock == chris:
							chrisconnect()
						elif sock == bubble:
							bubbleconnect()
						elif sock == fruit:
							fruitconnect()
						elif sock == xx:
							xxconnect()
						elif sock == lemon:
							lemonconnect()
						elif sock == jp:
							jpconnect()
					except (KeyboardInterrupt, SystemExit):
						raise
					except:
						log(Fore.RED,"Random error in dharmagg?")
			
			# reconnects after 2 minutes of inactivity, hopefully
			if int((datetime.datetime.utcnow() - ggtime).total_seconds()) > 120:
				wsconnect()
				dharmaggconnect()
				slugconnect()
				salvageconnect()
				asoconnect()
				sharkconnect()
				szconnect()
				opconnect()
				chrisconnect()
				bubbleconnect()
				fruitconnect()
				xxconnect()
				lemonconnect()
				bronzerggconnect()
				woopggconnect()
				jpconnect()
			#fo.write( data + "\n")
			#print data
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		try:
			s1msg( "<UNKNOWN_ERROR> " + str(data))
			log(Fore.RED , "penultimate error " + str(data))
			traceback.print_tb(sys.exc_info()[2])
			log(Fore.RED , str(sys.exc_info()))
		except:
			log(Fore.RED , "fucking horrible error")
			traceback.print_tb(sys.exc_info()[2])
			log(Fore.RED , str(sys.exc_info()))