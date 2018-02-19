const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')
const adapter = new FileSync('db.json')
const db = low(adapter)

db.defaults({
		setup_time: 10000
	})
	.write();

module.exports = {
	getSetup: function(done) {
		const tm = db
			.get("setup_time")
			.value()
		done({
			setup_time: tm
		})
	},
	postSetup: function(data, done) {
		console.log(data)
		db.set("setup_time", parseInt(data))
			.write()
		done({
			status: true
		})
	}
}
