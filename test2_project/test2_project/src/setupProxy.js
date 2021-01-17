const proxy = require('http-proxy-middleware')

module.exports = app => {
    app.use(
        '/api1',
        proxy({
            target: 'http://back:8000',
            changeOrigin: true,
            // pathRewrite: { '^/api1': '' }
        })
    )
}