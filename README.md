# NoScope

NoScope is a Python-based tool designed for network analysis and security testing. It provides functionalities such as domain name resolution, IP address expansion, and URL sanitization to assist in the evaluation of network resources and security postures. By leveraging `NoScope`, users can quickly resolve domain names to IP addresses, expand IP ranges, and assess URLs for potential security concerns.

## Features

- **Domain Resolution**: Resolve domain names to IP addresses, automatically handling both direct domain names and those prefixed with `www`.
- **IP Expansion**: Expand IP ranges (e.g., `192.168.0.1/24`) to list all encompassed IP addresses.
- **URL Sanitization**: Strip URLs to their base components for easier analysis.
- **Visual Output**: Generate tables of IPs and URLs for analysis, highlighting specific IPs of interest.
- **Duplicate Detection**: Identify and report duplicate IP addresses within input data.

## Installation

Before installing NoScope, ensure you have Python 3.x installed on your system. You will also need to install the required dependencies. To do this run the startup script:

```bash
sudo ./setup
```

## Usage

To use NoScope, run the following command from the terminal, replacing `filename.txt` with the path to your input file:

```bash
NoScope filename.txt
```

The input file should contain IP addresses, IP ranges, or URLs (one per line). The tool will process these inputs to resolve IPs, expand ranges, and sanitize URLs as configured.

## Input File Format

The input file can include:
- Single IP addresses (e.g., `192.168.1.1`)
- IP ranges using CIDR notation (e.g., `192.168.1.0/24`)
- URLs (e.g., `https://example.com`)

Each entry should be on a separate line.