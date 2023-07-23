# SCHEMAS MONGODB FORMAT JSON

def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:
    list_student_entiry = []
    for item in db_item_list:
        list_student_entiry.append(studentEntity(item))

    return list_student_entiry