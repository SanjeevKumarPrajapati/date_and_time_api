from flask import Flask
import datetime
app=Flask(__name__)

@app.route("/")
def home():
    a=datetime.datetime.now()
    return {"Hours:- ":a.strftime("%H"),"Minutes :- ":a.strftime("%M"),"Seconds :- ":a.strftime("%S"),"Day Name :-":a.strftime("%A"),
            "Month Name :- ":a.strftime("%B"),"Year :- ":a.strftime("%Y")}

if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')
