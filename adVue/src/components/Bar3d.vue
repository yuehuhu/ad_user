<template>
  <div id="Loading">
    <div class="loader-inner ball-beat" v-show="ballState">
      <div></div>
      <div></div>
      <div></div>
    </div>

    <div class="img" v-show="imgState">
      <div>
        <iframe
          src="./static/htmls/index.html"
          width="1000"
          height="650"
          frameborder="0"
          scrolling="auto"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "hello",
  data() {
    return {
      ballState: true,
      imgState: false
    };
  },
  mounted() {
    var that = this;
    (that.imgState = true), (that.ballState = false);
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