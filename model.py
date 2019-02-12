from dbconnect import connection
import json

def create_event(name):
    try:
        c, conn = connection() 
        c.execute("INSERT INTO events (`name`) VALUES (%s) ",(name))
        conn.commit()
        return success_response(c.lastrowid)
    except Exception as e:
        conn.rollback()
        msg = "Error while connecting to MySQL: " + str(e)
        return error_response(msg)

def get_event_summary():
    try:
        c, conn = connection() 
        c.execute("select * from event_summary")   
        rows = c.fetchone()
        return rows
    except Exception as e:
        msg = "Error while fetching rows: " + str(e)
        return  msg

def update_event_summary(count):
    try:
        c, conn = connection() 
        c.execute("UPDATE event_summary SET event_count = %s WHERE id = 1", (count))
        conn.commit()
        return success_response()
    except Exception as e:
        msg = "Error while fetching rows: " + str(e)
        return  error_response(msg)


def insert_event_summary(count):
    try:
        c, conn = connection() 
        c.execute("INSERT INTO event_summary (event_count) VALUES (%s)", (events_count))
        conn.commit()
        return success_response()
    except Exception as e:
        msg = "Error while fetching rows: " + str(e)
        return  error_response(msg)

def success_response(data):
    response = {'success' : 'true', 'data' : data}
    return response

def error_response(data = ''):
    response = {'success' : 'false', 'data' : data}
    return response