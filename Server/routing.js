/* Get db module object */
const db = require('./db.js')

module.exports = {
	startRoute: function(app) {
		// ROUTING
		app.get('/', function(req, res) {
			db.getSetup(function(result) {
				res.json(JSON.stringify(result))
			})
		})

		app.get('/setup', function(req, res) {
			db.postSetup(req.query.setup, function(result) {
				res.json(JSON.stringify(result))
			})
		})
	}
}
