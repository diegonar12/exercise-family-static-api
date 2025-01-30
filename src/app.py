"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

jackson_family = FamilyStructure("Jackson")

app = Flask(__name__)

@app.route("/members", methods=["GET"])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route("/member/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route("/member", methods=["POST"])
def add_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Invalid request"}), 400
    new_member = jackson_family.add_member(data)
    return jsonify(new_member), 200

@app.route("/member/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)