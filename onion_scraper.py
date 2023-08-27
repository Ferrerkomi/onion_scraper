import os
import sys
import requests

class OnionScraper:
    def __init__(self, onion_url, output_folder='output'):
        self.onion_url = onion_url
        self.output_folder = output_folder
        self.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        self.session = requests.Session()

    def access_onion_site(self):
        # Access the onion site using the configured proxies
        response = self.session.get(self.onion_url, proxies=self.proxies)
        content = response.text
        self.save_content(content)

        # Display information and cookies
        print("Website content and cookies saved in the '{}' folder.".format(self.output_folder))
        print("Cookies:")
        for cookie in self.session.cookies:
            print(cookie.name, ":", cookie.value)

        print("Script execution completed.")

    def save_content(self, content):
        # Create the output folder if it doesn't exist
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Save the website content to a file in the output folder
        with open(os.path.join(self.output_folder, 'website_content.txt'), 'w', encoding='utf-8') as content_file:
            content_file.write(content)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 {} <onion_url>".format(sys.argv[0]))
        sys.exit(1)

    # Get the onion URL from the command-line arguments
    onion_url = sys.argv[1]
    
    # Create an instance of the OnionScraper and access the onion site
    scraper = OnionScraper(onion_url)
    scraper.access_onion_site()

