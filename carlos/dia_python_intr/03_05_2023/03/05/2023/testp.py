import json
json_str = '{"nome": bele, "nascimento": 02/12/2006}'
json_obj = list(json.loads(json_str))

with open('19_04_2023.json', 'w') as f:
    string = json.dumps(json_obj, indent=4)
    f.write(string)