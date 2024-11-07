
# 🔍 Port Scanner

A simple yet powerful port scanner built in Python that allows you to check for open ports on a specified IP address. This tool can help network administrators and security enthusiasts identify services running on a target machine.

## 📦 Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.6 or higher**: This program uses Python features that require at least version 3.6.
- **pip**: Python's package installer should be installed (comes with Python installations). 

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hari9602/Port_Scanner.git
   cd Port_Scanner
   ```

2. **Install required packages**:
   This project uses the `colorama` library for colored output in the terminal. Install it using pip:
   ```bash
   pip install colorama
   ```

## 🚀 Usage

To run the port scanner, use the following command in your terminal:

```bash
python port_scanner.py <target_ip> <start_port-end_port>
```

### Example:

To scan the IP address `192.168.1.1` for open ports from `1` to `1024`, you would run:

```bash
python advanced_port_scanner.py 192.168.1.1 1-1024
```

### Output

The output will display open ports along with their corresponding service names. If no open ports are found, you will receive a message indicating that all ports are closed.

## 🛠️ Features

- Multithreaded scanning for faster results.
- Displays service names for common ports.
- User-friendly output with colored text.
- Notifies when no open ports are found.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---
---
***Thank you for checking out my Advanced Port Scanner! Happy scanning! 🔍✨***

