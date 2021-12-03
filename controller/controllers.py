from werkzeug.utils import redirect
from app import app
from flask import render_template, request
from models.event_list import events, add_new_event, delete_event
from models.event import Event
from datetime import date as date_f

@app.route('/events')
def index():
    return render_template('index.html', title = "Home of Events", events = events)

@app.route('/events', methods=['POST'])
def add_event():
    form = request.form
    name = form["name"]
    date_original = [int(x) for x in form["date"].split("-")]
    date = date_f(date_original[0], date_original[1], date_original[2])
    guests = form["guests"]
    room = form["room"]
    description = form["description"]
    recurring = True if 'recurring' in form else False
    new_event = Event(date, name, guests, room, description, recurring)
    add_new_event(new_event)
    return redirect("/events")

@app.route('/events/<id>')
def event(id):
    sevent = events[int(id)]
    return render_template('event.html', title = sevent.name, event = sevent)

@app.route('/events/delete/<id>', methods=['POST'])
def delete_given_event(id):
    try:
        int(id)
    except:
        actual_id = events.index([event for event in events if event.name == id][0])
        delete_event(actual_id, events)
    else:
        delete_event(int(id), events)
    return redirect("/events")

# @app.route('/events/delete-by-name/<name>', methods=["POST"])
# def delete_given_event_name(name):
#     id = events.index([event for event in events if event.name == name][0])
#     delete_event(id, events)
#     return redirect("/events")
