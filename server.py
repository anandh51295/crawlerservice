import subprocess

from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    spider_name = "mongodemo"
    lnk=request.json['url']
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-a", "start_url="+lnk, "-o", "output.json"])
    ok=201
    with open("output.json") as items_file:
        return items_file.read(),ok

if __name__ == '__main__':
    app.run(debug=True)