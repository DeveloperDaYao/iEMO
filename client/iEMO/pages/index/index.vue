<template>
	<view class="content">
		<view class="emoji-wrap">
			<video :src="encodeURI(currentEmoji.src)" autoplay="true" :loop="loop" :controls="false" object-fit="fill" muted
				id="videocc" ref="video"
				type="video/mp4"
				:show-play-btn="false" :show-center-play-btn="true" :show-loading="false" @ended="onVideoEnd"
				@play="cc" style="border: 0px solid red;width: 450px;height: 430px">
			</video>
			<view style="color:white;font-size: 1.5em;font-weight: bold;padding-bottom: 20px;">
				<text v-if="socketOpen" class="iconfont" style="color: green;font-size: 24px;">&#xe7e0;</text>
				<text v-if="!socketOpen" class="iconfont" style="color: red;font-size: 24px;">&#xe71d;</text>
				
			<text v-if="!listen" class="iconfont" style="color: white;font-size: 24px;">&#xe60b;</text>
			<text v-if="listen" class="iconfont" style="color: white;font-size: 24px;">&#xe614;</text>
			<text v-if="!listen && statusTip" class="iconfont" style="color: white;font-size: 24px;">&#xe861;</text>
			{{statusTip}}
			</view>
		</view>
		<view class="status-tip"><!-- 思考中... --></view>
		<view class="instruct-wrap">
			<!-- <button>按住 说话</button> -->
			<view class="microphone" @touchstart="microphoneDown()" @touchend="microphoneUp()">
				<text v-if="!listen" class="iconfont">&#xf0147;</text>
				<text v-if="listen" class="iconfont">&#xe6a3;</text>
			</view>
			<!-- <input class="uni-input" focus placeholder="自动获得焦点" /> -->
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				emojiList: [],
				currentIndex: 0,
				currentEmoji: null,
				loop: false,
				timer: null,
				statusTip:'',
				listen:false,
				
				socketOpen: false,
				socketMsg: "",

				emoji: {
					angry: [{
							src: '../../static/Emoji/angry/angry_in.mp4'
						},
						{
							src: '../../static/Emoji/angry/angry_loop.mp4'
						},
						{
							src: '../../static/Emoji/angry/angry_out.mp4'
						},
					],
					disdain: [{
							src: '../../static/Emoji/disdain/disdain_in.mp4'
						},
						{
							src: '../../static/Emoji/disdain/disdain_loop.mp4'
						},
						{
							src: '../../static/Emoji/disdain/disdain_out.mp4'
						},
					],
					fear: [{
							src: '../../static/Emoji/fear/fear_in.mp4'
						},
						{
							src: '../../static/Emoji/fear/fear_loop.mp4'
						},
						{
							src: '../../static/Emoji/fear/fear_out.mp4'
						},
					],
					sad: [{
							src: '../../static/Emoji/sad/sad_in.mp4'
						},
						{
							src: '../../static/Emoji/sad/sad_loop.mp4'
						},
						{
							src: '../../static/Emoji/sad/sad_out.mp4'
						},
					],
					excite: [{
							src: '../../static/Emoji/excite/excite_in.mp4'
						},
						{
							src: '../../static/Emoji/excite/excite_loop.mp4'
						},
						{
							src: '../../static/Emoji/excite/excite_out.mp4'
						},
					],
					neutral: {
						right: [{
								src: '../../static/Emoji/neutral/right_top/right_top_in.mp4'
							},
							{
								src: '../../static/Emoji/neutral/right_top/right_top_loop.mp4'
							},
							{
								src: '../../static/Emoji/neutral/right_top/right_top_out.mp4'
							},
						],
						left: [{
								src: '../../static/Emoji/neutral/left_top/left_top_in.mp4'
							},
							{
								src: '../../static/Emoji/neutral/left_top/left_top_loop.mp4'
							},
							{
								src: '../../static/Emoji/neutral/left_top/left_top_out.mp4'
							},
						],
						once: [{
							src: '../../static/Emoji/neutral/once_blink.mp4'
						}, ],
						double: [{
							src: '../../static/Emoji/neutral/double_blink.mp4'
						}, ]
					}
				},
			}
		},
		onLoad() {},
		onUnload() {
		  this.closeSocket();
		},
		created() {
			this.startEmoji()
		},
		mounted() {
			// 当组件挂载完成后，进行自动播放
			// this.playVideo();
			// this.currentEmoji = this.emojiList[this.currentIndex];
			
			this.createSocket();
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
				  this.socketOpen = false;
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
			},
			
			
			 playVideo() {
			      // const videoContext = uni.createVideoContext('videocc', this);
			      // videoContext.play();
				  // this.$refs.video.play()
			    },
			microphoneDown(){
				this.listen=true
				this.statusTip='我在听...'
				this.loop = true
				this.setEndTime(5000)
				this.startEmoji(this.emoji.neutral.once)
				
				this.sendSocketMessage('地方大幅度发');
				
				console.log('microphoneDown')
			},
			microphoneUp(){
				this.listen=false
				this.statusTip='思考中...'
				this.loop = false
				this.setEndTime(5000)
				this.startEmoji(this.emoji.neutral.right)
				console.log('microphoneUp')
			},
			startEmoji(emoji) {
				console.log('======= start a round =======>');
				this.currentIndex = 0
				if(!emoji){
					emoji = this.randomEmoji()
				}
				console.log('start emoji:', emoji)

				this.emojiList = emoji
				this.currentEmoji = this.emojiList[this.currentIndex];
			},
			randomEmoji() {
				let describe = ['angry', 'disdain', 'fear', 'sad', 'excite', 'neutral']
				let r = Math.floor(Math.random() * 9) + 1
				// let r = 9
				console.log('random emoji index:', r)
				switch (r) {
					case 1:
						return this.emoji.angry
					case 2:
						return this.emoji.disdain
					case 3:
						return this.emoji.fear
					case 4:
						return this.emoji.sad
					case 5:
						return this.emoji.excite
					case 6:
						this.loop = true
						this.setEndTime(Math.floor(Math.random() * 1000))
						return this.emoji.neutral.right
					case 7:
						this.loop = true
						this.setEndTime(Math.floor(Math.random() * 1000))
						return this.emoji.neutral.left
					case 8:
						this.loop = true
						this.setEndTime(Math.floor(Math.random() * 2000))
						return this.emoji.neutral.once
					case 9:
						this.loop = true
						this.setEndTime(Math.floor(Math.random() * 1500))
						return this.emoji.neutral.double
				}
			},
			cc() {
				// console.log(33333333333333333)
			},
			onVideoEnd() {
				console.log('end count',this.currentIndex)
				this.currentIndex++;
				if (this.currentIndex < this.emojiList.length) {
					this.currentEmoji = this.emojiList[this.currentIndex];
				} else {
					console.log('emoji homed!');
					console.log('<======= ended =======');
					this.startEmoji()
				}

				if (1 === this.currentIndex) {
					this.loop = true
					this.setEndTime()
				}
			},

			setEndTime(duration) {
				if (!duration) {
					duration = Math.floor(Math.random() * 6) * 1000
				}
				console.log(`emoji duration: ${duration} ms`)
				this.timer = setTimeout(() => {
					this.loop = false
					clearTimeout(this.timer)
					console.log('emoji homing...');
				}, duration);
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