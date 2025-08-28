SIMPLE BUT BUILT WITH LOVE - Smile

# Mini_SOC_Dashboard_Project
Hello kindly check out my first simple mini soc dashboard project.
Built with Python Tkinter, It demonstrates basic log monitoring, reads encrypted log files, displays summaries of login attempts (success & failed), supports refresh, and exports data to Excel.


## Features
- Reads & decrypts encrypted login logs.  
- Shows real-time **summary of login attempts** (successful vs failed).  
- **Refresh button** to reload latest logs.  
- Export results to **CSV (soc_report.csv)** for further analysis.  
- Maintains **user details** in a separate log file.  



## Project Structure
mini-soc-dashboard/
│── analysis.py # Handles log analysis
│── cryption.py # Handles encryption/decryption
│── dashboard.py # Tkinter GUI dashboard
│── users_details.txt # Stores user activity
│── login_log_encrypt.txt # Encrypted log file
│── requirements.txt # Project dependencies


## Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/mini-soc-dashboard.git
   
2. Install dependencies:
    pip install -r requirements.txt

3. Run the dashboard:
   python dashboard.py


Future Improvements

Generate styled PDF report with tables & headers.

Add real-time log monitoring.

Improve GUI design.



Author
Mercy Ikeh
http://www.linkedin.com/in/mercy-ikeh-8946482aa

Gracias for scrolling to this point!

