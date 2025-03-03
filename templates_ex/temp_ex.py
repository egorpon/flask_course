from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/report_page')
def report_page():
    username = request.args.get('username')
    last_character_isdigit = any([char[-1].isdigit() for char in username])
    is_upper_character = any([char.isupper() for char in username ])
    is_lower_character = any([char.islower() for char in username])

#     last_character_isdigit==True and is_lower_character==True and
#   is_upper_character ==True
    report = last_character_isdigit and is_lower_character and is_upper_character
    
    
    return render_template('report_page.html',report=report,last_character_isdigit=last_character_isdigit,is_lower_character=is_lower_character,is_upper_character=is_upper_character)


if __name__ == '__main__':
    app.run(debug=True)