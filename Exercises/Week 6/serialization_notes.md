https://docs.python-guide.org/scenarios/serialization/

# Serializing Text

## Flat data

- repr - takes a single object parameter and returns a printable representation of the input:

- ast.literal_eval - safely parses and evaluates an expression for a Python datatype. Supported data types are: strings, numbers, tuples, lists, dicts, booleans, and None

## Nested Data

- YAML

        import yaml
        with open("dogs.yaml", "r", newline="") as f:
        try:
            print(yaml.load(f))
        except yaml.YAMLError as ymlexcp:
            print(ymlexcp)

- JSON

        import json

        # Reading data
        with open("dogs.json", "r") as f:
            data = json.load(f)

        # Writing data
        with open("dogs.json", "w") as f:
            json.dump(data, f, sort_keys = True)

# Binary

- Numpy

        import NumPy as np

        byte_output = np.array(....).tobytes()

        array_format = np.frombuffer(byte_output)

- Pickle

        import pickle

        grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

        serial_grades = pickle.dumps(grades)

        received_grades = pickle.loads(serial_grades)
