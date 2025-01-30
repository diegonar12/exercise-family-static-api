from flask import Flask, jsonify, request
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {"id": self._generate_id(), "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": self._generate_id(), "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": self._generate_id(), "first_name": "Jimmy", "last_name": "Jackson", "age": 5, "lucky_numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_Id = self._next_id
        self._next_id += 1
        return generated_Id

    def add_member(self, member):
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return {"done": True}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return {"done": False}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
