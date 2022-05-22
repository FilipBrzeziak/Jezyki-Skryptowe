from fastapi import FastAPI, HTTPException
import Person
import Valid

app = FastAPI()

people = {}


@app.get("/get-person-by-id/{person_id}")
def get_person(person_id: int):
    return people[person_id]


@app.get("/get-people-by-surname/")
def get_people_surname(lastname: str):
    result = []
    for person in people:
        if (person.last_name == lastname):
            result.append(person)
    return result


@app.get("/get-people/")
def get_people():
    return people


@app.post("/add-person/{person_id}")
def post_person(person_id: int, name: str, lastname: str, phone_number: str, email: str):
    if person_id in people:
        return {"Error": "Person with given ID already exist!"}
    if not Valid.valid_email(email):
        raise HTTPException(status_code=400, detail="Wrong email domain! Only PWR emails allowed!")
    if not Valid.valid_number(phone_number):
        raise HTTPException(status_code=400, detail="Wrong number format!")

    people[person_id] = Person.Person(name, lastname, phone_number, email)
    return people[person_id]


@app.delete("/delete-person-by-id/{person_id}")
def delete_person(person_id: int):
    if person_id not in people:
        return {"Error": "Person with given ID does not exist!"}
    del people[person_id]
