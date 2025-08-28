#this is my main SOC App - So you can think of it as the main Tkinter window

#import Tkinter to build the UI
import tkinter as tk 
import csv  

#import functions from cryption & analysis files
from cryption import decrypt_log
from analysis import analyze_log

#declearing a constant
FILEPATH = "login_log_encrypt.txt"
KEY_PATH = "secret.key"


#Funtion for CSV export 
def export_to_csv():
    exp_logs = decrypt_log(FILEPATH, KEY_PATH)
    exp_summary = analyze_log(FILEPATH, KEY_PATH)    

    with open("soc_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        #this will write logs - How logs will be written to the soc export csv file
        writer.writerow(["INFO", "STATUS", "TIMESTAMP"])
        for row in exp_logs:
           # writer.writerow([row["info"], row["status"], f"{row['timestamp']}"])
            writer.writerow([row["info"], row["status"], "\t" + row["timestamp"]])

        #Empty line between sections
        writer.writerow([])
        writer.writerow([])
        
        
        #this will write summary - How summary will be written to the soc export csv file
        writer.writerow(["STATUS", "COUNT"])
        for status, count in exp_summary.items():
            writer.writerow([status, count])

    

    
#Dashboard funtion begins
def show_dashboard():
    #Section A - create main window
    root = tk.Tk()
    root.title("Mini SOC Dashboard")
    root.geometry("800x600")    #this is the window size


    #Section A - the decrypted log section (left side)
    logs_frame = tk.LabelFrame(root, text="Decrypted Logs", padx=10, pady=10)
    logs_frame.pack(side="left", fill="both", expand=True)

    logs_text = tk.Text(logs_frame, wrap="word", width=60, height=20)
    logs_text.pack(fill="both", expand=True)
    
    
    #Section B - the login attempt section (right side)
    summary_frame = tk.LabelFrame(root, text="Summary of Login Attempts", padx=10, pady=10)
    summary_frame.pack(side="right", fill="both", expand=True)

    summary_text = tk.Text(summary_frame, wrap="word", width=30, height=20)
    summary_text.pack(fill="both", expand=True)



    #Section C - Funtion to get log data and summary into UI
    def load_data():
        #this will clear old conttent
        logs_text.delete("1.0", tk.END)
        summary_text.delete("1.0", tk.END)

    #to load encrypted logs
        logs = decrypt_log(FILEPATH, KEY_PATH)
        for row in logs:
            logs_text.insert("end", f"{row}\n")

    #to load the summary of the encrypted logs
        summary = analyze_log(FILEPATH, KEY_PATH)   
        for status, count in summary.items():
            summary_text.insert("end", f"{status}: {count}\n")

    #the initial load when app opens
    load_data()


    #Section D - the refresh and CSV buttonS

    #CSV Button
    export_btn =tk.Button(root, text="Export CSV", command=export_to_csv)
    export_btn.pack(side="top", pady=10)
    #Refresh Button
    refresh_btn =tk.Button(root, text="Refresh", command=load_data)
    refresh_btn.pack(side="bottom", pady=10)
      

    #Section E - Start main event loop
    root.mainloop()



if __name__ == "__main__":
    show_dashboard()


