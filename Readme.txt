Certainly! Here’s the updated `README.txt` that includes a note about setting the execute permissions for `install.sh`:

---

# Fileshare.py

## Overview

`Fileshare.py` is a script designed to send files or folders from one machine to another over various protocols. You can specify the method of transfer, such as SCP, FTP, SFTP, or RSYNC. The script also supports debugging mode to help with troubleshooting.

## Features

- **Send files or folders** to a remote machine.
- **Choose transfer method**: SCP, FTP, SFTP, or RSYNC.
- **Debug mode** for detailed error reporting.
- **Command-line arguments** for flexible usage.

## Prerequisites

Before running the script, ensure that you run the install script:

## Installation

1. **Make the installation script executable:**

    ```bash
    chmod +x install.sh
    ```

2. **Run the installation script:**

    ```bash
    ./install.sh
    ```

   This script will install Python 3, pip, and all required libraries.

## Usage

### Basic Syntax

```bash
python3 Fileshare.py -f FILE -i IP -u USER -r REMOTE -w METHOD [-d]
```

### Arguments

- `-f FILE, --file FILE`  
  *Path to the file or folder to send.*

- `-i IP, --ip IP`  
  *IP address of the remote machine.*

- `-u USER, --user USER`  
  *Username of the remote machine.*

- `-r REMOTE, --remote REMOTE`  
  *Path on the remote machine to save the file.*

- `-w METHOD, --way METHOD`  
  *Method to send the file. Options: scp, ftp, sftp, rsync.*

- `-d, --debug`  
  *Enable debug mode.*

### Examples

**Send a file using SCP:**

```bash
python3 Fileshare.py -f /path/to/file -i 192.168.1.1 -u username -r /remote/path -w scp
```

**Send a folder using RSYNC:**

```bash
python3 Fileshare.py -f /path/to/folder -i 192.168.1.1 -u username -r /remote/path -w rsync
```

## Troubleshooting

If you encounter any issues:
- Check the command syntax.
- Ensure all required libraries are installed by running `./install.sh`.
- Use the `-d` flag for debug mode to get detailed error information.

## License

This script is provided "as-is" without warranty of any kind. Use it at your own risk.

---
