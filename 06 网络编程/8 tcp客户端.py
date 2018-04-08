from socket import *

def main():
	tcp_client_socket = socket(AF_INET,SOCK_STREAM)
	tcp_client_socket.connect(("192.168.1.107",8080))

	content = "你好啊"
	#发送数据时没必要填写ip和端口，因为前面已经连接好
	tcp_client_socket.send(content.encode("gb2312"))

	#客户端的返回信息
	recv_data = tcp_client_socket.recv(1024)
	print(recv_data.decode("gb2312"))

	tcp_client_socket.close()

if __name__ == '__main__':
	main()