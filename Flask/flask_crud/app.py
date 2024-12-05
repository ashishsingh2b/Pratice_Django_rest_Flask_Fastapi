# app.py

from flask import Flask, request, jsonify
from models import Student, session  # Import the Student model and session

app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to the home page"

@app.route("/students", methods=["GET"])
def get_students():
    students = session.query(Student).all()
    return jsonify([{"id": student.id, "first_name": student.first_name, "last_name": student.last_name, "age": student.age, "email": student.email} for student in students])

@app.route("/student/<int:id>", methods=["GET"])
def get_student(id):
    student = session.query(Student).filter_by(id=id).first()
    if student:
        return jsonify({"id": student.id, "first_name": student.first_name, "last_name": student.last_name, "age": student.age, "email": student.email})
    else:
        return "Student not found", 404

@app.route("/student", methods=["POST"])
def add_student():
    data = request.json
    new_student = Student(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        email=data['email']
    )
    session.add(new_student)
    session.commit()
    return jsonify({"message": "Student added", "student": {"id": new_student.id}}), 201

@app.route("/student/<int:id>", methods=["PUT"])
def update_student(id):
    student = session.query(Student).filter_by(id=id).first()
    if not student:
        return "Student not found", 404
    
    data = request.json
    student.first_name = data.get('first_name', student.first_name)
    student.last_name = data.get('last_name', student.last_name)
    student.age = data.get('age', student.age)
    student.email = data.get('email', student.email)
    
    session.commit()
    return jsonify({"message": "Student updated", "student": {"id": student.id}})

@app.route("/student/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = session.query(Student).filter_by(id=id).first()
    if not student:
        return "Student not found", 404
    
    session.delete(student)
    session.commit()
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True)
