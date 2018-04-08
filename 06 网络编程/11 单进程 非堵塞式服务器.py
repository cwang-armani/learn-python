from socket import *

def main():
	tcp_server_socket = socket(AF_INET,SOCK_STREAM)
	local_addr = ("192.168.1.107",8080)
	tcp_server_socket.bind(local_addr)
	tcp_server_socket.setblocking(False)
	#设置为⾮堵塞后，如果accept时，恰巧没有客户端connect，那么accept会，产⽣⼀个异常，所以需要try来进⾏处理
	tcp_server_socket.listen(5)

	new_client_list = []
	while True:
		# 调用accept之前没有客户端到来会产生异常
		# 检测是否有新用户到来，若有，存入列表并打印
		try:
			tcp_client_socket,tcp_client_addr = tcp_server_socket.accept()
		except:
			pass
		else:
			print("一位新用户到来：%s"%str(tcp_client_addr))
			tcp_client_socket.setblocking(False)
			new_client_list.append((tcp_client_socket,tcp_client_addr))

		# 遍历列表，检测是否收到每个客户端的新消息
		for tcp_client_socket,tcp_client_addr in new_client_list:
			try:
				#没有数据同样会产生异常
				recv_data = tcp_client_socket.recv(1024)
			except:
				pass
			else:
				if len(recv_data)>0:
					print("[%s]:%s"%(str(tcp_client_addr),recv_data.decode("gb2312")))
				else:
					new_client_list.remove((tcp_client_socket,tcp_client_addr))
					print("[%s]已经下线了....")
					break

if __name__ == '__main__':
	main()

#单进程非堵塞式服务器需要一直运行，理解思想