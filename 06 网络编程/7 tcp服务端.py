from socket import *

def main():
	tcp_server_socket = socket(AF_INET,SOCK_STREAM)
	tcp_server_socket.bind(("192.168.1.107",8080))
	tcp_server_socket.listen(5)
	'''
	如果有新的客户端来链接服务器，创建新的套接字专⻔为这个客户端服务器 
	client_socker⽤来为这个客户端服务 
	tcp_server_socket就可以省下来专⻔等待其他新客户端的链接
	'''
	new_client_socket, new_client_addr = tcp_server_socket.accept()
	#接收对方发来的信息 最大字节数1024 堵塞
	receive_data = new_client_socket.recv(1024)

	print("[%s]:[%s]"%(str(new_client_addr),receive_data.decode("gb2312")))

	#关闭客户端套接字，不再为该客户服务
	new_client_socket.close()
	#关闭服务端套接字，服务端不能再为其他客户服务
	tcp_server_socket.close()

if __name__ == '__main__':
	main()