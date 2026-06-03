# Car Price Predictor - Deployment Guide

## Quick Deployment on Render.com (Recommended - Free & Easy)

### Step 1: Prepare Your Project
✅ Already done! Your project has been prepared with:
- `Procfile` - Configuration for Render
- `requirements.txt` - All dependencies
- `runtime.txt` - Python version specification

### Step 2: Push to GitHub
1. Create a GitHub account (if you don't have one): https://github.com
2. Create a new repository named `car-price-predictor`
3. In your terminal, run these commands from your project folder:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/car-price-predictor.git
git push -u origin main
```

### Step 3: Deploy on Render
1. Go to https://render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account and select `car-price-predictor` repository
4. Fill in the settings:
   - **Name**: `car-price-predictor`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - Keep other settings as default
5. Click **"Create Web Service"**
6. Wait 2-3 minutes for deployment to complete
7. Your app will be live at: `https://car-price-predictor-xxxx.onrender.com`

---

## Alternative: Railway.app

1. Go to https://railway.app
2. Click **"New Project"** → **"Deploy from GitHub"**
3. Connect GitHub and select your repository
4. Railway auto-detects Flask app
5. Your app will be live in minutes

---

## Alternative: PythonAnywhere

1. Go to https://pythonanywhere.com
2. Sign up for free account
3. Upload your files via Web interface
4. Set up a new web app (Flask)
5. Configure to use your app.py

---

## Testing Your Deployment

Once deployed, visit your live URL and test:
- Select Toyota, Model: Corolla, Year: 2015, Fuel: Petrol, KM: 50000
- Click "Predict Price"
- You should get: ₹561,072.09

---

## Troubleshooting

**If you get 500 error:**
- Check Render/Railway logs for error messages
- Ensure all files are uploaded (especially `LinearRegressionModel.pkl` and `Cleaned_Car_data.csv`)

**If page looks broken (no CSS):**
- The app is working, just CSS isn't loading - this is normal for some deployments

**If prediction fails:**
- Ensure `LinearRegressionModel.pkl` is included in deployment

---

## Project Files Needed for Deployment:
✅ app.py
✅ requirements.txt
✅ Procfile
✅ runtime.txt
✅ .gitignore
✅ templates/index.html
✅ static/style.css
✅ Cleaned_Car_data.csv
✅ LinearRegressionModel.pkl
