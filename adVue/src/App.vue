<template lang="pug">
  el-container(direction="horizontal" id="menu")
    el-aside(width="220px" v-if="this.$route.name != 'upload'")
      navMenu
    el-container(direction="vertical")
      el-main
        router-view
</template>

<script>
import navMenu from "./components/NavMenu";
export default {
  name: "App",
  components: {
    navMenu
  },
  data() {
    return {};
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
