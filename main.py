from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# APPLICATION WORKS!!
# cmdline to test site: flask --app main.py run -p 5000 

start_time = 0

@app.route("/")
def main():
    global start_time

    start_time = time.perf_counter_ns()
    return render_template('index.html')


@app.route("/time")
def get_time():
    x = record_time() 
    return {"time": f"{x['days']}d {x['hours']:02d}h {x['minutes']:02d}m {x['seconds']:02d}s"}


def record_time():
    # Total elasped is measured in ns
    final_time = time.perf_counter_ns() - start_time
    total_ms = final_time // 1_000_000
    
    total_seconds = total_ms // 1000
        
    seconds = total_seconds % 60
    total_minutes = total_seconds // 60
        
    minutes = total_minutes % 60
    total_hours = total_minutes // 60
        
    hours = total_hours % 24
    days = total_hours // 24

    return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
    }

