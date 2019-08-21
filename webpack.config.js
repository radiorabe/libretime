var glob = require("glob");

module.exports = {
  mode: 'development',
  context: __dirname + "/ui",
  entry: glob.sync(__dirname + "/ui/src/css/**/*.css"),
  output: {
    path: __dirname + "/airtime_mvc/public/",
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        loader: 'style-loader',
      },
      {
        test: /\.css$/i,
        loader: 'css-loader',
        options: {
          modules: false,
        },
      },
      {
        test: /\.(png|jpe?g|gif|svg|eot|ttf|woff|woff2)$/i,
        loader: 'url-loader',
        options: {
          name: "ui/[contenthash].[ext]",
          limit: 8192,
        },
      },
    ],
  },
};
