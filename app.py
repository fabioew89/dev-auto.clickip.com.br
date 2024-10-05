from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def principal(debug=True):
    fruta1 = 'uva'
    fruta2 = 'maca'
    fruta3 = 'laranja'
    fruta4 = 'morango'
    return render_template('index.html', 
                           fruta1=fruta1,
                           fruta2=fruta2,
                           fruta3=fruta3,
                           fruta4=fruta4)

@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')

# http://localhost:5000


if __name__ == "__main__":
    app.run(debug=True)