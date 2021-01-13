const proxy = require('http-proxy-middleware')

module.exports = app => {
    app.use(
        '/api1',
        proxy({
            target: 'http://172.16.238.4:8000',
            changeOrigin: true,
            // pathRewrite: { '^/api1': '' }
        })
    )
}