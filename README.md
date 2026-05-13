# Caesar Cipher Web Application

A modern, visually stunning web implementation of the classic Caesar Cipher algorithm. Built with a Python/Flask backend and a beautiful, glassmorphism-inspired HTML/CSS frontend.

## Features

- **Encrypt Messages**: Easily obfuscate your text using a shift-based Caesar Cipher.
- **Decrypt Messages**: Decode previously encrypted text back into readable English by providing the correct shift key.
- **Premium UI**: Dark mode aesthetics with glassmorphism, animated backgrounds, and a responsive layout for mobile and desktop devices.
- **Serverless Ready**: Fully configured for instant, zero-hassle deployment on Vercel using Python serverless functions.

## Technology Stack

- **Frontend**: HTML5, Vanilla CSS3 (Custom properties, Flexbox, CSS Animations)
- **Backend**: Python 3, Flask
- **Deployment**: Vercel Serverless Functions

## Local Development Setup

To run this project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/pavanmnaikcse/caesar_cipher.git
   cd caesar_cipher
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Deploying to Vercel

This project is pre-configured for Vercel. 
1. Log in to [Vercel](https://vercel.com).
2. Click "Add New..." -> "Project".
3. Import your GitHub repository (`caesar_cipher`).
4. Click **Deploy**. Vercel will automatically read the `vercel.json` and deploy your Flask app as a serverless function.
