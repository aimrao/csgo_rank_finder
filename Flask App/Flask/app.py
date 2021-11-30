from flask import Flask, render_template, request, flash, session
from main import *
from prettytable import PrettyTable
from threading import Thread

app = Flask(__name__)
app.secret_key = "a@egWYRasdasda1231~fkQ=lyN"
app.static_folder = 'static'

def queryResult(content, tb):
    tb.append(find_rank_new(take_input(content)))

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        try:
            content = request.form['content'].strip().split('\n')[1:-1]
            if len(content) > 5:
                threads = []
                tb2 = []
                for i in range(0, len(content),4):
                    process = Thread(target=queryResult, args=[content[i:i+4], tb2])
                    process.start()
                    threads.append(process)
                for process in threads:
                    process.join()
            tb = []
            for i in tb2:
                for j in i:
                    tb.append(j)
            tb_str = PrettyTable()
            tb_str.field_names = ['Name', 'Rank', 'Best', 'Wins', 'HS %', 'K/D']
            tb_str.add_rows(val[:6] for val in tb)
            tb.append(tb_str)
            flash('Hooray! Ranks revealed.', 'success')
            return render_template('index.html', result=tb)
        except Exception as e:
            flash('Invalid/Empty console output given', 'danger')

    return render_template('create.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=False)
