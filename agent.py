from google.adk.agents import Agent

import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

smtp_host = "smtp.google.com" 
smtp_port = 587

def emailTool(recipient_email:str, subject:str, message: str):
    """
    Sends an email. 

    Args:
        recipient_email: The email adress that receives email
        subject: Email subject
        message: Email content
        
    Returns:
        string: confirmation or error message whether the email was sent or not
    """

    server = smtplib.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(user=sender_email,password=sender_password)

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Send the message via our own SMTP server.
    try:
        server.send_message(msg)
    except:
        return "Message could not be send"
    finally:
        return "Successful!"

root_agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that sends an Email"
    ),
    instruction=(
        "You are a helpful agent who sends emails"
    ),
    tools=[emailTool],
)