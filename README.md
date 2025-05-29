# IMEI Label Flask App

This app allows you to upload an Excel file, search for an IMEI, and generate printable label images with barcodes.

## Deploy to Render

1. Push this code to a GitHub repo
2. Go to https://render.com and create a Web Service
3. Choose Python environment
4. Use `web: python flask_label_auto_print.py` as your start command
5. Add a build command: `pip install -r requirements.txt`
6. Done!
