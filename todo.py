from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:\Users\Hallo Welt\Documents\GitHub\Todo_App'
db = SQLAlchemy(app)
