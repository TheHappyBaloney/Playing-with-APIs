from flask import Flask
import main
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def index():
    return render_template('index.html')

@app.route('/get_image')
def get_image():
    category = requests.args.get('category', 'Random')
    image_data = main.get_image(category)  
    return jsonify(image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)