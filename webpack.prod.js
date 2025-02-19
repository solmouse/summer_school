const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
const path = require("path");

module.exports = merge(common, {
  mode: "production",
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "docs"),
    publicPath: "./", // ✅ 상대 경로 사용
  },
  optimization: {
    minimize: true,
  },
});
