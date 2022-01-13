from cgi import print_environ_usage 
from flask import Flask
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  


@app.route('/Dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def show_user_profile(name):
    print(name)
    return "Hi " + (name.capitalize()) +"!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num,word):
    # return (num * word)
    output = ""
    for i in range(0,num):
        output += f"<h2>{word}</h2>"
    return output

if __name__=="__main__":   
    app.run(debug=True)   

