import subprocess
from flask_pymongo import PyMongo

from flask import Flask, request, json, jsonify

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:12345@ds239097.mlab.com:39097/demo'
app.config['MONGO_DBNAME'] = 'demo'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/',methods=['POST'])
def hello_world():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output1.json"

    wait for  this command to finish, and read output1.json to client.
    """
    spider_name = "mongodemo"
    lnk=request.json['url']
    name=request.json['project_name']
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-a", "start_url="+lnk])
    ok=201
    ls=[]
    # with open("output.json") as items_file:
    with open("output.text") as items_file:
        id=items_file.read()
        id.strip()
        for x in id.split(','):
            ls.append(x)

    f = open('output.text', 'r+')
    f.truncate()
    f.close()
    data = {}
    data['links'] = []
    data['links'].append(ls)

    data['project']=name
    # return jsonify({'list': data})

    with open('output.json', 'w') as outfile:
        json.dump(data, outfile)
    mongo.db.projectdetails.insert(data)
    data.clear()
    ls.clear()
    with open('output.json') as items:
        return items.read(),ok


if __name__ == '__main__':
    app.run(debug=True)