import requests

print("Enter the url without http and www example: google.com or example.tr")
url = raw_input("Target url: ")


def request(url):
    try:
        return requests.get("http://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        pass


with open("/root/PycharmProjects/path_finder/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        target_url = url + "/" + line.strip()
        response = request(target_url)
        if response:
            print("[+] Discovered Path --> " + target_url)
