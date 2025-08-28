#This will contain my analyze_log funtion - which will be responsible for:
# 1. extrracting the decrypted status from logs
# 2. counting the occurrences of statuses 
# 3. listing the the summary of Login atttempts


#importing the decrypt_log function
from cryption import decrypt_log 
#importing the Counter class from the collections module
from collections import Counter

USER_LOG = "users_details.txt"

def analyze_log(filepath, key_path):
    logs = decrypt_log(filepath, key_path)

    #this will only extract the statuses 
    statuses = [row['status'] for row in logs if row["status"]]

    #this will count the occurrences of statuses
    counts = Counter(statuses) 

    return dict(counts)     #this will return usable data for the dashboard





if __name__ == "__main__":
    summary = analyze_log("login_log_encrypt.txt", "secret.key")

    print("\n ==== Summry of Login Attempts ===")
    for status, count in summary.items():
        print(f"{status}: {count}")


