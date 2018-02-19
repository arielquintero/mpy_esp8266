/* Add header library */
const express = require('express')
const app = express()
const bodyParser = require('body-parser')

/* Init bodyParser */
app.use(bodyParser.urlencoded({
	extended: false
}));
app.use(bodyParser.json());

/* Init CORS */
app.use(function(req, res, next) {
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Methods", "GET");
	res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
	next();
});
app.use(express.static('./Public'))

const servers = app.listen(process.env.PORT || 3000, function() {
	var host = servers.address().address;
	var port = servers.address().port;
	console.log("App run at http://%s:%s", host, port);
})

var apps = require('./routing.js')
apps.startRoute(app);
