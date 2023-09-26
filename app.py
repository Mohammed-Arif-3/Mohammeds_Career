# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def hello_world():
#     return"<p>Hello,World</p>"
from flask import Flask, app, render_template
app =Flask(__name__)
JOBS = [
    {
        'id':1,
    'title':'Software Engineer',
    'location':'New Mumbai, India',
    'salary':'Rs 10,00,000'
     },

      {
          'id':2,
    'title':'Frontend Engineer',
    'location':'Hyderabad, India',
    'salary':'Rs 15,00,000'
     },

      {
          'id':3,
    'title':'Backend Engineer',
    'location':'Remote',
    'salary':'Rs 18,00,000'
     },

      {
          'id':4,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs 20,00,000'
     }
]
@app.route("/")
def hello_mohammed():
    return render_template('index.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(debug=True)