# Deployment Guide

## How to Deploy on Streamlit Cloud

Follow these steps to deploy your Interactive Age Calculator app on Streamlit Cloud:

1. **Create a GitHub repository**:
   - Push your code to a new GitHub repository
   - Make sure to include all files: `streamlit_app.py`, `requirements.txt`, `.streamlit/config.toml`, etc.

2. **Sign up for Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account

3. **Deploy your app**:
   - Click "New app"
   - Select your repository, branch (usually main)
   - Set the main file path to `streamlit_app.py`
   - Click "Deploy"

4. **Check your app**:
   - Once deployed, Streamlit will provide a URL where your app is live
   - Test all functionality to ensure it works as expected

## Repository Structure

```text
streeamlit/
├── streamlit_app.py      # Main application file
├── requirements.txt      # Dependencies
├── README.md            # Project documentation
├── .gitignore          # Git ignore file
└── .streamlit/         # Streamlit configuration
    └── config.toml     # Streamlit custom settings
```

## Requirements

The `requirements.txt` file includes:

- streamlit==1.27.0
- plotly==5.18.0
- python-dateutil==2.8.2

## Custom Configuration

The `.streamlit/config.toml` file contains custom theme settings:

- Custom color scheme
- Font settings
- Server configuration

## Troubleshooting

If you encounter issues during deployment:

1. Check your GitHub repository structure
2. Verify all dependencies are in `requirements.txt`
3. Make sure `streamlit_app.py` is the correct main file
4. Check the Streamlit Cloud logs for error messages
