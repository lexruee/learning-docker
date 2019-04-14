const http = require("http"),
    os = require("os");

http.createServer((reg, res) => {
    const dateTime = new Date(),
        load = os.loadavg(),
        doc = `<DOCTYPE html>
        <html>
        <head>
            <title>Hello World Node</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Hello World Node!</h1>
            <ul>
                <li>Server time: ${dateTime} </li>
                <li>Server load: ${load[0]} </li>
            </ul>
        </body>
        </html>`
    res.setHeader('Content-Type', 'text/html');
    res.end(doc);
}).listen(8080);
