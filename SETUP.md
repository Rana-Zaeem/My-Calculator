# Setup Guide

## Quick Setup for Deployment

Follow these steps to prepare your app for deployment:

1. **Initialize Git repository**:

   ```bash
   cd c:\Users\mb\Desktop\streeamlit
   git init
   git add .
   git commit -m "Initial commit of Age Calculator app"
   ```

2. **Create a GitHub repository**:
   - Go to [GitHub](https://github.com)
   - Create a new repository (e.g., "age-calculator")
   - Follow the instructions to push an existing repository

3. **Push to GitHub**:

   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/age-calculator.git
   git branch -M main
   git push -u origin main
   ```

4. **Deploy on Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub account
   - Select the repository you just created
   - Set the main file path to `streamlit_app.py`
   - Click "Deploy"

## Running Locally

To run the app locally before deploying:

```bash
cd c:\Users\mb\Desktop\streeamlit
streamlit run streamlit_app.py
```

The app will open in your default web browser at [http://localhost:8501](http://localhost:8501)

## File Structure Check

Make sure you have all these files in your repository before deploying:

- `streamlit_app.py` (main app)
- `requirements.txt` (dependencies)
- `.streamlit/config.toml` (Streamlit configuration)
- `README.md` (project documentation)
- `.gitignore` (git ignore file)
- `DEPLOYMENT.md` (this deployment guide)

## Troubleshooting

If the app works locally but has issues on Streamlit Cloud:

- Check that all dependencies are in `requirements.txt`
- Ensure there are no path-specific operations in your code
- Review the deployment logs on Streamlit Cloud
