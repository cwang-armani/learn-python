from socket import *
from multiprocessing import Process

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
		tcp_client_socket,tcp_client_addr = tcp_server_socket.accept()
		print("一位新用户到来：%s"%str(tcp_client_addr))
		p = Process(target=handel_client,args=(tcp_client_socket,tcp_client_addr))
		p.start()
		#已经向子进程中copy了一份新客户端的引用，子进程继续运行，父进程套接字已经没有作用，故close
		tcp_client_socket.close()
	
	tcp_server_socket.close()

if __name__ == '__main__':
	main()

# 当客户端不是特别多的时候，这种⽅式还⾏，
# 如果有⼏百上千个，就不 可取了，因为每次创建进程等过程需要好较⼤的资源
