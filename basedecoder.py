# -*- coding: utf-8 -*-
"""
Decoding from base64 to plain-text and another way.
"""
import base64
from flask import Flask, request, render_template


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        string = request.form['text']
        if "decode" in request.form.keys():
            try:
                result = base64.b64decode(string).decode("utf-8")
            except:
                result = u"It isn't a Base64!"
            return render_template('index.html', source_text=string, result=result)
        elif "encode" in request.form.keys():
            return render_template('index.html', source_text=string,
                                   result=base64.b64encode(string.encode("utf-8")))
        return render_template('index.html', source_text=u"Wrong request!")
    return render_template('index.html', source_text=u"")


if __name__ == '__main__':
    app.run(debug=True)
