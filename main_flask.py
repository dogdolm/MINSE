import flask
application = flask.Flask(__name__)


@application.route('/')
def index():
    return flask.render_template('mainpage.html')


@application.route('/compare/')
def compare():
    return flask.render_template('compare.html')


@application.route('/login/', methods=['get', 'post'])
def login():
    if flask.request.method == 'POST':
        import password
        login = flask.request.form.get('login')
        passwd1 = str(flask.request.form.get('passwd'))
        passwd2 = str(flask.request.form.get('passwdrepeat'))
        if passwd2 == passwd1:
            f = password.create_account(login, passwd1)
            if f == True:
                return flask.redirect('/pay/')
            else:
                return flask.render_template('login.html', message="Логин уже зарегистрирован!")
    return flask.render_template('login.html')


@application.route('/entrance/', methods=['get', 'post'])
def entrance():
    if flask.request.method == 'POST':
        import password
        login = flask.request.form.get('email')
        passwd = str(flask.request.form.get('passwd'))
        f = password.check_password(login, passwd)
        if f == True:
            return flask.redirect('/pay/')
        else:
            return flask.render_template('entrance.html', message="Пароль или логин неверен!")
    return flask.render_template('entrance.html')


@application.route('/pay/')
def payment():
    return flask.render_template('pay.html')


if __name__ == "__main__":
    application.run()

