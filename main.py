from flask import Flask, request, send_from_directory
app = Flask(__name__)

import os
import codecs

@app.route("/")
def hello():
	return readHTML('index.html')


@app.route("/search/<name>")
def search(name):
	path = 'LocationPages/'
	if name in 'Cafe Area':
		return readHTML(path + 'cafe.html')
	elif name in 'Game Room':
		return readHTML(path + 'games_room.html')
	elif name in 'Hall way':
		return readHTML(path + 'hall.html')
	elif name in 'Outside':
		return readHTML(path + 'outside.html')
	elif name in 'Repair room':
		return readHTML(path + 'PC_repair_room.html')


def readHTML(file):
	f = codecs.open(file, 'r')
	content = f.read()
	return content;

def search_1(search_word):
	video_dir = 'videos'
	for filename in os.listdir(video_dir):
		if search_word in filename:
			pass # Do sthing

if __name__ == "__main__":
    app.run()
	#print(readHTML('index.html'))
