from project_code.connector.wordpress import Wordpress
import json
import os


class WordpressETL:
    def main(self):
        print("START ETL")

        webpages = {"ted": "https://blog.ted.com"}

        for web_name, web_url in webpages.items():
            print(f"Downloading posts from {web_url}")
            posts = Wordpress(web_url).get_posts()

            print(f"Saving posts in {web_name}.json")
            filename = f"/opt/airflow/posts/{web_name}/{web_name}.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(posts, f, indent=4)

        print("END")
