from flask import Flask, render_template
import src.audio_prueba as au
import subprocess

app = Flask(__name__)

# Creating simple Routes 
@app.route('/ejecutandoprograma')
def test():
    subprocess.Popen(["python3","-c","import src.audio_prueba as au\nau.conversacion()"])
    return "Home Page"

@app.route('/ejemplos')
def ejemplo():
    return render_template("ejemplos.html")

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/asistentevirtual', strict_slashes=False)
def about():
    
    #conversaciones = au.conversacion()
    return render_template("asistentevirtual.html")

# Make sure this we are executing this file
if __name__ == '__main__':
   app.run(debug=True)