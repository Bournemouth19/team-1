from flask import Flask, request, render_template
app = Flask(__name__)

import os
import codecs

@app.route("/")
def hello():
	return render_template('index.html')
	
	
@app.route("/LocationPages/<name>")
def search(name):
	path = '/LocationPages/'
	if name == 'Cafe.html':
		return render_template(path + 'Cafe.html')
	elif name == 'games_room.html':
		return render_template(path + 'games_room.html')
	elif name == 'hall.html':
		return render_template(path + 'hall.html')
	elif name == 'outside.html':
		return render_template(path + 'outside.html')
	elif name == 'pc_repair_room.html':
		return render_template(path + 'pc_repair_room.html')
	

	
if __name__ == "__main__":
    app.run()
	#print(readHTML('index.html'))