# Code Injector Tool

The Code Injector Tool is a Python script that uses Scapy and NetfilterQueue to intercept and modify network traffic, specifically HTTP responses. This tool allows you to inject custom code into the HTML response body and perform keyword replacement in the HTTP response. 

## Requirements

- Python 3.x
- Scapy
- NetfilterQueue

## Installation

1. Clone or download the repository to your local machine.

2. Install the required dependencies using pip:

```sh
pip install scapy netfilterqueue
```

## Usage

1. Open a terminal and navigate to the directory containing the `code_injector.py` script.

2. Run the script as root (administrator) using the following command:

```sh
sudo python3 code_injector.py
```

3. The script will start intercepting network traffic and analyzing HTTP responses.

4. When an HTTP response is intercepted and matches the specified conditions, the tool will inject custom code into the response body and modify the Content-Length accordingly.

5. To modify the injected code or perform keyword replacement, locate the following section in the `code_injector.py` script and make the necessary changes:

```python
if "example.com" in load:  # Replace "example.com" with your target keyword
    replacement_code = '<div>New Content Here</div>'
    load = load.replace("example.com", replacement_code)
```

Replace `"example.com"` with the keyword you want to replace and set the `replacement_code` to the custom code you wish to inject.

6. Press `Ctrl+C` in the terminal to stop the tool and exit gracefully.

## Important Notes

- This tool intercepts and modifies network traffic. Use it responsibly and only on networks you have permission to analyze.
- Be cautious while modifying response payloads, as improper modification may break functionality or introduce vulnerabilities.

## Disclaimer

This tool is provided for educational and research purposes only. The authr shall not be held responsible for any misuse or illegal activities conducted using this tool.

