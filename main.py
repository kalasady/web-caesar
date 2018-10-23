from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" />
            <textarea name="text">{0}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    user_text = str(request.form['text'])
    rot_value = int(request.form['rot'])
    return form.format(rotate_string(user_text, rot_value))

app.run()