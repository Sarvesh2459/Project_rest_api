from flask import Flask,render_template
app = Flask(__name__ , static_url_path="" , static_folder="./static/css" , template_folder="./static/css")
@app.route('/')
def home():
	Method = ['PATCH', 'GET', 'PUT', 'DELETE']
	return render_template('index.html', Method=Method)
if __name__ == "__main__":
	app.run(debug=True)