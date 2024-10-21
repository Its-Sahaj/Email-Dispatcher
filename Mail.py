import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import getpass
import os

def send_email(smtp_server, smtp_port, login_email, password, to_emails, subject, body, attachments):
    try:
        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = login_email
        message['To'] = ', '.join(to_emails)
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Attach files if any
        for file_path in attachments:
            try:
                with open(file_path, 'rb') as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                message.attach(part)
            except Exception as e:
                print(f"Could not attach {file_path}: {e}")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(login_email, password)
            server.sendmail(login_email, to_emails, message.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle user inputs
def main():
    # Get user input
    smtp_server = input('Enter SMTP server (e.g., smtp.gmail.com): ')
    smtp_port = int(input('Enter SMTP port (e.g., 587): '))
    login_email = input('Enter your email: ')
    password = getpass.getpass('Enter your password: ')  # Use getpass to hide password input
    to_emails = input('Enter recipient emails separated by commas: ').split(',')
    subject = input('Enter email subject: ')
    body = input('Enter email body: ')
    attachments_input = input('Enter file paths separated by commas (optional): ')
    
    attachments = [path.strip() for path in attachments_input.split(',')] if attachments_input else []

    # Call the send_email function
    send_email(
        smtp_server=smtp_server,
        smtp_port=smtp_port,
        login_email=login_email,
        password=password,
        to_emails=[email.strip() for email in to_emails],
        subject=subject,
        body=body,
        attachments=attachments
    )

if __name__ == "__main__":
    main()
