 MGNREGA Data Visualization Dashboard
Overview

An interactive web dashboard for analyzing and visualizing MGNREGA (Mahatma Gandhi National Rural Employment Guarantee Act) data.
The system allows users to explore metrics such as Total Persondays and Participation Trends for different districts and months, using real-time visual insights powered by Flask and Plotly Dash.

 Key Features

 Interactive bar and line charts for monthly/district trends

 District-level analytics for performance comparison

 Dynamic filtering and visualization updates

 CSV-based dataset integration

 Web-based dashboard deployable on Render, Railway, or Vercel

 Tech Stack
Component	Technology
Backend	Flask (Python)
Frontend	Dash + Plotly
Data Handling	Pandas
Deployment	Gunicorn
Utilities	Geocoder
📂 Project Structure
📁 MGNREGA-Dashboard/
│
├── app.py                         # Main application file
├── assets/
│   ├── style.css                  # Optional custom CSS for styling
│
├── data/
│   ├── mgnrega_data.csv           # Dataset file
│
├── README.md                      # Project documentation
└── requirements.txt               # Dependencies list

Setup Instructions
1️ Install Dependencies

Make sure you have Python 3.x installed.
Then run:

pip install -r requirements.txt

2️ Run the App Locally
python app.py

3️ Open in Browser

Once the server starts, open:

http://127.0.0.1:8050/

 Insights Provided

Total Persondays per Month (District-wise)

Participation Trends per Month

Comparative Analytics for Different Districts

Clear Data Visualization for Reporting and Intern Analysis

 requirements.txt
Flask==3.0.3
pandas==2.2.2
plotly==5.24.1
gunicorn==23.0.0
geocoder==1.38.1

 Deployment Guide (Render / Railway / Vercel)
Step 1: Push Your Code to GitHub

Include all folders and files (especially app.py, requirements.txt, and data/).

Step 2: Create a New Web Service

Platform: Render / Railway / Vercel

Environment: Python 3.x

Start Command:

gunicorn app:server

Step 3: Wait for Deployment

Once the build completes, your app will be live at a generated URL (e.g., https://mgnrega-dashboard.onrender.com).

 Future Enhancements

Real-time API data fetch from MGNREGA website

Database integration (MySQL/PostgreSQL)

Role-based user dashboard

Mobile-responsive layout

 License

This project was developed as part of an Internship Project .
© 2025 Priyanka — All rights reserved.
