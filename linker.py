import requests, sys, traceback, re, json, time, select, socket
from websocket import create_connection
from colorama import init, Fore, Back, Style

'''
LinkerBot
This operates 10 echobots in Rizon's IRC network that repeat text from Destiny's website's chat.
The large number of bots is to avoid channel flood throttling.
Despite this, messages occasionally still don't transmit due to extreme chat activity.
'''

init()
first = ""
msgcount = 0
pingcount = 0
fo = open("rizonlog.txt", "a")
PORT=6667
channel = "#destinyecho"
mydict = {"\u003e":">","\u003c":"<","\\\"":"\"","\\\\":"\\"}
def log(c,s):
	print(Fore.BLUE + Style.BRIGHT + time.asctime() + Fore.RESET + " " + c + s + Fore.RESET + Back.RESET + Style.NORMAL)
def s1connect():
	NICK = IDENT = REALNAME = "I|||||||||"
	HOST = "irc.thefear.ca"
	global s1
	s1=socket.socket( )
	s1.connect((HOST, PORT))
	s1.send("NICK %s\r\n" % NICK)
	s1.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s1.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s1 connect")
	time.sleep( 5 )
def s2connect():
	NICK = IDENT = REALNAME = "|I||||||||"
	HOST="irc.broke-it.com"
	global s2
	s2=socket.socket( )
	s2.connect((HOST, PORT))
	s2.send("NICK %s\r\n" % NICK)
	s2.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s2.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s2 connect")
	time.sleep( 5 )
def s3connect():
	NICK = IDENT = REALNAME = "||I|||||||"
	HOST="irc.cccp-project.net"
	global s3
	s3=socket.socket( )
	s3.connect((HOST, PORT))
	s3.send("NICK %s\r\n" % NICK)
	s3.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s3.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s3 connect")
	time.sleep( 5 )
def s4connect():
	NICK = IDENT = REALNAME = "|||I||||||"
	HOST="irc.cyberdynesystems.net"
	global s4
	s4=socket.socket( )
	s4.connect((HOST, PORT))
	s4.send("NICK %s\r\n" % NICK)
	s4.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s4.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s4 connect")
	time.sleep( 5 )
def s5connect():
	NICK = IDENT = REALNAME = "||||I|||||"
	HOST="irc.rizon.io"
	global s5
	s5=socket.socket( )
	s5.connect((HOST, PORT))
	s5.send("NICK %s\r\n" % NICK)
	s5.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s5.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s5 connect")
	time.sleep( 5 )
def s6connect():
	NICK = IDENT = REALNAME = "|||||I||||"
	HOST="irc.rizon.us"
	global s6
	s6=socket.socket( )
	s6.connect((HOST, PORT))
	s6.send("NICK %s\r\n" % NICK)
	s6.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s6.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s6 connect")
	time.sleep( 5 )
def s7connect():
	NICK = IDENT = REALNAME = "||||||I|||"
	HOST="irc.sxci.net"
	global s7
	s7=socket.socket( )
	s7.connect((HOST, PORT))
	s7.send("NICK %s\r\n" % NICK)
	s7.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s7.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s7 connect")
	time.sleep( 5 )
def s8connect():
	NICK = IDENT = REALNAME = "|||||||I||"
	HOST="irc.shakeababy.net"
	global s8
	s8=socket.socket( )
	s8.connect((HOST, PORT))
	s8.send("NICK %s\r\n" % NICK)
	s8.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s8.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s8 connect")
	time.sleep( 5 )
def s9connect():
	NICK = IDENT = REALNAME = "||||||||I|"
	HOST="irc.lolipower.org"
	global s9
	s9=socket.socket( )
	s9.connect((HOST, PORT))
	s9.send("NICK %s\r\n" % NICK)
	s9.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s9.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s9 connect")
	time.sleep( 5 )
def s10connect():
	NICK = IDENT = REALNAME = "|||||||||I"
	HOST="irc.siglost.com"
	global s10
	s10=socket.socket( )
	s10.connect((HOST, PORT))
	s10.send("NICK %s\r\n" % NICK)
	s10.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	s10.send("JOIN " + channel + "\n")
	log(Fore.RESET, "s10 connect")
	#time.sleep( 5 )
def wsconnect():
	global ws
	ws = create_connection("ws://www.destiny.gg:9998/ws", header={"Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "ws connect")
def dharmaggconnect():
	global dharmagg
	dharmagg = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "dharma connect")
def woopggconnect():
	global woopgg
	woopgg = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "woop connect")
def bronzerggconnect():
	global bronzergg
	bronzergg = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "bronzer connect")
def slugconnect():
	global slug
	slug = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "slug connect")
def bubbleconnect():
	global bubble
	bubble = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "bubble connect")
def fruitconnect():
	global fruit
	fruit = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "fruit connect")
def xxconnect():
	global xx
	xx = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "xx connect")
def lemonconnect():
	global lemon
	lemon = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "lemon connect")
def jpconnect():
	global jp
	jp = create_connection("ws://www.destiny.gg:9998/ws", header={"Cookie: sid=xx","Origin: http://www.destiny.gg"})
	log(Fore.GREEN , "jp connect")
