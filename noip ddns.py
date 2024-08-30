import requests
import base64
import time

while True:
    try:
        def update_no_ip(username, password, hostname):
            auth_string = f"{username}:{password}"
            base64_auth = base64.b64encode(auth_string.encode()).decode()

            headers = {
                "Authorization": f"Basic {base64_auth}",
            }

            url = "http://dynupdate.no-ip.com/nic/update"
            params = {
                "hostname": hostname
            }
            

            response = requests.get(url, headers=headers, params=params)


            print(f"Response: {response.text}")

        if __name__ == "__main__":

            username = "username@outlook.com"
            password = "password"
            hostname = "hostname.ddns.net"
            update_no_ip(username, password, hostname)
            time.sleep(60)

    except Exception as e:
                 print(e)        