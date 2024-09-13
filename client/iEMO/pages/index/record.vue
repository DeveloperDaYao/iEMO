<template>
	<view>
		<button @tap="startRecord">开始录音</button>
		<button @tap="endRecord">停止录音</button>
		<button @tap="playVoice">播放录音</button>
	</view>
</template>

<script>
	const recorderManager = uni.getRecorderManager();
	const innerAudioContext = uni.createInnerAudioContext();
	
	innerAudioContext.autoplay = true;
	
	export default {
		data() {
			return {
				text: 'uni-app',
				voicePath: ''
			}
		},
		onLoad() {
			let self = this;
			recorderManager.onStop(function (res) {
				console.log('recorder stop' + JSON.stringify(res));
				self.voicePath = res.tempFilePath;
			});
		},
		methods: {
			startRecord() {
				console.log('开始录音');
	
				recorderManager.start();
			},
			endRecord() {
				console.log('录音结束');
				recorderManager.stop();
			},
			playVoice() {
				console.log('播放录音');
	
				if (this.voicePath) {
					innerAudioContext.src = this.voicePath;
					innerAudioContext.play();
				}
			}
		}
	}

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