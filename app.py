from flask import Flask
tako = Flask(__name__)
 
@tako.route('/')

def helloworld():
    return "hello world"

#port = 8080

if __name__ == "__main__":
    tako.run(host = "0.0.0.0", debug = True)