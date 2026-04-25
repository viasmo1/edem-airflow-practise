import requests


class Wordpress:
    def __init__(self, website):
        self.api_version = "v2"
        self.url = f"{website}/wp-json/wp/{self.api_version}/posts?per_page=100"

    def get_posts(self):
        response = requests.get(url=self.url, headers={}).json()
        return response


if __name__ == "__main__":
    data = Wordpress("https://techcrunch.com").get_posts()
    print(data)
