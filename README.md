# cipher_search

This script is designed to check the security status of SSL cipher suites based on their hexadecimal values. It utilizes an API from [ciphersuite.info](https://ciphersuite.info/api/cs) to fetch data about various cipher suites and then matches them against provided hexadecimal values.

## Prerequisites

Make sure you have Python 3 installed on your system.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dennist-an/cipher_search.git
    ```

2. Navigate to the cloned repository:

    ```bash
    cd cipher_search
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have a text file containing SSL cipher suite data. The format should be as follows (you could paste the results from Nessus):

    ```
    ECDHE-RSA-AES128-SHA256 0xC0, 0x2F ECDH RSA AES-GCM(128)
    SHA256
    ECDHE-RSA-AES256-SHA384 0xC0, 0x30 ECDH RSA AES-GCM(256)
    SHA384
    ECDHE-RSA-CHACHA20-POLY1305 0xCC, 0xA8 ECDH RSA ChaCha20-Poly1305(256)
    SHA256
    ```

2. Run the script and provide the path to your text file:

    ```bash
    python cipher_search.py
    ```

3. The script will process the provided hexadecimal values, fetch corresponding cipher suite details, and display the security status in colored output.