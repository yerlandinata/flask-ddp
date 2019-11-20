from flask import Flask, request

app = Flask(__name__)

message_element = '<div class="card mb-3"><div class="card-body"><p class="card-text">MSG</p><p class="card-text"><small class="text-muted">An Imperial Starship intercepted this rebel\'s message</small></p></div></div>'

def read_db():
    db = []
    with open('db.txt', 'r') as f:
        for line in f:
            db.append(line)
    return db[::-1]

def write_db(message):
    with open('db.txt', 'a') as f:
        f.write(message.replace('<', '').replace('>', '').replace('(', '').replace(')', '') + '\n')

def render(messages):
    with open('index.html', 'r') as f:
        html = f.read()
    msg_elements = ''.join([message_element.replace('MSG', m) for m in messages])
    return html.replace('MSG', msg_elements)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        print(request.form)
        write_db(request.form['message'])
    return render(read_db())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51236)

