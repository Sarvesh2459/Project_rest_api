from flask import Flask,render_template,request,json,redirect,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__ , static_url_path="" , static_folder="./static/css" , template_folder="./static/css")

@app.route('/')
def home():
	Method = ['PATCH', 'GET', 'PUT', 'DELETE']
	return render_template('index.html', Method=Method)


@app.route('/submitJSON' , methods=["GET","POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    response = ''
    method=jsonObj['methods']
    id=jsonObj['id']
    name = jsonObj['name']
    views = jsonObj['views']
    likes = jsonObj['likes']
    f=open('description.txt' , 'w+')
    f.write(method+"\n"+id+"\n" + name+"\n"+views + "\n" +likes)
    f.close()
if __name__ == "__main__":
	app.run(host="localhost" , port="8000" , debug=True)
