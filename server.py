from flask import Flask, jsonify, Response
import typing
list = typing.List
dict = typing.Dict
app: Flask = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

events: list[dict[str, str]] = []
with open("data.csv", encoding="utf-8") as f:
    for line in f.readlines():
        event_name, date, location = line.strip().split(", ")
        events.append({
            "event_name": event_name,
            "date": date,
            "location": location
        })


@app.route("/events")
def return_events() -> Response:
    d: dict[str, list[dict[str, str]]] = {"events": events}
    res: Response = jsonify(d)
    return res


if __name__ == "__main__":
    app.run(debug=True)
