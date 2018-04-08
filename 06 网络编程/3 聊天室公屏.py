from socket import *

def main():
	udpsocket = socket(AF_INET,SOCK_DGRAM)
	addr = ("",15789)
	udpsocket.bind(addr)

	while True:
		recv_data = udpsocket.recvfrom(1024) #recvfrom是关键字
		content,destinfo = recv_data
		print("[%s]:[%s]"%(destinfo,content.decode("gb2312")))

if __name__ == '__main__':
	main()