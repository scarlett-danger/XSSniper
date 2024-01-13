# XSSniper

XSSniper is a powerful tool designed to scan for and exploit Cross-Site Scripting (XSS) vulnerabilities. It provides automated scanning capabilities for reflected XSS, stored XSS, and DOM-based XSS attacks. This tool is intended for educational and ethical purposes only.

## Features

- Enumerate subdomains using a wordlist file
- Scan for reflected, stored, and DOM-based XSS vulnerabilities
- Exploit detected vulnerabilities by sending payloads
-
## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/XSSniper.git
   ```

2. Install the required dependencies:

   ```shell
   pip install requests
   ```

## Usage

1. Run the XSSniper script:

   ```shell
   python xssniper.py target_domain wordlist_file
   ```

   - `target_domain` - The target domain to scan for XSS vulnerabilities.
   - `wordlist_file` - The path to the wordlist file containing subdomains to enumerate.

2. Wait for the scan to complete. XSSniper will scan each subdomain, check for XSS vulnerabilities, and exploit them if found.

3. Review the scan results in the terminal. XSSniper will display any detected vulnerabilities and indicate whether exploitation was successful.

## Disclaimer

XSSniper is a tool intended for educational and ethical purposes only. The author and contributors are not responsible for any misuse or illegal activities performed with this tool. Use it at your own risk and make sure to comply with all applicable laws and regulations.

## License

XSSniper is released under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.