import os
import urllib3
import json
import traceback
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

def email(receiver, subject, content):
    """Send email
    :param receiver: email address where we send email
    :param subject: text for email subject
    :param content: text for email content
    :return: boolean if success, error message if not
    """

    message = Mail(
    from_email='oskari.jarvelin@myynninmaailma.fi',
    to_emails=receiver,
    subject=subject,
    html_content=content)
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        return True
    except Exception as e:
        return e.message

def slack(message):
    """Send slack message
    :param message: message content
    :return: boolean if success, error message if not
    """
    try:
        slack_message = {'text': message}
        http = urllib3.PoolManager()
        response = http.request('POST', 'https://hooks.slack.com/services/' + os.getenv('SLACK_TOKEN'), body = json.dumps(slack_message), headers = {'Content-Type': 'application/json'}, retries = False)
    except:
        traceback.print_exc()

    return True