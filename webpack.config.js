var path = require("path");
var webpack = require('webpack');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const CopyPlugin = require("copy-webpack-plugin");

module.exports = [{
    devtool: 'inline-source-map',
    entry: {
        'react/testApp': __dirname + '/swift_parsing_app/react_apps/TestApp.js',
        'js/bundle': __dirname + '/assets/js/master.js',
        'css/master': __dirname + '/assets/scss/master.scss',
    }
    ,  // path to our input file
    output: {
        filename: '[name].js',  // output bundle file name
        path: path.resolve(__dirname, './static'),  // path to our Django static directory
    },
    // optimization: {
    //     minimize: true,
    // },
    module: {
        rules: [
            {
                test: /[Aa]pp.js/,
                // exclude: /node_modules/,
                use: [

                    {
                        loader: "babel-loader",
                        options: {presets: ["@babel/preset-env", "@babel/preset-react"]}
                    },
                    // {
                    //     loader: 'file-loader',
                    //     options: {
                    //         outputPath: path.resolve(__dirname, './static/react'),
                    //         name: '[name].js'
                    //     }
                    //
                    // }

                ]

            },
            {
                test: /\.(js|jsx)$/,
                // exclude: /node_modules/,
                use: [
                    // {
                    //     loader: 'file-loader',
                    //     options: {outputPath: './js', name: '[name].[ext]',
                    //         esModule: false}
                    // },
                    {
                        loader: "babel-loader",
                        options: {presets: ["@babel/preset-env"]}
                    }
                ]

            },
            {
                // test: /\.scss$/,
                // // exclude: /node_modules/,
                // use: [
                //     {
                //         loader: 'file-loader',
                //         options: {outputPath: path.resolve(__dirname, './static/css'), name: '[name].min.css'}
                //     }, {
                //         loader: "style-loader"
                //     },
                //     // Add browser prefixes and minify CSS.
                //     {loader: 'postcss-loader', options: {sourceMap: true, plugins: [autoprefixer(), cssnano()]}},
                //     {
                //         loader: "sass-loader", options: {
                //             sourceMap: true
                //         }
                //     }

                // ]
                test: /\.scss$/,
                // exclude: /node_modules/,
                use: [
                    // {
                    //     loader: 'file-loader',
                    //     options: {outputPath: path.resolve(__dirname, './static/css'), name: '[name].min.css'}
                    // },
                    {
                        loader: MiniCssExtractPlugin.loader,
                    },
                    // Add browser prefixes and minify CSS.
                    {
                        loader: 'css-loader',
                        options: {
                            url: false, sourceMap: true
                        }
                    },
                    {loader: 'postcss-loader', options: {sourceMap: true, plugins: [autoprefixer(), cssnano()]}},
                    {
                        loader: "sass-loader", options: {
                            sourceMap: true
                        }
                    }
                ]
            }
        ]
    },
    devServer: {
        writeToDisk: true,
    },
    plugins: [
        new CleanWebpackPlugin(
            {
                // cleanAfterEveryBuildPatterns: ['./*.js'],
            }
        ),
        new MiniCssExtractPlugin({
            linkType: 'text/css',
        }),
        new CopyPlugin({
            patterns: [
                {from: "assets/fonts", to: path.resolve(__dirname, './static/fonts'), noErrorOnMissing: true},
                {
                    from: './node_modules/@fortawesome/fontawesome-free/webfonts',
                    to: path.resolve(__dirname, './static/fonts'),
                    noErrorOnMissing: true
                },
                {from: "assets/img", to: path.resolve(__dirname, './static/img'), noErrorOnMissing: true},
            ],
            options: {
                concurrency: 100,
            },
        }),
    ],
    mode: "development"
}];