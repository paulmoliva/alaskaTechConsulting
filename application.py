import flask
import os

application = flask.Flask(__name__)

application.secret_key = os.getenv('SECRET_KEY') or 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@application.route('/')
def index():
    return flask.render_template('home.html')

@application.route('/services')
def services():
    return flask.render_template('services.html')

if __name__ == '__main__':
    application.run(debug=True)
