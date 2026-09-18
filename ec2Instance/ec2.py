import paramiko
import os

# Configuration details
hostname = "13.235.79.150"  # e.g., "54.210.12.34"
username = "ubuntu"           # Common default users: ec2-user, ubuntu, debian, centos
key_path = "/Users/whynew/Downloads/30_June_26.pem"

def connect_to_ec2(host, user, key_file):
    # Initialize SSH client
    client = paramiko.SSHClient()
    
    # Automatically add host key to known_hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"Connecting to {host}...")
        
        # Load the RSA private key
        key = paramiko.RSAKey.from_private_key_file(key_file)
        
        # Connect to the EC2 instance
        client.connect(hostname=host, username=user, pkey=key)
        print("Connected successfully!\n")
        
        # Execute a command on the EC2 instance
        command = "uname -a && uptime"
        stdin, stdout, stderr = client.exec_command(command)
        
        # Read and display the output
        print("Command Output:")
        print(stdout.read().decode())
        
        # Print errors if any occurred
        error_output = stderr.read().decode()
        if error_output:
            print("Errors:")
            print(error_output)

    except Exception as e:
        print(f"Failed to connect: {e}")
        
    finally:
        # Close the SSH connection
        client.close()
        print("Connection closed.")

if __name__ == "__main__":
    connect_to_ec2(hostname, username, key_path)