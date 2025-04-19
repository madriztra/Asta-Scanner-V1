# AstaScannerV1 🚀

## Installation ⚙️

1. **Clone or download the project**:

    ```bash
    git clone https://github.com/username/asta-scanner.git
    cd asta-scanner
    ```

2. **(Optional) Create and activate a virtual environment**:

    - **Linux/macOS**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    - **Windows**:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage 💻

1. Run the `asta.py` script:

    ```bash
    python asta.py
    ```

2. Enter the **domain** or **IP** of the target you want to scan and select the appropriate protocol (`http` or `https`).

## Features 🎯

### 1. WHOIS Information

Collects information about the ownership of the domain and other related data, such as email addresses or administrative contacts.

### 2. DNS Lookup

Allows you to check the IP addresses associated with the target domain. This is important for network mapping or further analysis of server configuration.

### 3. CMS/Framework Detection

AstaScannerV1 can detect if the website is using a specific CMS or framework (such as WordPress, Joomla, or Drupal). This helps identify the technology used and potential vulnerabilities.

### 4. Admin Panel Finder

This feature searches for commonly used admin panel URLs, such as `/admin` or `/wp-admin`, to expose potential entry points to the system.

### 5. Nmap Scan

Performs port scanning to find open ports, such as those for SSH, HTTP, HTTPS, and FTP. This can help identify services running on the target server.

### 6. Nuclei Scan

Vulnerability scanning using **Nuclei** to detect potential vulnerabilities based on available exploit templates.

### 7. Auto Exploit

When a CMS is detected, AstaScannerV1 can attempt to automatically execute exploits against the CMS, if exploit scripts are available within the tool.

## Contributing 🤝

If you're interested in contributing to the development of **AstaScannerV1**, you can submit **pull requests** or report bugs by opening **issues**.

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
