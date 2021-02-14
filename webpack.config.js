const path = require('path');
const {
    CleanWebpackPlugin
} = require('clean-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');

module.exports = {
    entry: './wedding/frontend/src/index.js',
    module: {
        rules: [{
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: ['babel-loader'],
        }, ],
    },
    resolve: {
        extensions: ['*', '.js', '.jsx'],
    },
    plugins: [
        new CleanWebpackPlugin(), // removes outdated assets from the output dir
        new ManifestPlugin(), // generates the required manifest.json file
    ],
    output: {
        filename: '[name].[contenthash].js', // renames files from example.js to example.8f77someHash8adfa.js
        path: path.resolve(__dirname, 'wedding/jsdist'),
    },
};