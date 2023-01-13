import requests


class Wordpress:
    def __init__(self, website):
         self.url = website + "/wp-json/wp/v2/posts?per_page=100"

    def get_posts(self):
        response = requests.get(url=self.url, headers={}).json()
        return response


if __name__ == "__main__":
    data = Wordpress("https://techcrunch.com").get_posts()
    print(data)
