"""
This JSON schema defines the structure and validation rules for a data object representing personal information.

Schema Overview:
- The object must have the following properties:
  - 'id': An integer representing the person's ID.
  - 'name': A string representing the person's name.
  - 'home_phone', 'cell_phone', and 'work_phone': Strings representing phone numbers. At least one of these must be present.
  - 'birth_date': A string representing the person's birth date in date format.
  - 'govt_id_number': A string representing a government ID number.
  - 'day': A string representing the day of the week, limited to values "SU", "MO", "TU", "WE", "TH", "FR", "SA".

Validation Rules:
- 'id' and 'name' are required fields.
- At least one of 'home_phone', 'cell_phone', or 'work_phone' must be present.
- Either 'birth_date' or 'govt_id_number' must be present, but not both.
- If 'birth_date' or 'govt_id_number' is present, the other should not be present.

Usage:
This schema can be used to validate JSON data representing personal information, ensuring that it adheres to the specified structure and validation rules.
"""
import json
from jsonschema import validate, ValidationError

class JsonValidator:
    def validate_schema(self, json_file, schema_file):
        try:
            # Load JSON data
            with open(json_file, 'r') as f:
                json_data = json.load(f)

            # Load JSON schema
            with open(schema_file, 'r') as f:
                schema = json.load(f)

            # Validate against schema
            validate(instance=json_data, schema=schema)

            return True  # Validation succeeded
        except ValidationError as e:
            print(f"Validation failed: {e}")
            return False  # Validation failed

json_file_path = 'D:/Assignment/json_file.json'
schema_file_path = 'D:/Assignment/schema_file.json'
validator = JsonValidator()
result = validator.validate_schema(json_file_path, schema_file_path)
if result:
    print("Validation succeeded.")
else:
    print("Validation failed.")
