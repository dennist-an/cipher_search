import json
import re
import requests
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)
            
# Function to make the API request
def fetch_ciphersuite_data():
    api_url = "https://ciphersuite.info/api/cs"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch data. Error: {e}")
        return None

# Your API response
api_data = fetch_ciphersuite_data()

def search_ciphersuites(hex_byte_1, hex_byte_2):
    matching_ciphersuites = []
    for ciphersuite in api_data.get("ciphersuites", []):
        for key, value in ciphersuite.items():
            if (
                "hex_byte_1" in value and value["hex_byte_1"] == hex_byte_1
                and "hex_byte_2" in value and value["hex_byte_2"] == hex_byte_2
            ):
                matching_ciphersuites.append({key: value})
    return matching_ciphersuites

def print_colored_result(result):
    for entry in result:
        for ciphersuite, details in entry.items():
            openssl_name = details.get('openssl_name', 'N/A')
            security_status = details.get("security")
            if security_status == "secure" or security_status == "recommended":
                json_response = json.dumps({ciphersuite: details["security"]}, indent=2)
                # Parse the JSON response
                data = json.loads(json_response)

                # Iterate through key-value pairs and print values
                for key, value in data.items():
                    print(Fore.GREEN + f"{ciphersuite} is {value}" )
            else:
                json_response = json.dumps({ciphersuite: details["security"]}, indent=2)
                # Parse the JSON response
                data = json.loads(json_response)

                # Iterate through key-value pairs and print values
                for key, value in data.items():
                    print(Fore.RED + f"{ciphersuite} is {value}" )
# Specify the path to your file
file_path = './file.txt'

# Define a regular expression pattern to match hex values
hex_pattern = re.compile(r'0x[0-9A-Fa-f]+,\s0x[0-9A-Fa-f]+')

# Open and read the file containing the following from Nessus SSL Cipher Suites Supported result
"""
ECDHE-RSA-AES128-SHA256 0xC0, 0x2F ECDH RSA AES-GCM(128)
SHA256
ECDHE-RSA-AES256-SHA384 0xC0, 0x30 ECDH RSA AES-GCM(256)
SHA384
ECDHE-RSA-CHACHA20-POLY1305 0xCC, 0xA8 ECDH RSA ChaCha20-Poly1305(256)
SHA256
"""
with open(file_path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Find all matches of the hex pattern in the line
        hex_matches = hex_pattern.findall(line)
        
        # Print each pair of hex values
        for hex_pair in hex_matches:
            # Extract individual hex values
            # Remove commas and split the string into individual hex values
            hex_values = hex_pair.replace(",", "").split()

            # Now you can use hex_values[0] and hex_values[1] as strings in your function
            param1 = hex_values[0]
            param2 = hex_values[1]

            # Call your function with the extracted hex values
            result = search_ciphersuites(param1, param2)

            # Print the colored result
            print_colored_result(result)
