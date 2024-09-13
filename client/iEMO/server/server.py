import socket
import threading
 
def handle_client(client_socket):
    data = client_socket.recv(1024)  # 接收客户端的数据
    response = "Hello, client!"  # 生成响应数据
    client_socket.send(response.encode())  # 发送响应数据给客户端
    client_socket.close()  # 关闭客户端连接
 
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务器套接字
    server_socket.bind(('192.168.2.59', 8888))  # 绑定服务器地址和端口
    server_socket.listen(5)  # 等待客户端连接的队列长度为5
    print("Server started, listening on port 8888...")
 
    while True:
        client_socket, client_address = server_socket.accept()  # 等待客户端连接
        print(f"Accept connection from {client_address[0]}:{client_address[1]}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()  # 使用线程处理客户端请求
 
run_server()