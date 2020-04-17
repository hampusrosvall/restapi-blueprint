from app import app, db 
import os 

db.init_app(app)

@app.before_first_request
def createa_tables(): 
    db.create_all()

if __name__ == '__main__': 
    app.run(host='0.0.0.0')