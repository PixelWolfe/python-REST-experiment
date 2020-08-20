from flask import Flask, render_template, request

app = Flask(__name__)

serverList = ['test', 'test1']

def getServerList():
    return print(serverList)

def addToServerList():
    serverList.append('Post successful!')
    return 'Success Posting!'

def deleteFromServerList():
    if len(serverList) >= 1:
        serverList.remove(serverList[len(serverList)-1])
    return 'Deleted last entry!'
    
def editLastEntryServerList():
    serverList[len(serverList)-1]

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    if request.method == 'GET':
        return getServerList()
    elif request.method == 'POST':
        return addToServerList()
    elif request.method == 'DELETE':
        return deleteFromServerList()
    else:
        return editLastEntryServerList()


if __name__ == '__main__':
    app.run(debug=True)