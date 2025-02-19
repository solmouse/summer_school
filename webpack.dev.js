const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
const path = require("path");

module.exports = merge(common, {
  mode: "development",
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"), // 개발 모드에서는 dist 폴더 사용
    publicPath: "/", // 개발 환경에서는 루트 경로 사용
  },
  devServer: {
    static: {
      directory: path.resolve(__dirname, "public"),
    },
    devMiddleware: {
      publicPath: "/",
    },
    host: "0.0.0.0",
    port: 3000,
    open: true,
    allowedHosts: "all",
  },
  devtool: "inline-source-map", // 디버깅을 위한 source map 활성화
});
