const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = merge(common, {
  mode: "production",
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "docs"), // 배포용 폴더
    publicPath: "/", // GitHub Pages용 publicPath 설정
  },
  plugins: [
    new CopyWebpackPlugin({
      patterns: [{ from: "public/data.json", to: "data.json" }], // ✅ data.json 복사
    }),
  ],
  optimization: {
    minimize: true, // 코드 최적화
  },
});
