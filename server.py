from flask import Flask, jsonify, Response
from flask_cors import CORS
import typing
list = typing.List
dict = typing.Dict
app: Flask = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

events: list[dict[str, str]] = []
with open("data.csv", encoding="utf-8") as f:
    for line in f.readlines():
        event_name, description, event_period, location, image_url = line.strip().split(", ")
        events.append({
            "event_name": event_name,
            "description": description,
            "event_period": event_period,
            "location": location,
            "image_url": image_url
        })


@app.route("/")
def index() -> str:
    return "Hello"


@app.route("/events")
def return_events() -> Response:
    d: dict[str, list[dict[str, str]]] = {"events": events}
    res: Response = jsonify(d)
    return res


from random import choice
@app.route("/events/choice")
def choice_event() -> Response:
    res: Response = jsonify(choice(events))
    return res


if __name__ == "__main__":
    import os
    app.run(port=int(os.environ["PORT"]), host="0.0.0.0", debug=True)
