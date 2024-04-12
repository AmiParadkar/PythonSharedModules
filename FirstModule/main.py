import json

import SharedUtils.helper

# Get yesterday's date
yesterday_date = SharedUtils.helper.get_yesterday_date()

print(f"Yesterday's date: {yesterday_date}")


test_file = open('./FirstModule/test.json')
field_operation = json.load(test_file)
print(f"Field operation: {field_operation}")