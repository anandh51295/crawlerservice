import subprocess
from flask_pymongo import PyMongo
import pysitemap
from flask import Flask, request, json, jsonify
import os

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:12345@ds239097.mlab.com:39097/demo'
app.config['MONGO_DBNAME'] = 'demo'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/crawl/rip',methods=['POST'])
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

# @app.route('/crawl/flow',methods=['POST'])
# def sitemap():
#     # f = open('tst.json', 'r+')
#     # f.truncate()
#     # f.close()
#     spider = "sitemap"
#     lnk1=request.json['url']
#     # name1=request.json['project_name']
#     subprocess.check_output(['scrapy', 'crawl', spider, "-a", "start_url="+lnk1])
#     ok=201
#     # lt=[]
#     # with open("tst.json") as items_file:
#     #     id=items_file.read()
#     #     id.strip()
#     #     for x in id.split(','):
#     #         lt.append(x)
#     # val = {}
#     # val['children'] = []
#     # for i in lt:
#     #     if i in lnk1:
#     #         val['text']=i
#
#     with open('tst.json') as items:
#         return items.read(),ok

@app.route('/crawl/sitemap', methods=['POST'])
def map():
    os.remove("sitemap.xml")
    ok=201
    lnk2 = request.json['url']
    url = 'https://muditasol.weebly.com'  # url from to crawl
    logfile = 'errlog.log'  # path to logfile
    oformat = 'xml'  # output format
    crawl = pysitemap.Crawler(url=lnk2, logfile=logfile, oformat=oformat)
    crawl.crawl()
    with open('sitemap.xml') as items:
        return items.read(), ok


# @app.route('/file',methods=['POST'])
# def auto():
#     """
#     Run spider in another process and store items in file. Simply issue command:
#
#     > scrapy crawl dmoz -o "output1.json"
#
#     wait for  this command to finish, and read output1.json to client.
#     """
#
#     # f = open('at.json', 'r+')
#     # f.truncate()
#     # f.close()
#     lnk24 = request.json['url']
#     spider = "values"
#     lnk23=request.json['main']
#     ok=201
#     # f = open('values.json', 'r+')
#     # f.truncate()
#     # f.close()
#     # name1=request.json['project_name']
#     # with open('at.json', 'w+') as outfile:
#     #     json.dump(lnk23, outfile)
#
#     subprocess.check_output(['scrapy', 'crawl', spider, "-a", "start_url="+lnk24])
#
#
#     # with open("output.json") as items_file:
#
#     # return jsonify({'list': data})
#     # f = open('at.json', 'r+')
#     # f.truncate()
#     # f.close()
#
#     with open('values.json') as items:
#         return items.read(),ok


if __name__ == '__main__':

    app.run(debug=True)