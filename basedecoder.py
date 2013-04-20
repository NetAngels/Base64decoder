# -*- coding: utf-8 -*-
"""
Приложение предназначено для декодирования из base64 в plain-text.
"""

import base64
from flask import Flask, request, render_template


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ main page whith main forms"""

    if request.method == 'POST':
        string = request.form['base64text'].decode("utf-8")
        if "decoder" in request.form.keys():
            try:
                rezult = base64.b64decode(string).decode("utf-8")
            except:
                rezult = u"Это не Base64!"
            return render_template('index.html', 
                                   rezult=rezult,
                                   source_text=string)
        elif "coder" in request.form.keys():
            try:
                rezult = base64.b64encode(string).decode("utf-8")
            except:
                rezult = u"Произошла ошибка!"
            return render_template('index.html', 
                                   rezult=rezult,
                                   source_text=string)
    else:
        return render_template('index.html', source_text=u"")


if __name__ == '__main__':
    app.run(debug=True)
