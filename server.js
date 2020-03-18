var http = require('http');
var url = require('url');
var fs = require('fs');
var path = require('path');
const hostname = "127.0.0.1";

var port = 8080;

console.log("Starting server on port " + port);

http.createServer(function (req, res) {
  if(url.parse(req.url, true).pathname == '/exit') {
    process.exit();
  }else if(url.parse(req.url, true).pathname == '/') {
    req.url = "/final.html";
  }
  
  var q = url.parse(req.url, true);
  var filename = "." + q.pathname;
  var content_type = 'text/html';
  
  if(q.pathname.endsWith('.css')) {
	  content_type = 'text/css';
  }
  
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    }
	
    res.writeHead(200, {'Content-Type': content_type});
    res.write(data);
    return res.end();
  });
}).listen(port);