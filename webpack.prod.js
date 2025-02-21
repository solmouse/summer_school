const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
const path = require("path");

module.exports = merge(common, {
  mode: "production",
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "docs"), // 배포용 폴더
    publicPath: "/summer_school/", // GitHub Pages용 publicPath 설정 (github의 url)
  },
  optimization: {
    minimize: true, // 코드 최적화
  },
});
