from threading import Thread 
from socket import *

#1收数据，打印
def recv_data():
	addr = ("",12348)
	udp_socket.bind(addr)
	while True:
		info = udp_socket.recvfrom(1024)
		content,frominfo = info
		print(">>[%s]:%s"%(frominfo,content.decode("gb2312")))

#2发数据
def send_data():
	while True:
		content = input(">>")
		dest = ("192.168.1.107",8081)
		udp_socket.sendto(content.encode("gb2312"),dest)

udp_socket = None

def main():
	global udp_socket
	udp_socket = socket(AF_INET,SOCK_DGRAM)

	tr = Thread(target=recv_data)
	ts = Thread(target=send_data)
	tr.start()
	ts.start()
	tr.join()
	ts.join()

if __name__ == '__main__':
		main()	