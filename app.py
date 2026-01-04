from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
CORS(app)

# Email configuration
SENDER_EMAIL = "rameezwasif1@gmail.com"
RECEIVER_EMAIL = "rameezwasif1@gmail.com"
# You'll need to set an app password for Gmail
# Go to: https://myaccount.google.com/apppasswords
APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD', '')

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        if not all([name, email, message]):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Create email
        subject = f"New Portfolio Message from {name}"
        body = f"""
        New message from your portfolio website:
        
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """
        
        # Send email using Gmail SMTP
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECEIVER_EMAIL
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            server.send_message(msg)
            server.quit()
            
            return jsonify({'success': True, 'message': 'Email sent successfully!'}), 200
        
        except Exception as e:
            print(f"SMTP Error: {e}")
            return jsonify({'success': False, 'message': f'Error sending email: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# For local testing
if __name__ == '__main__':
    app.run(debug=False, port=5000)
