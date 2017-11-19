import flask
import os
import requests

application = flask.Flask(__name__)

application.secret_key = os.getenv('SECRET_KEY') or 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@application.route('/')
def index():
    return flask.render_template('home.html')


@application.route('/services')
def services():
    return flask.render_template('services.html')


@application.route('/contact')
def contact():
    return flask.render_template('contact.html')


@application.route('/form-submit', methods=['POST'])
def form_submit():
    form_json_data = flask.request.json
    key = os.getenv('mailgun_api_key')
    sandbox = 'alaskatechconsulting.com'
    recipient = 'paulmoliva+aktech@gmail.com'

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': form_json_data['email'],
        'to': recipient,
        'subject': 'Alaska Tech Consulting Form Submission',
        'text': 'Name: {name} \n Email: {email} \n Phone: {phone} \n Message: {message} \n'.format(
            name=form_json_data['name'],
            email=form_json_data['email'],
            phone=form_json_data['phone'],
            message=form_json_data['message']
        )
    })

    print('Status: {0}'.format(request.status_code))
    print('Body:   {0}'.format(request.text))
    return ''

if __name__ == '__main__':
    application.run(debug=True)
