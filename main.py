from flask import Flask,request
import getpostfromreddit # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/hot')
def hot_meme():
    return getpostfromreddit.downloadMeme("hot",request.args.get('count', default = 1, type = int))

@app.route('/new')
def dynamic_page():
    print(request.args.get('count', default = 1, type = int))
    return getpostfromreddit.downloadMeme("new",request.args.get('count', default = 1, type = int))

@app.route('/zenhot')
def hot_meme():
    return getpostfromreddit.downloadZenMeme("hot",request.args.get('count', default = 1, type = int))

@app.route('/zennew')
def dynamic_page():
    print(request.args.get('count', default = 1, type = int))
    return getpostfromreddit.downloadZenMeme("new",request.args.get('count', default = 1, type = int))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8050', debug=True)