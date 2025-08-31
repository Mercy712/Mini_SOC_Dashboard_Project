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

Mini-SOC-Dashboard/
│── encrypt_key_log_file.py   # Generates data + encryption
│── dashboard.py              # Main SOC Dashboard (Tkinter UI)
│── cryption.py               # Encryption & decryption functions
│── analysis.py               # Log analysis functions
│── secret.key                # Encryption key (auto-generated)
│── login_log_encrypt.txt     # Encrypted logs
│── login_log.txt             # Plain logs
│── users_details.txt         # User details
│── requirements.txt          # Dependencies





## How to Run the Mini SOC Dashboard

### Clone this repo
   ```bash
      git clone https://github.com/Mercy712/mini-soc-dashboard.git
      cd mini-soc-dashboard

# prerequisites:

* Install Python 3.x on your system
* Install the required dependencies

      pip install -r requirements.txt

* Tkinter usually comes with Python, but if it's missing run:
   # On Ubuntu/Debian
      sudo apt-get install python3-tk
   # On Windows  (Tkinter comes pre-installed with Python)


## STEP 1: Generate Data
Run the encrypt_key_log_file.py script. This will:

- Request user’s details (username, password, etc.)

- Generate secret.key (your encryption key)

- Encrypt login details

- Create the following files automatically:

   * login_log_encrypt.txt → encrypted login attempts

   * login_log.txt → plain text login log (for debugging/personal reference)

   * users_details.txt → stores registered user details in plain text
 


## STEP 2: Launch the Dashboard
Run the dashboard.py script. This will:

- Display decrypted login logs in the dashboard UI

- Show a summary of login attempts (success vs failed logins)

- Allow you to export a report (soc_report.csv) by clicking the Export CSV button

- Let you refresh logs with the Refresh button



Future Improvements

Add real-time log monitoring.

Improve GUI design.



Author
Mercy Ikeh
http://www.linkedin.com/in/mercy-ikeh-8946482aa

Gracias for scrolling to this point!

