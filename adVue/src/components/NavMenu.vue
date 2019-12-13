<template lang="pug">
  el-menu(:default-active="$route.meta.navIndex" router background-color="#f6f6f6" text-color="#909399" active-text-color="#303133")
    el-menu-item(v-for="(item,i) in navList" :key="i" :index="item.name")
      i.iconfont(:class="item.icon")
      span(slot="title") {{ item.navItem }}
</template>

<style>
.el-menu {
  border: none !important;
  height: calc(100vh - 545px);
}
.el-menu-item {
  border-left: 3px solid transparent;
}
.el-menu-item:focus,
.el-menu-item:hover {
  outline: 0;
  background-color: #eeeeee !important;
}
.el-menu-item.is-active {
  background-color: #eeeeee !important;
  border-left: 5px solid #fcbb42;
}
.el-menu-item .iconfont {
  margin-right: 10px;
  font-size: 15px;
}
</style>

<script>
export default {
  data() {
    return {
      navList: [
        {
          name: "/upload",
          navItem: "退出",
          icon: "icon-repeal_icon"
        }
      ]
    };
  }
};
</script>