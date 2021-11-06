from flask import Flask, render_template, request, flash, session
from main import *

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        tries = 3
        while(tries):
            try:
                flash('Query submitted, please wait while we reveal the ranks...', 'info')
                tb = find_rank_new(take_input(content))
                tries = 0
                if not content:
                    session.pop('_flashes', None)
                    flash('Content can not be empty.', 'danger')
                else:
                    session.pop('_flashes', None)
                    flash('Hooray! Ranks revealed.', 'success')
                    return render_template('index.html', result=tb)
            except:
                session.pop('_flashes', None)
                flash('Invalid console output, make sure to copy the entire console output of status command. If the status command output is correct please retry submit button 2-3 times as it might be the issue with scraper.', 'danger')
                tries-=1
    return render_template('create.html')


if __name__ == '__main__':
    app.secret_key = "a@egWYR~fkQ=lyN"
    app.run(host="0.0.0.0", debug=False)