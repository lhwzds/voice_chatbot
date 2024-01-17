const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      '/local':{
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/local': ''
        }
      }
    }
  }
})
