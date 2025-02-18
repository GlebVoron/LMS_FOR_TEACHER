import flask

app = flask.Flask(__name__)


@app.route('/')
def slesh():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/image_mars')
def promotion():
    return f"""
    <html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{flask.url_for('static', filename='mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она какая, красная планета.</p>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')