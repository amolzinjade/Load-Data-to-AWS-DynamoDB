import json
import boto3  # import Boto3



def load_data(persons, dynamodb=None):
    dynamodb = boto3.resource('dynamodb',region_name='',verify=False,aws_access_key_id="",aws_secret_access_key="")

    person_table = dynamodb.Table('test_person')

    for person in persons:

        new_item = {
            "personId":persons["personId"],
            "name":persons["name"],
            "Salary":persons["Salary"],
            "Department":persons["Department"],
            "country":persons["country"],
            "Designation":persons["Designation"]
        }

        person_table.put_item(Item=new_item)

if __name__ == '__main__':
    # open file and read all the data in it
    with open("data.json") as json_file:
        person_list = json.load(json_file)
        load_data(person_list)

