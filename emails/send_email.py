import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from feedback.api_key import *

def send_email(data):
    msg = MIMEMultipart("alternative")
    # an array of {question, response, word_choice, clarity, tone, time}
    print(data)
    feedback_data = data['feedback']
    print(feedback_data)

    def question_feedback(feedbacks):
        for i in range(len(feedback_data)):
            q = feedback_data[i]
            timing = "Good"
            if int(q['timing']) < 30:
                timing = "Too short"
            elif int(q['timing']) > 120:
                timing = "Too long"

            feedbacks.append(f"""
            <li>
                <b>Question</b>: {q['question']}
                <ul>
                    <li><b>Your Response:</b> {q['response']}</li>
                    <li>Word choice: {q['wordChoice']}</li>
                    <li>Clarity: {q['clarity']}</li>
                    <li>Tone: {q['tone']}</li>
                    <li>Timing: {timing}</li>
                </ul>
            </li>""")

    feedbacks = []
    question_feedback(feedbacks)
    print(''.join(feedbacks))

    html = f"""<html>
        <head></head>
        <body>
            <p>Thank you for using CareerCue! Here is a summary of the feedback from your latest session:</p>
            <br><br>
            <ul>{''.join(feedbacks)}</ul>
            <br>
            <p>Happy interviewing!</p>
        </body>
    </html>
    """
    print(html)
    
    html_content = MIMEText(html, "html")
    msg["Subject"] = "Your CareerCue Feedback"
    msg["From"] = "cmdf.2023.mailserver@gmail.com"
    msg["To"] = data['email']

    msg.attach(html_content)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    #s = smtplib.SMTP('localhost')
    #s.sendmail("cmdf.2023.mailserver@gmail.com", [data['email']], msg.as_string())
    #s.quit()

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("cmdf.2023.mailserver@gmail.com", EMAIL_PASSWORD)
        server.sendmail(
            "cmdf.2023.mailserver@gmail.com", data['email'], msg.as_string()
        )