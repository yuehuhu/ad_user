<template>
  <div id="Loading">
    <div class="loader-inner ball-beat" v-show="ballState">
      <div></div>
      <div></div>
      <div></div>
    </div>
    <div class="img" v-show="imgState">
      <img :src="imgUrl" width="500px" height="500px">
      <el-input v-show="boxState" v-model="input" placeholder="请输入内容"></el-input>

      <br>
      <el-button
        style="padding:10px"
        type="primary"
        :loading="buttonState"
        @click="onSubmit()"
        v-show="submitState"
      >分析</el-button>

      <span v-show="spanState">{{spanText}}</span>
      <br>
      <br>

      <el-button type="primary" @click="onCancel()" v-show="cancelState">返回</el-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      imgState: false,
      ballState: true,
      boxState: true,
      buttonState: false,
      submitState: true,
      spanState: false,
      cancelState: false,
      imgUrl: null,
      input: "前台",
      flag: 0,
      spanText: ""
    };
  },
  methods: {
    onResult(data) {
      var that = this;
      that.spanText = "关于服务做的很棒哦，请继续保持~~~"
      // that.spanText = data[0];
    },
    onSubmit() {
      var that = this;
      that.buttonState = true;
      that.$http
        .post("http://127.0.0.1:5000/nlp", that.input)
        .then(function(result) {
          console.log(result);
          that.imgUrl = "../../static/imgs/nlp.png?t=" + new Date().getTime();
          that.buttonState = false;
          that.boxState = false;
          that.submitState = false;
          that.spanState = true;
          that.cancelState = true;
          that.onResult(result.data);
        });
    },
    onCancel() {
      var that = this;
      that.imgUrl = "../../static/imgs/wordcloud.png?t=" + new Date().getTime();
      that.submitState = true;
      that.cancelState = false;
      that.boxState = true;
      that.spanState = false;
    }
  },
  mounted() {
    var that = this;
    that.imgUrl = "../../static/imgs/wordcloud.png?t=" + new Date().getTime();
    that.imgState = true;
    that.ballState = false;
  }
};
</script>

<style type="text/css">
#Loading {
  top: 50%;
  left: 50%;
  position: absolute;
  -webkit-transform: translateY(-50%) translateX(-50%);
  transform: translateY(-50%) translateX(-50%);
  z-index: 100;
}
@-webkit-keyframes ball-beat {
  50% {
    opacity: 0.2;
    -webkit-transform: scale(0.75);
    transform: scale(0.75);
  }

  100% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

@keyframes ball-beat {
  50% {
    opacity: 0.2;
    -webkit-transform: scale(0.75);
    transform: scale(0.75);
  }

  100% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

.ball-beat > div {
  background-color: #279fcf;
  width: 15px;
  height: 15px;
  border-radius: 100% !important;
  margin: 2px;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  display: inline-block;
  -webkit-animation: ball-beat 0.7s 0s infinite linear;
  animation: ball-beat 0.7s 0s infinite linear;
}
.ball-beat > div:nth-child(2n-1) {
  -webkit-animation-delay: 0.35s !important;
  animation-delay: 0.35s !important;
}
</style>