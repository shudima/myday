var express = require('express');
var mongoose = require('mongoose');
var app = express();

mongoose.connect('mongodb://admin:admin@ds031691.mongolab.com:31691/shudima');

mongoose.model('analyzed_texts', { sign : String, sentiment: String})
app.get('/daily/:sign', function(req, res) { 

	mongoose.model('analyzed_texts').find({sign : req.params.sign },function(err, analysis) {
		res.send(analysis);
	});
});

app.listen(7000);