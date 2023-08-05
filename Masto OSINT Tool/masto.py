import time
import json
import requests
from tqdm import tqdm
from w3lib.html import remove_tags
from bs4 import BeautifulSoup


class Masto:
    def __init__(self):
        pass

    # search username with Mastodon API
    def username_search_api(self, username):
        url = f"https://mastodon.social/api/v2/search?q={username}"
        response = requests.request("GET", url)
        data = json.loads(response.text)
        for _ in tqdm(range(10)):
            time.sleep(0.03)

        if response.text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
            return f"\nTarget username: [{username}] NOT found using the Mastodon API!"

        data = filter(
            lambda x: x.get("username").lower() == username.lower(), data["accounts"]
        )

        result_string = ''

        for index, intelligence in enumerate(list(data), start=1):
            result_string += "\n\n══════════"
            result_string += f"\nAccount: {index}\n"
            result_string += "══════════\n"

            identity = intelligence["id"]
            lock = intelligence["locked"]
            pro_url = intelligence["url"]
            target_username = intelligence["username"]
            account = intelligence["acct"]
            display = intelligence["display_name"]
            creation_date = intelligence["created_at"]
            bot = intelligence["bot"]
            discov = intelligence["discoverable"]
            fwers = intelligence["followers_count"]
            fwing = intelligence["following_count"]
            posts = intelligence["statuses_count"]
            laststatus = intelligence["last_status_at"]
            group = intelligence["group"]
            note = intelligence["note"]
            note = remove_tags(note)
            avatar = intelligence["avatar"]

            result_string += f"user ID: {identity}\n"
            result_string += f"profile url: {pro_url}\n"
            result_string += f"account locked: {lock}\n"
            result_string += f"username: {target_username}\n"
            result_string += f"account: {account}\n"
            result_string += f"display Name: {display}\n"
            result_string += f"profile creation date: {creation_date}\n"
            result_string += f"user is a bot: {bot}\n"
            result_string += f"user opted to be listed on the profile directory: {discov}\n"
            result_string += f"followers: {fwers}\n"
            result_string += f"following: {fwing}\n"
            result_string += f"number of posts: {posts}\n"
            result_string += f"user last message date: {laststatus}\n"
            result_string += f"user is a group: {group}\n"
            result_string += f"user bio: {note}\n"

            fields = []
            for field in intelligence.get("fields", []):
                name = field.get("name")
                value = field.get("value")

                if value and "</" not in value:
                    continue

                soup = BeautifulSoup(value, "html.parser")
                a = soup.find("a")
                if a:
                    fields.append(f'--> {name}: {a.get("href")}')
                    result_string += f"sites found:\n"
                else:
                    continue

                for field in fields:
                    result_string += f"\t {field}\n"

            result_string += f"\nuser's avatar link: {avatar}\n"

        return result_string

    # username search with the Masto OSINT Tool servers database
    def username_search(self, username):
        headers = {
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US;q=0.9,en;q=0,8",
            "accept-encoding": "gzip, deflate",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
            "Chrome/104.0.0.0 Safari/537.36",
        }

        response = requests.get(
            "https://raw.githubusercontent.com/C3n7ral051nt4g3ncy/Masto/master/fediverse_instances.json"
        )
        sites = response.json()["sites"]
        is_any_site_matched = False
        result_string = ''

        for site in sites:
            uri_check = site["uri_check"]
            site_name = site["name"]
            uri_check = uri_check.format(account=username)

            try:
                res = requests.get(uri_check, headers=headers)
                estring_pos = res.text.find(site["e_string"]) > 0
            except Exception as e:
                continue

            if res.status_code == 200 and estring_pos:
                is_any_site_matched = True
                result_string += f"[+] Target found ✓ on: {site_name}\n"
                result_string += f"Profile URL: {uri_check}\n"

        if not is_any_site_matched:
            result_string += f"\nTarget username: [{username}] NOT found on the Masto OSINT Tool servers database!\n"

        return result_string
