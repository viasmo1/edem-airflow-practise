from project_code.connector.wordpress_solution import Wordpress
import json
import os


class WordpressETL:
    def __init__(self, webpage_name: str, webpage_url: str) -> None:
        self.webpage_name = webpage_name
        self.webpage_url = webpage_url

    def main(self) -> None:
        print("START ETL")
        print(f"Downloading posts from {self.webpage_url}")
        posts = Wordpress(self.webpage_url).get_posts()

        print(f"Saving posts in {self.webpage_name}.json")
        filename = f"/opt/airflow/posts/{self.webpage_name}/{self.webpage_name}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=4)
        print("END")
