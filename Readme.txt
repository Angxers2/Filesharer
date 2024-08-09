

---

# Fileshare.py

## Overview

Fileshare.py is a Python script for transferring files or folders to a remote machine using various protocols. It supports SCP, FTP, SFTP, and RSYNC. It also includes a debug mode for troubleshooting.

## Features

- **File/Folder Transfer**: Send files or directories to a remote machine.
- **Multiple Protocols**: Choose from SCP, FTP, SFTP, or RSYNC.
- **Debug Mode**: Activate detailed error reporting.
- **Command-Line Arguments**: Simple and flexible usage.

## Prerequisites

- Python 3.x
- Required Python libraries

## Installation

1. **Make the installation script executable:**

    ```plaintext
    chmod +x install.sh
    ```

2. **Run the installation script:**

    ```plaintext
    ./install.sh
    ```

    The script will install Python 3, pip, and all required libraries. During installation, it will display an animation.

## Usage

### Basic Syntax

```plaintext
python3 Fileshare.py -f FILE -i IP -u USER -r REMOTE -w METHOD [-d]
```

## Arguments

- **`-f FILE, --file FILE`**  
  Path to the file or folder to send. *(REQUIRED)*

- **`-i IP, --ip IP`**  
  IP address of the remote machine. *(REQUIRED)*

- **`-u USER, --user USER`**  
  Username for the remote machine. *(REQUIRED)*

- **`-r REMOTE, --remote REMOTE`**  
  Destination path on the remote machine. *(REQUIRED)*

- **`-w METHOD, --way METHOD`**  
  Transfer method: `scp`, `ftp`, `sftp`, `rsync`. *(REQUIRED)*

- **`-d, --debug`**  
  Enable debug mode.

## Examples

**Send a file using SCP:**

```plaintext
python3 Fileshare.py -f /path/to/file -i 192.168.1.1 -u username -r /remote/path -w scp
```

**Send a folder using SCP:**

```plaintext
python3 Fileshare.py -f /path/to/folder -i 192.168.1.1 -u username -r /remote/path -w scp
```

**Send a file using FTP:**

```plaintext
python3 Fileshare.py -f /path/to/file -i 192.168.1.1 -u username -r /remote/path -w ftp
```

**Send a file using SFTP:**

```plaintext
python3 Fileshare.py -f /path/to/file -i 192.168.1.1 -u username -r /remote/path -w sftp
```

**Send a file using RSYNC:**

```plaintext
python3 Fileshare.py -f /path/to/file -i 192.168.1.1 -u username -r /remote/path -w rsync
```

---
