<template>
	<view>
		<button @tap="startRecord">开始录音</button>
		<button @tap="endRecord">停止录音</button>
		<button @tap="playVoice">播放录音</button>
	</view>
</template>

<script>
	
	// 以下路径需根据项目实际情况填写
	// import socket from '../../js_/plus-websocket/index.js'
	
	const recorderManager = uni.getRecorderManager();
	const innerAudioContext = uni.createInnerAudioContext();
	
	innerAudioContext.autoplay = true;
	
	
	
	
	export default {
	  data() {
	    return {
	      socketOpen: false,
	      socketMsg: ""
	    };
	  },
	  onUnload() {
	    this.closeSocket();
	  },
	  methods: {
		  
	    createSocket() {
	      uni.connectSocket({
	        url: 'ws://192.168.2.59:8888/', // 你的TCP服务器地址
		
			// header: {
			// 		'content-type': 'application/json'
			// 	},
			// protocols: ['protocol1'],
			// method: 'GET'
			complete: ()=> {}
	      });
	 
	      uni.onSocketOpen((res) => {
			  
	        this.socketOpen = true;
	        console.log('WebSocket连接已打开！', res);
	      });
	 
	      uni.onSocketError((err,e) => {
	        console.error('WebSocket连接打开失败，请检查服务器URL！', err);
	      });
	 
	      uni.onSocketMessage((res) => {
	        console.log('收到服务器内容：', res.data);
	        this.socketMsg = res.data;
	      });
	 
	      uni.onSocketClose((res) => {
	        this.socketOpen = false;
	        console.log('WebSocket已关闭！', res);
	      });
	    },
	    closeSocket() {
	      if (this.socketOpen) {
	        uni.closeSocket();
	      }
	    },
	    sendSocketMessage(msg) {
	      if (this.socketOpen) {
	        uni.sendSocketMessage({
	          data: msg,
	          success: function (res) {
	            console.log('发送数据成功', res);
	          },
	          fail: function (err) {
	            console.error('发送数据失败', err);
	          }
	        });
	      }
	    }
	  },
	  mounted() {
	    this.createSocket();
	  }
	};

</script>

<style>
	@font-face {
	  font-family: 'iconfont';
	  src: url('~@/static/iconfont.ttf') format('truetype');
	  /* src: url('http://localhost:5173/iconfont.ttf?t=1723789495389') format('truetype'); */
	}
	.iconfont {
	  font-family: "iconfont" !important;
	  font-size: 40px;
	  font-style: normal;
	  -webkit-font-smoothing: antialiased;
	  -moz-osx-font-smoothing: grayscale;
	}
	
	
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100%;
		background-color: black;
	}

	.emoji-wrap {
		background-color: black;
		height: 79%;
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.status-tip{
		height: 1%;
		width: 100%;
		background-color: gainsboro;
		text-align: center;
		color: white;
		font-size: 1.5em;
		font-weight: bold;
	}
	.instruct-wrap{
		height: 20%;
		width: 100%;
		background-color: lightgray;
		text-align: center;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.microphone{
		/* font-size: 80px; */
		border: 0px solid red;
		/* padding: 40px; */
		background-color: white;
		width: 100px;
		height: 100px;
		line-height: 100px;
		border-radius: 50px;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>