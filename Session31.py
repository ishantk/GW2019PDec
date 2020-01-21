# JSON: Java Script Object Notation
#       It is Dictionary represented as String
#       Dictionary can further have dictionary or Lists only and will always start as dictionary
import json
employee = {
            "eid": 101,
            "name": "John",
            "salary": 3000,
            "addresses":[
                            {"adrsLine": "Redwood Shores", "pin": 141001},
                            {"adrsLine": "Pristine Magnum", "pin": 141004}
                        ]
            }
print(employee, type(employee))

print()

# Covert Dictionary into JSON
jsonData = json.dumps(employee)
print(jsonData, type(jsonData))

# Directly convert the data into string
# Don't use this below technique for getting data as JSON
# jsonData = str(employee)
# print(jsonData, type(jsonData))


# Covert JSON into Dictionary
employeeData = json.loads(jsonData)
print(employeeData, type(employeeData))

