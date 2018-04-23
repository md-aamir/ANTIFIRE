#!/usr/bin/env python
# built by SYNTAX ERROR	

from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3
def fetchdata():
	conn=sqlite3.connect('sensorsData.db')
	curs=conn.cursor()

	for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		smoke = row[2]
	conn.close()
	return time, temp, smoke

# main route 
@app.route("/")
def index():
	
	time, temp, smoke = fetchdata()
	templateData = {
	  'time'	: time,
          'temp'	: temp,
          'smoke'	: smoke
	}
	return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='192.168.43.196', port=80, debug=False)