def s1msg(msg):
	global msgcount
	msgcount += 1
	if msgcount == 1:
		try:
			s1.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s1.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 2:
		try:
			s2.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s2.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 3:
		try:
			s3.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s3.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 4:
		try:
			s4.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s4.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 5:
		try:
			s5.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s5.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 6:
		try:
			s6.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s6.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 7:
		try:
			s7.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s7.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 8:
		try:
			s8.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s8.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 9:
		try:
			s9.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s9.send("PRIVMSG " + channel + " :" + msg + "\n")
	if msgcount == 10:
		msgcount = 0
		try:
			s10.send("PRIVMSG " + channel + " :" + msg.encode('utf-8') + "\n")
		except (UnicodeDecodeError, UnicodeEncodeError):
			s10.send("PRIVMSG " + channel + " :" + msg + "\n")
s1connect()
s2connect()
s3connect()
s4connect()
s5connect()
s6connect()
s7connect()
s8connect()
s9connect()
s10connect()
wsconnect()
dharmaggconnect()
slugconnect()
bubbleconnect()
fruitconnect()
xxconnect()
lemonconnect()
bronzerggconnect()
woopggconnect()
jpconnect()
log(Fore.BLUE + Back.RED , "v117.aaaaaaaaaa" )
s1msg("Goliath online.")
while 1:
	try:
		(r, w, x) = select.select([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, ws, dharmagg, woopgg, slug, bubble, fruit, xx, bronzergg, lemon, jp], [], [])
		for sock in r:
			if (sock == s1) or (sock == s2) or (sock == s3) or (sock == s4) or (sock == s5) or (sock == s6)  or (sock == s7) or (sock == s8) or (sock == s9) or (sock == s10) :
				data = sock.recv(1024).strip('\r\n')
				m = re.search(':[|I]+!~[|I]+@\S+ PRIVMSG #destinyecho.* :<\w+?>.*', data)
				if m is None:
					if first != data and data.find('PING') != 0:
						first = data
						if sock == s1:
							log(Fore.RESET , "1=" + data)
						elif sock == s2:
							log(Fore.RESET , "2=" + data)
						elif sock == s3:
							log(Fore.RESET , "3=" + data)
						elif sock == s4:
							log(Fore.RESET , "4=" + data)
						elif sock == s5:
							log(Fore.RESET , "5=" + data)
						elif sock == s6:
							log(Fore.RESET , "6=" + data)
						elif sock == s7:
							log(Fore.RESET , "7=" + data)
						elif sock == s8:
							log(Fore.RESET , "8=" + data)
						elif sock == s9:
							log(Fore.RESET , "9=" + data)
						elif sock == s10:
							log(Fore.RESET , "10=" + data)
				if sock == s1:
					m = re.search(':(.*?)!(.*?) PRIVMSG #(.*?) :(.*)', data)
					if m is not None:
						origin = m.group(4)
						mystr = m.group(4)
						for k, v in mydict.iteritems():
							mystr = mystr.replace(v, k)
						if m.group(2) == "~woopitybo@head.against.the.heart" and origin[0] != "<":
							if mystr[0] == "~":
								woopgg.send('MSG {"data":"' + mystr[1:] + '"}')
							else:
								dharmagg.send('MSG {"data":"' + mystr + '"}')
						if "@vee.hoast" in m.group(2) and origin[0] != "<":
							bronzergg.send('MSG {"data":"' + mystr + '"}')
						elif "@28E293F6.8D0AAF9A.B646B4DE.IP" in m.group(2) and origin[0] != "<":
							slug.send('MSG {"data":"' + mystr + '"}')
						elif "@just.keep.swimming" in m.group(2) and origin[0] != "<":
							bubble.send('MSG {"data":"' + mystr + '"}')
						elif "@fruit.of.doom" in m.group(2) and origin[0] != "<":
							fruit.send('MSG {"data":"' + mystr + '"}')
						elif "@xxtphty.host" in m.group(2) and origin[0] != "<":
							xx.send('MSG {"data":"' + mystr + '"}')
						elif "@stay.noided" in m.group(2) and origin[0] != "<":
							lemon.send('MSG {"data":"' + mystr + '"}')
						elif "@goodDeals.jpham9210" in m.group(2) and origin[0] != "<":
							jp.send('MSG {"data":"' + mystr + '"}')
					elif data == "":
						s1connect()
				elif sock == s2:
					if data == "":
						s2connect()
				elif sock == s3:
					if data == "":
						s3connect()
				elif sock == s4:
					if data == "":
						s4connect()
				elif sock == s5:
					if data == "":
						s5connect()
				elif sock == s6:
					if data == "":
						s6connect()
				elif sock == s7:
					if data == "":
						s7connect()
				elif sock == s8:
					if data == "":
						s8connect()
				elif sock == s9:
					if data == "":
						s9connect()
				elif sock == s10:
					if data == "":
						s10connect()
				if data.find('PING') != -1:
					sock.send('PONG ' + data.split() [1] + '\r\n')
			else:
				try:
					data = sock.recv().strip('\r\n')
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
					if data[0:4] == "PING":
						sock.send("PONG" + data[4:])
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
							if pingcount % 300 == 0:
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #bronzer
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #slug
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #bubble
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #woopboop
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #lemon
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #jp
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #fruit
								requests.Session().get('http://www.destiny.gg/ping', headers={"Cookie": "sid=xx"}) #xx
								log(Fore.YELLOW, "SESSION REFRESHED")
							pingcount += 1
						elif command == "NAMES" or command == "QUIT" or command == "JOIN":
							pass
						elif command != "":
							s1msg( "<UNKNOWN_COMMAND> " + data)
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
						traceback.print_tb(sys.exc_info()[2])
						log(Fore.RED , str(sys.exc_info()))
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