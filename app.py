from flask import Flask, request, jsonify
from db import insert_event, get_all_events
from utils import parse_event

app = Flask(__name__)

@app.route('/')
def home():
    return 'GitHub Webhook Listener is running'

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    print("Event Type:", event_type)
    print("Payload:", payload)

    data = parse_event(event_type, payload)
    print("Parsed Data:", data)

    if data:
        insert_event(data)
        return 'Event stored', 200
    return 'Ignored', 400


@app.route('/logs', methods=['GET'])
def logs():
    events = get_all_events()
    result = []
    for e in events:
        formatted = {
            "action": e["action"],
            "author": e["author"],
            "timestamp": e["timestamp"].strftime('%d %B %Y - %I:%M %p UTC')
        }
        if e["action"] == "push":
            formatted["to_branch"] = e["to_branch"]
        else:
            formatted["from_branch"] = e["from_branch"]
            formatted["to_branch"] = e["to_branch"]
        result.append(formatted)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
