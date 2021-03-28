from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'строитель' in prof.lower() or 'инженер' in prof.lower():
        return render_template('base.html', name='Инженерные тренажеры',
                               pic='ing')
    else:
        return render_template('base.html', name='Научные симуляторы',
                               pic='nau')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
