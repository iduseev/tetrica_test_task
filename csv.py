import csv
import requests


with open("data.csv") as csv_file, open("result.csv", mode="w") as file_writer:
    csv_reader = csv.reader(csv_file, delimiter=",")

    fieldnames=["uuid", "userId", "todo_id", "is_owner", "completed"]
    csv_writer = csv.DictWriter(file_writer, fielnames=fieldnames)
    csv_writer.writeheader()
    for idx, row in enumerate(csv_reader):
        if idx >= 50:
            break
        uuid = row[0]
        userId = int(row[1])
        todo_id = int(row[2])
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}/todos")
        result_json = response.json()
        if not result_json:
            print("userID is invalid!")
            continue

        result_dict = {
            "uuid": uuid,
            "userId": userId,
            "todo_id": todo_id,
            "is_owner": False,
            "completed": False
        }
        for i in result_json:
            id = i["id"]
            if id == todo_id:
                result_dict["is_owner"] = True
                result_dict["completed"] = i["completed"]

        csv_writer.writerow(result_dict)
