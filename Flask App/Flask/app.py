from flask import Flask, render_template, request, url_for, flash, redirect
from main import *

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        try:
            tb = find_rank_new(take_input(content))
        except:
            flash('Invalid console output, make sure to copy the entire console output of status command.')
        if not content:
            flash('Content can not be empty')
        else:
            return render_template('index.html', result=tb)
    return render_template('create.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=False)