from flask import Flask , render_template
import psutil

app = Flask(__name__)

@app.route("/")     
def index():
    cpu_metric = psutil.cpu_percent(interval=1)  # Specify interval for CPU measurement
    mem_metric = psutil.virtual_memory().percent
    message = None
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)
#   return f"CPU Utilization: {cpu_metric}% and Memory Utilization: {mem_metric}%\n"
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
