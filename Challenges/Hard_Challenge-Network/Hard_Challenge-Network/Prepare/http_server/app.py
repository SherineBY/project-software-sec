from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "HTTP Server Active."

@app.route('/response', methods=['GET'])
def hidden_data():
    return "hidden_flag_part_3:CTF_hidden"  # Partial flag content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
