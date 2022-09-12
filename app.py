from flask import Flask, render_template
import calendar

tako = Flask(__name__)
nombre = "Juan"

@tako.route('/')
def helloworld():
    return render_template("a.html", nombre = nombre)
 
@tako.route('/tako.html')
def helloworld2():
    return render_template("tako.html")


#port = 8080

if __name__ == "__main__":
    tako.run(host = "0.0.0.0", debug = True)