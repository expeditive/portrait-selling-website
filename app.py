from flask import Flask, render_template

app = Flask(__name__)

WORKS = [

    {
      'id':'1',
      'title':'Pencil Portrait',
      'size' : 'A4',
      'price':'400',
    },
    {
      'id':'2',
      'title':'Water color Portrait',
      'size' : 'A4',
      'price':'700',
    },
    {
      'id':'3',
      'title':'Pencil Portrait',
      'size' : 'A3',
      'price':'700',
    },
    {
      'id':'4',
      'title':'Water Color Portrait',
      'size' : 'A3',
      'price':'1000',
    }
  ]

@app.route('/')
def hello():
  return render_template('home.html',works=WORKS)

if __name__=='__main__':
  app.run(host='0.0.0.0',debug = True)