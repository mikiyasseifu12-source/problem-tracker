from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///problems.db'
db = SQLAlchemy(app)

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    solved = db.Column(db.Boolean, default=False)

@app.route('/')
def hello():
    return {"message": "Hello, World!"}

@app.route('/problems')
def get_problems():
    problems = Problem.query.all()
    return {"problems": [{"id": p.id, "title": p.title, "solved": p.solved} for p in problems]}

@app.route('/problems/<int:id>', methods=['DELETE'])
def delete_problem(id):
    problem = Problem.query.get(id)
    if not problem:
        return {"message": "Problem not found"}, 404
    db.session.delete(problem)
    db.session.commit()
    return {"message": "Problem deleted"}

@app.route('/problems/<int:id>', methods=['PUT'])
def update_problem(id):
    problem = Problem.query.get(id)
    if not problem:
        return {"message": "Problem not found"}, 404
    data = request.get_json()
    problem.title = data.get('title', problem.title)
    problem.solved = data.get('solved', problem.solved)
    db.session.commit()
    return {"message": "Problem updated", "id": problem.id}

with app.app_context():
    db.create_all()

@app.route('/problems', methods=['POST'])
def add_problem():
    data = request.get_json()
    new_problem = Problem(title=data['title'], solved=data.get('solved', False))
    db.session.add(new_problem)
    db.session.commit()
    return {"message": "Problem added", "id": new_problem.id}

if __name__ == '__main__':
    app.run(debug=True)
