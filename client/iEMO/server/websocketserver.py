import asyncio
import websockets

class WebSocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None

    async def handle_client(self, websocket, path):
        async for message in websocket:
            await self.process_message(websocket, message)

    async def process_message(self, websocket, message):
        # 在这里处理收到的消息，这里只是简单地将消息发送回客户端
        await websocket.send(message+'。end')

    async def start(self):
        self.server = await websockets.serve(self.handle_client, self.host, self.port)
        print(f"WebSocket server started at ws://{self.host}:{self.port}")
        await self.server.wait_closed()

    def stop(self):
        if self.server:
            self.server.close()

# 使用示例
if __name__ == "__main__":
    server = WebSocketServer("192.168.2.59", 8888)
    asyncio.get_event_loop().run_until_complete(server.start())
