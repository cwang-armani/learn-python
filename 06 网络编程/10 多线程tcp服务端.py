from socket import *
from threading import Thread

def handel_client(tcp_client_socket,tcp_client_addr):
	while True:
		recv_data = tcp_client_socket.recv(1024)
		if len(recv_data)>0:
			print("[%s]:%s"%(str(tcp_client_addr),recv_data.decode("gb2312")))
		else:
			print("[%s]已经关闭客户端"%str(tcp_client_addr))
			break
	tcp_client_socket.close()

def main():
	tcp_server_socket = socket(AF_INET,SOCK_STREAM)
	local_addr = ("192.168.1.107",8080)
	tcp_server_socket.bind(local_addr)
	tcp_server_socket.listen(5)

	while True:
		#3次握手已经建立后，执行本行代码
		#accept与while循环一同调用容易出现异常
		tcp_client_socket,tcp_client_addr = tcp_server_socket.accept()
		print("一位新用户到来：%s"%str(tcp_client_addr))
		p = Thread(target=handel_client,args=(tcp_client_socket,tcp_client_addr))
		p.start()
		#因为线程中共享这个套接字，如果关闭了会导致这个套接字不可⽤
		#但是此时在线程中这个套接字可能还在收数据，因此不能关闭	
		#tcp_client)socket.close()

	tcp_server_socket.close()

if __name__ == '__main__':
	main()