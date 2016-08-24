import logging
import socket
print('start')

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',
level = logging.DEBUG, filename = u'/home/mihail/Документы/Coding/python/MyDefender/log')

logging.debug("start")

sock = socket.socket()
sock.bind(('', 65090))

while True:
	sock.listen(1)
	conn, addr = sock.accept()
	file_white = open('/home/mihail/Документы/Coding/python/MyDefender/whitelist', 'r')
	file_black = open('/home/mihail/Документы/Coding/python/MyDefender/blacklist', 'w+')

	control = (str(file_white.read(1))=='1')
	file_white.seek(0)
	if(not control):
		logging.critical("CONTROL IS DISABLED!")	

	#print('connected:', addr)
	logging.debug("connected"+str(addr))
	
	data=""
	while True:
		data = conn.recv(1024)
		if not data: break
		logging.debug(data)
		#print(data)
		fl = False
		for line in file_white:
			if (data.decode("utf-8") == line[:-1] or (not control)):
				#print('Access forward\n')
				logging.debug("Access allowed")
				conn.send("ok!".encode("utf-8"))
				fl = True
		if (not fl):
			#print('Access denied\n')
			logging.debug("Access denied")
			file_black.write(file_black.read()+data.decode("utf-8")+"\n")
			conn.send("nit".encode("utf-8"))
		if(not control):
			file_black.write(file_black.read()+data.decode("utf-8")+"\n")
	conn.close()
	file_black.close()
	file_white.close()
