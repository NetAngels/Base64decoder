# -*- coding: utf-8 -*-
"""
Приложение предназначено для декодирования из base64 в plain-text.
"""

from flask import Flask, request, render_template


app = Flask(__name__)
app.config.from_object(__name__)

def decoder(coding_text):
    """function do decoding string from base64
to plain text
    
    Arguments:
    - `coding_text`: string
    """
    pass


#------------------------------------------------------------
# view
#------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    """ main page whith main forms"""

    if request.method == 'POST':
        string = request.form['base64text'].decode("utf-8")
        return render_template('index.html', 
                               rezult=string.decode("utf-8"))
    else:
        return render_template('index.html',
                               rezult='Тестовое сообщение'.decode("utf-8"))

if __name__ == '__main__':
    app.run(debug=True)
