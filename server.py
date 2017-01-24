from flask import Flask
from flask.templating import render_template
from sign_in import sign_in
from sign_up import sign_up

app = Flask(__name__)



def create_app():
    app = Flask(__name__)
    app.register_blueprint(sign_in)
    app.register_blueprint(sign_up)
    return app


def main():
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

        
if __name__ == '__main__':
    main()
    
    
    
    
    