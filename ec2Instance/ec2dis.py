import paramiko
import os

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname="13.235.79.150", username="ubuntu", key_filename="/Users/whynew/Python/ec2Instance/30_June_26.pem")
    
    # Run commands here
    stdin, stdout, stderr = client.exec_command("uptime")
    print(stdout.read().decode())

finally:
    # This block ALWAYS runs, ensuring proper disconnection
    client.close()
    print("Disconnected safely.")