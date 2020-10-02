from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Hallo Welt/Documents/GitHub/Todo_App/todo.db'
db = SQLAlchemy(app)
