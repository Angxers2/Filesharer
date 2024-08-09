import argparse
import subprocess
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Send a file or folder to a remote machine.\nArguments with * are required."
    )
    
    parser.add_argument('-f', '--file', type=str, required=True, help='* Path to the file or folder to send.')
    parser.add_argument('-i', '--ip', type=str, required=True, help='* IP address of the remote machine.')
    parser.add_argument('-u', '--user', type=str, required=True, help='* Username of the remote machine.')
    parser.add_argument('-r', '--remote', type=str, required=True, help='* Path on the remote machine to save the file.')
    parser.add_argument('-w', '--way', type=str, choices=['scp', 'ftp', 'sftp', 'rsync'], required=True, help='* Method to send the file.')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode.')
    
    return parser.parse_args()

def send_file():
    """ Send the file or folder based on user choice. """
    if args.way == 'scp':
        command = f"scp {args.file} {args.user}@{args.ip}:{args.remote}"
    elif args.way == 'ftp':
        command = f"ftp {args.user}@{args.ip}"
    elif args.way == 'sftp':
        command = f"sftp {args.user}@{args.ip}:{args.remote}"
    elif args.way == 'rsync':
        command = f"rsync -avz {args.file} {args.user}@{args.ip}:{args.remote}"
    else:
        print("Invalid method specified.")
        sys.exit(1)

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        if args.debug:
            print(f"Error sending file: {e}")
        else:
            print("An error occurred while sending the file. Refer to the help with -h.")
        sys.exit(1)

def main():
    global args
    args = parse_arguments()
    
    if args.debug:
        print(f"Debug mode enabled.")
    
    send_file()

if __name__ == "__main__":
    main()
