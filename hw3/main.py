import json
import sys
import re


variables = {}
name = r'[a-zA-Z_]\w*'


def parse_value(value, key=None):
    global variables
    if isinstance(value, (int, float)):
        if key:
            variables[key] = value
        return str(value)
    elif isinstance(value, list):
        if key:
            variables[key] = value
        return "{" + ", ".join(parse_value(v) for v in value) + "}"
    elif re.match(fr"^({name}|\d+)\s[+\-/*]\s({name}|\d+)$", str(value)):
        val = str(value).split()
        if ((not val[0].isdigit() and val[0] in variables or val[0].isdigit()) and
            (not val[2].isdigit() and val[2] in variables or val[2].isdigit())):
            value = eval(f'{variables.get(val[0], val[0])} {val[1]} {variables.get(val[2], val[2])}')
        else:
            raise ValueError(f"Invalid value: {value}")
        if key:
            variables[key] = value
        return f'[{val[1]} {val[0]} {val[2]}]'
    elif re.match(fr"^sort\({name}\)$", str(value)):
        val = str(value)[5:-1]
        if val in variables and type(variables[val]) == list:
            value = sorted(variables[val])
        else:
            raise ValueError(f"Invalid value: {value}")
        if key:
            variables[key] = value
        return "[sort " + val + "]"
    else:
        raise ValueError(f"Invalid value: {value}")

def parse_json(data):
    global variables
    output = []
    for key, value in data.items():
        if not re.match(r'^[a-zA-Z_]\w*$', key):
            raise ValueError(f"Invalid name: {key}")
        output.append(f"{key} is {parse_value(value, key)};")
    return "\n".join(output)


def translate(json_input):
    try:
        data = json.loads(json_input)
        return parse_json(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decode error: {e}")
    except ValueError as e:
        raise ValueError(f"Error: {e}")


if __name__ == '__main__':
    json_input = sys.stdin.read()
    try:
        output = translate(json_input)
        print(output)
    except Exception as e:
        print(e, file=sys.stderr)
