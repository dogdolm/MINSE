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
        subscribition_type_premium = flask.request.form.get('premium')
        subscribition_type_standart = flask.request.form.get('standart')
        subscribition_type_lite = flask.request.form.get('lite')
        subscribition_type = 0
        if subscribition_type_premium == 'on':
            subscribition_type = 1
        elif subscribition_type_standart == 'on':
            subscribition_type = 2
        elif subscribition_type_lite == 'on':
            subscribition_type = 3
        else:
            return flask.render_template('login.html', message="Вы не выбрали подписку!")
        if passwd2 == passwd1:
            f = password.create_account(login, passwd1)
            if f == True:
                return payment(subscribition_type)
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
            import payed_users
            if payed_users.check(login) == True:
                return registered()
            else:
                return flask.redirect('/login/')
        else:
            return flask.render_template('entrance.html', message="Пароль или логин неверен!")
    return flask.render_template('entrance.html')


def payment(subscribition_type):
    if subscribition_type == 1:
        href = '<iframe src="https://yoomoney.ru/quickpay/button-widget?targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20Premium%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20minse.ru&default-sum=619&button-text=11&yoomoney-payment-type=on&button-size=l&button-color=black&mail=on&successURL=&quickpay=small&account=4100111091828033&" width="227" height="48" frameborder="0" allowtransparency="true" scrolling="no"></iframe>'
        hreft = '<iframe src="https://yoomoney.ru/quickpay/button-widget?targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20Premium%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20minse.ru&default-sum=619&button-text=11&any-card-payment-type=on&button-size=l&button-color=black&mail=on&successURL=&quickpay=small&account=4100111091828033&" width="227" height="48" frameborder="0" allowtransparency="true" scrolling="no"></iframe>'
    elif subscribition_type == 2:
        href = '<iframe src="https://yoomoney.ru/quickpay/button-widget?targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20Standart%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20minse.ru&default-sum=459&button-text=11&yoomoney-payment-type=on&button-size=l&button-color=black&mail=on&successURL=&quickpay=small&account=4100111091828033&" width="227" height="48" frameborder="0" allowtransparency="true" scrolling="no"></iframe>'
        hreft = '<iframe src="https://yoomoney.ru/quickpay/button-widget?targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20Standart%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20minse.ru&default-sum=459&button-text=11&any-card-payment-type=on&button-size=l&button-color=black&mail=on&successURL=&quickpay=small&account=4100111091828033&" width="227" height="48" frameborder="0" allowtransparency="true" scrolling="no"></iframe>'
    elif subscribition_type == 3:
        href = '<iframe src="https://yoomoney.ru/quickpay/button-widget?targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20Lite%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20minse.ru&default-sum=229&button-text=11&yoomoney-payment-type=on&button-size=l&button-color=black&mail=on&successURL=&quickpay=small&account=4100111091828033&" width="227" height="48" frameborder="0" allowtransparency="true" scrolling="no"></iframe>'
        hreft = '<iframe src="https://yoomoney.ru/quickpay/button-widget?targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20Lite%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20minse.ru&default-sum=229&button-text=11&any-card-payment-type=on&button-size=l&button-color=black&mail=on&successURL=&quickpay=small&account=4100111091828033&" width="227" height="48" frameborder="0" allowtransparency="true" scrolling="no"></iframe>'
    return flask.render_template('pay.html', href = href, hreft = hreft)


def registered():
    return flask.render_template('for_reg.html')


if __name__ == "__main__":
    application.run()

