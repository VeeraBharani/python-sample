from flask import Flask, request
from model import * 
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/events', methods=["POST"])
def register_page():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            c, conn = connection() 
            res = create_event(name)
            if (res['success'] == 'true'):
                rows = get_event_summary()
                if rows:
                    events_count = rows[1]
                    events_count += 1
                    update_event_summary(events_count)
                else:
                    events_count = 1
                    insert_event_summary(1)
                conn.commit()
                msg = "Record successfully added! Events count is " + str(events_count)
        except Exception as e:
            conn.rollback()
            msg = "Error while connecting to MySQL: " + str(e)
        finally:
            return msg
            conn.close()

if __name__ == '__main__':
   app.run(debug=True)
