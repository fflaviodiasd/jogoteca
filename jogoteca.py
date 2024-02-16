from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'alura'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    '{SGBDB}://{usuario}:{senha}@{servidor}/{database}?auth_plugin=mysql_native_password'.format(
        SGBDB= 'mysql+mysqlconnector',
        usuario= 'root',
        senha= '1234',
        servidor= '127.0.0.1',
        database= 'jogoteca'
    )

db = SQLAlchemy(app)

app.run(debug=True)