var  http = require('http')

var server = http.createServer(function (request, response) { 

	response.writeHead(200);
	response.end("Dima2");

});


server.listen(7000);