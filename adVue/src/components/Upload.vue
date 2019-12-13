<template lang="pug">
  div
    el-row(:gutter="2")
      el-col(:span="10")
        el-form(:model="form" :rules="rules" ref="ruleForm" label-width="100px" :hide-required-asterisk="true")
          el-form-item(label="用户信息" prop="scores")
            el-upload(class="upload" ref="fileUpload" drag action="/" :on-change="importExcel" :on-exceed="onFileExceed" :on-remove="onFileRemove" :auto-upload="false" :limit="1")
              i.el-icon-upload
              .el-upload__text 将文件拖到此处，或<em>点击上传</em>
              .el-upload__tip(slot="tip") 上传 Excel 表格文件。
          el-form-item
            el-button(type="primary" @click="onSubmit('ruleForm')") 提交
            el-button(@click="onCancel()") 取消
      //- el-col.data-preview(:span="12" v-if="form.scores.length")
      //-   .tips 
      //-     i.el-icon-view
      //-     span 待上传的数据（{{form.scores.length}}条）
      //-   el-table(:data="form.scores" max-height="10000")
      //-     el-table-column(label="酒店名称" prop="酒店名称" width="80px")
      //-     el-table-column(label="用户" prop="用户" width="60px")
      //-     el-table-column(label="等级" prop="等级" width="60px")
      //-     el-table-column(label="入住时间" prop="入住时间" width="60px")
      //-     el-table-column(label="评价时间" prop="评价时间" width="60px")
      //-     el-table-column(label="出差类型" prop="出差类型" width="60px")
      //-     el-table-column(label="房型" prop="房型" width="70px")
      //-     el-table-column(label="位置" prop="位置" width="50px")
      //-     el-table-column(label="设施" prop="设施" width="50px")
      //-     el-table-column(label="服务" prop="服务" width="50px")
      //-     el-table-column(label="卫生" prop="卫生" width="50px")
      //-     el-table-column(label="评价" prop="评价" width="300px")
</template>

<script>
import XLSX from "xlsx";
export default {
  data() {
    return {
      form: {
        scores: []
      },
      rules: {
        scores: [
          {
            type: "array",
            required: true,
            min: 1,
            message: "请上传分数数据",
            trigger: "change"
          }
        ]
      }
    };
  },

  methods: {
    onSubmit() {
      var that = this;
      that.$refs["ruleForm"].validate(valid => {
        if (valid) {
          that
            .$confirm("确定提交吗？", "提示", {
              confirmButtonText: "确定",
              cancelButtonText: "取消",
              type: "warning",
              center: true
            })
            .then(function() {
              that.$http
                .post("http://127.0.0.1:5000/upload", that.form)
                .then(function(result) {
                  console.log(result);
                  that.$router.push("/Bar3d");
                  that.$message({
                    type: "success",
                    message: "上传成功!"
                  });
                });
            })
            .catch(() => {});
        } else {
          return false;
        }
      });
    },
    onCancel() {
      this.$confirm("您编辑的内容尚未上传，确定取消吗？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "继续编辑",
        type: "warning",
        center: true
      })
        .then(() => {
          this.$refs["fileUpload"].clearFiles();
          this.form.scores = [];
        })
        .catch(() => {});
    },
    onFileExceed() {
      this.$message.error("上传文件超出数量限制！");
    },
    onFileRemove() {
      this.$refs["fileUpload"].clearFiles();
      this.form.scores = [];
    },
    importExcel(file) {
      const types = file.name.split(".")[1];
      const fileType = ["xlsx", "xlc", "xlm", "xls", "xlt", "xlw", "csv"].some(
        item => item === types
      );
      if (!fileType) {
        this.$message.error("格式错误！请重新选择！");
        this.form.scores = [];
        this.$refs["fileUpload"].clearFiles();
        return;
      }
      this.file2Xce(file).then(tabJson => {
        if (tabJson && tabJson.length > 0) {
          this.form.scores = tabJson[0].sheet;
          this.$refs["ruleForm"].validateField(["scores"]);
        }
      });
    },
    file2Xce(file) {
      return new Promise(function(resolve, reject) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const data = e.target.result;
          this.wb = XLSX.read(data, {
            type: "binary"
          });
          const result = [];
          this.wb.SheetNames.forEach(sheetName => {
            result.push({
              sheetName: sheetName,
              sheet: XLSX.utils.sheet_to_json(this.wb.Sheets[sheetName])
            });
          });
          resolve(result);
        };
        reader.readAsBinaryString(file.raw);
      });
    }
  }
};
</script>

<style>
.upload {
  width: 300px;
}
.data-preview {
  padding: 10px;
  background-color: #f9f9f9;
}
.data-preview .tips {
  margin: 8px 4px 12px;
  color: #909399;
  font-size: 16px;
}
.data-preview .tips span {
  margin-left: 4px;
  font-size: 14px;
}
</style>
