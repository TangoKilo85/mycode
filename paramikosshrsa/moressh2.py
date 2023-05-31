import paramiko
import csv
from datetime import datetime

def read_connections(filename):
    """Reads the connection information from a CSV file"""
    credz = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            credz.append({'un': row['username'], 'ip': row['ip']})
    return credz

def main():
    """Our runtime code that calls other functions"""
    # Read connection information from the external file
    credz = read_connections('connections.csv')

    # describe the connection data
    # Removed the hardcoded credz list since we are reading it from the file

    # Retrieve the private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # rest of your code...
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for cred in credz:
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        # Write the output of the ls command to results.log
        explanation = f"Results for {cred.get('un')} @ {cred.get('ip')} on {now}:\n"
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))
        output = sessout.read().decode('utf-8')
        with open('results.log', 'a') as file:
            file.write(explanation + output + "\n")

        sshsession.close()

    print("Thanks for looping with Alta3!")

main()

