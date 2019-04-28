let express = require('express')
let app = express()

const PORT = 3000

app.get('/', (req, res) => {
    res.send('Hello World\n')
})

app.listen(PORT, () => {
    console.log(`Running on port ${PORT}.`)
})
