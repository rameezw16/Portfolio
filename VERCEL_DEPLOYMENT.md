# Vercel Deployment Guide

## Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Create a new repository called `portfolio` (or any name)
3. Clone it locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/portfolio.git
   cd portfolio
   ```

## Step 2: Upload Your Portfolio Files

Copy all files from `c:\Users\HP\Downloads\Portfolio Website` to your cloned repository:
- index.html
- styles.css
- script.js
- app.py
- requirements.txt
- vercel.json
- github_data.json
- All image files (*.png, *.jpeg)

## Step 3: Initialize Git and Push to GitHub

```bash
git add .
git commit -m "Initial portfolio commit"
git branch -M main
git push -u origin main
```

## Step 4: Deploy to Vercel

### Option A: Using Vercel Dashboard (Easiest)

1. Go to https://vercel.com/signup (sign up with GitHub)
2. Click "New Project"
3. Select your portfolio repository
4. Click "Import"
5. Under "Environment Variables", add:
   - Key: `GMAIL_APP_PASSWORD`
   - Value: Your 16-character Gmail app password
6. Click "Deploy"

### Option B: Using Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. When prompted, set the environment variable:
   ```bash
   vercel env add GMAIL_APP_PASSWORD
   # Enter your Gmail app password when prompted
   ```

## Step 5: Get Gmail App Password

1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer"
3. Google generates a 16-character password
4. Copy and use this in Vercel environment variables

## Step 6: Verify Deployment

1. Your site will be live at: `https://your-project-name.vercel.app`
2. Test the contact form to make sure emails work
3. Check that all images display correctly

## Step 7: Custom Domain (Optional)

1. In Vercel dashboard, go to Settings → Domains
2. Add your custom domain
3. Update DNS records following Vercel's instructions

## Troubleshooting

### Images not showing
- Make sure image filenames match exactly (case-sensitive)
- Verify all files are pushed to GitHub

### Email not working
- Check that GMAIL_APP_PASSWORD environment variable is set
- Verify the app password is correct (16 characters)
- Check Vercel logs for errors: Dashboard → Deployments → Logs

### Form errors
- Open browser DevTools (F12) → Console to see error messages
- Check that endpoint is `/send-email` (not localhost)

## Updating Your Portfolio

After deployment, to make changes:

1. Edit files locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update portfolio"
   git push
   ```
3. Vercel automatically redeploys on every push

## Keeping GitHub Data Fresh

To update your project list with new repositories:

```bash
python fetch_github.py
git add github_data.json
git commit -m "Update GitHub projects"
git push
```

## Security Notes

- Never commit your Gmail password to GitHub
- Always use environment variables for secrets
- Gmail app passwords are safer than your main password
- You can revoke app passwords anytime in your Google account settings
