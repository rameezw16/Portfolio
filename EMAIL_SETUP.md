# Email Setup Instructions

To enable the contact form to send emails to your inbox, follow these steps:

## Step 1: Set Up Gmail App Password

1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer" (or your device)
3. Google will generate a 16-character app password
4. Copy this password

## Step 2: Install Flask and Required Packages

Run this command in your terminal:
```bash
pip install flask flask-cors
```

## Step 3: Set Environment Variable

### On Windows (PowerShell):
```powershell
$env:GMAIL_APP_PASSWORD = "your_16_character_password_here"
python app.py
```

### On Windows (Command Prompt):
```cmd
set GMAIL_APP_PASSWORD=your_16_character_password_here
python app.py
```

## Step 4: Run the Backend

Keep the Flask app running while your portfolio is live:
```bash
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

## Step 5: Keep Both Servers Running

- Keep the Flask backend running on port 5000
- Keep the HTTP server running on port 8000 for your portfolio

Now when users submit the contact form, emails will be sent to rameezwasif1@gmail.com!

## Troubleshooting

- Make sure Flask is installed: `pip list | findstr flask`
- Make sure the app password is set correctly
- Check that port 5000 is not blocked
- Look at the console for any error messages
