# iEMO 服务端程序

服务端程序。



## ✅待办

- [ ] 串连组合各模块，并可随时替换新的。具备可插拔性。
- [ ] 维护每台终端机状态，可控制表情序列下达至终端。
- [ ] 记录对话历史。数据的统计与分析。


## 📂模块约定
```
└─module
    ├─auditory //音频识别模块（ASR）。in：语音 -> out：文本
    ├─brain //语义处理模块（LLM）。in：文本 -> out：回复文本
    └─speak //音频合成模块（TTS）。in：回复文本 -> out：合成语音
```

## 启动socket服务端
运行`server`目录下的脚本后打印表示服务端socket通道创建完毕。
```
python websocketserver.py
```
```
WebSocket server started at ws://192.168.2.59:8888
```

