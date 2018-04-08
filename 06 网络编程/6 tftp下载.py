# -*- coding:utf-8 -*-
from socket import *
import struct
def main():
	# 下载文件名 
	download_filename = "test_picture.png"
	# 创建socket
	udp_socket = socket(AF_INET,SOCK_DGRAM)
	# 向服务端发送请求
	send_addr = ("192.168.1.107",69)
	request_data = struct.pack("!H%dsb5sb"%len(download_filename),1,b"test_picture.png",0,b"octet",0)
	udp_socket.sendto(request_data,(send_addr))
	
	f.open = ("download_filename","w")
	num = 0
	flag = True
	
	while True:
		# 接收服务端返回的数据
		response_data = udp_socket.recvfrom(1024)
		receive_data,sever_info = response_data

		option_num = struct.unpack("!H",receive_data[:2])
		block_num = struct.unpack("!H",receive_data[2:4])


		#print(option_num)
		#print(block_num)
		if option_num[0] = 3
			num += 1

			if num == 65535:
				num = 0

			if num == block_num[0]
				#收到的数据写到文件中
				f.write(receive_data[4:])
				num = block_num[0]

		
		ACK_data = struct.pack("!HH",4,block_num[0])
		udp_socket.sendto(ACK_data,sever_info)

		
		if option_num[0] = 5
			print("无法找到该文件")
			flag = False

		if len(receive_data)<516:
			break

	if flag == True:
		f.close()
	else:
	os.unlink(downloadFileName)#如果没有要下载的文件，那么就需要把刚刚创建的文件进行删除

if __name__ == '__main__':
	main()