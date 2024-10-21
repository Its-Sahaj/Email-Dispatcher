# Email-Dispatcher
I created the email-sending project because it's a practical demonstration of how Python can be used to automate tasks that involve sending emails, which is a common real-world use case. I created this project using both simple python and also using colab . This type of project introduces important concepts like:

Interacting with External Services (SMTP): It shows how to connect to an email server using Python to send messages, which is useful in many automated systems, like sending notifications, reports, or alerts.

Security Practices (App Passwords): The project includes using secure methods like App Passwords, promoting best practices when handling sensitive information like credentials.

User Interaction (Widgets in Colab): By including interactive widgets, the project becomes more user-friendly, allowing users to input email details in a form rather than hardcoding them.

Real-World Application: Automating emails is highly relevant in fields like business, development, and system monitoring. It can be applied in tasks like sending invoices, marketing emails, or error reports.

Overall, it's a simple yet powerful example of how Python can streamline communication processes, making tasks more efficient.
![Screenshot 2024-10-21 233303](https://github.com/user-attachments/assets/1a148dee-9ce8-4f29-af2c-d722697577f9)
![Screenshot 2024-10-21 221918](https://github.com/user-attachments/assets/bd55e046-de8a-4416-8da2-a9dc3acfd18a)
![Screenshot 2024-10-21 235426](https://github.com/user-attachments/assets/e8833e08-c9d5-4762-9ae0-88e4d0043ebd)

#Note : Generally you would have an error because of password would not be accepted but it can be easily resolved by following these steps :
Go to Google Account Security Settings:

Open your browser and navigate to https://myaccount.google.com/security.
Sign in to Your Google Account:

If you're not already signed in, log in using your Google email address and password.
Enable 2-Step Verification (if not already enabled):

Scroll down to the Signing in to Google section.
Look for the option labeled 2-Step Verification. If it's not enabled, you need to set it up.
Click 2-Step Verification and follow the prompts to enable it. You'll need to verify your identity (usually via SMS or the Google Authenticator app).
After enabling 2-Step Verification, proceed to the next step.

Access App Passwords:

Once 2-Step Verification is enabled, return to the Signing in to Google section.
You will now see the App Passwords option available below 2-Step Verification.
Click on App Passwords.
Generate an App Password:

In the App Passwords section, Google will ask you to select the app and the device for which you want to create the password.
In the drop-down menu under Select app, choose Mail.
Under Select device, choose Other (Custom name).
A text box will appear where you can enter a custom name for the device. For example, type "Colab Email Sender" or any custom name that makes sense to you.
Click Generate.
Copy Your App Password:

Google will generate a 16-character App Password. It will look something like this: abcd efgh ijkl mnop.
Copy this password (including spaces).
You won’t need to remember it, as it’s only used for authentication in apps. You can always generate a new one if needed.
Use the App Password in Your Code:

In your Python code (in Colab or elsewhere), replace your regular Gmail password with the generated 16-character App Password.
