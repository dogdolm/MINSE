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
            if payed_users.check(login) != False:
                return registered(payed_users.check(login))
            else:
                return flask.redirect('/entrance/')
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
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>MINSE - оплата</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head><body><div class="offcanvas offcanvas-start show" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel" style="visibility: visible;"><div class="offcanvas-header"><h5 class="offcanvas-title" id="offcanvasLabel">Важное сообщение!</h5><button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button></div><div class="offcanvas-body">Внимание! Не оплачивайте подписку если вы не из 7 класса 444 школы!</div></div>' + href + hreft + '</body><script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script></html>'


def registered(login):
    if login == "lite":
        return flask.render_template('for_lite.html')
    elif login == "standart":
        return flask.render_template('for_standart.html')
    elif login == "premium":
        return flask.render_template('for_premium.html')


if __name__ == "__main__":
    application.run(host="0.0.0.0")