import flask
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('mainpage.html')


@app.route('/compare/')
def compare():
    return flask.render_template('compare.html')


@app.route('/login/')
def login():
    return flask.render_template('login.html')


app.run()
