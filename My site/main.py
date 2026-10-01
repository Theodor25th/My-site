from flask import Flask
from flask import request, render_template, send_from_directory
import os
app = Flask(__name__)

def get_image_files():
    path = os.path.join('my site', 'static', 'images')
    return os.listdir(path)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    return render_template("index.html")

@app.route("/blog")
def blogpost():
    return render_template("blogpost.html")

@app.route("/record")
def record():
    return render_template("aboutme.html")

@app.route("/memes", methods=['GET', 'POST'])
def memes():
    image_name = None
    top_text = None
    if request.method == 'POST':
        image_name = request.form.get('image_name', '')
        top_text = request.form.get('top_text', '')
    image_list = get_image_files()
    
    return render_template("memes.html", image_name=image_name, image_list=image_list, top_text=top_text)

@app.route("/calc", methods=['GET', 'POST'])
def calculator():
    number1 = 0
    number2 = 0
    if request.method == 'POST':
        number1 = request.form.get("num1", type=int)
        number2 = request.form.get("num2", type=int)
        if not (isinstance(number1, int) and isinstance(number2, int)):
            return render_template("calculator.html", result="Введите число, а не букву или дробь")
        if number1 < 0 or number2 < 0:
            return render_template("calculator.html", result="Вы ввели отрицательное число")
        if number1 > number2:
            return render_template("calculator.html", result="У вас текущий уровень больше нужного")
        return render_template("calculator.html", result=(number2 ** 2 + 6 * number2) - (number1 ** 2 + 6 * number1))
    return render_template("calculator.html", result=0)

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == "__main__":
    app.run(debug=True)