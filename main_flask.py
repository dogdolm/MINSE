import flask
application = flask.Flask(__name__)


@application.route('/')
def index():
    return flask.render_template('mainpage.html')


@application.route('/compare/')
def compare():
    return flask.render_template('compare.html')


@application.route('/login/')
def login():
    return flask.render_template('login.html')


@application.route('/entrance/')
def entrance():
    return flask.render_template('entrance.html')



if __name__ == "__main__":
   application.run(host='0.0.0.0')
