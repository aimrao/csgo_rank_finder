from flask import Flask, render_template, request, flash, session
from main import *
from prettytable import PrettyTable

app = Flask(__name__)
app.secret_key = "a@egWYRasdasda1231~fkQ=lyN"
app.static_folder = 'static'

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
                elif len(tb) == 0:
                    session.pop('_flashes', None)
                    flash('Invalid console output.', 'danger')
                else:
                    tb_str = PrettyTable()
                    tb_str.field_names = ['Name', 'Rank', 'Best', 'Wins']
                    tb_str.add_rows(val[:4] for val in tb)
                    tb.append(tb_str)
                    session.pop('_flashes', None)
                    flash('Hooray! Ranks revealed.', 'success')
                    return render_template('index.html', result=tb)
            except Exception as e:
                print(e)
                session.pop('_flashes', None)
                flash('Invalid console output, make sure to copy the entire console output of status command. If the status command output is correct please retry submit button 2-3 times as it might be the internal server issue.', 'danger')
                tries -= 1
    return render_template('create.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
