
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
 

@app.route("/about)
def about():
    return render_template("about.html")
    
if __name__ == "__lab_":
    app.run(debug=True)