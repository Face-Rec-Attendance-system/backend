from datetime import date
import requests


def create_new_column(sheet_id, sheet_name, column_title):
    today = date.today().strftime('%Y-%m-%d')

    endpoint_url = f"https://api.sheety.co/{sheet_id}/{sheet_name}/1"

    headers = {
        # "Authorization": "Bearer YOUR_SHEETY_API_KEY",
		"Content-type": "application/json",
    }

    new_column_data = {
        sheet_name: {
            "columnNames": [column_title],
        }
    }

    response = requests.patch(endpoint_url, json=new_column_data, headers=headers)

    if response.status_code == 200:
        print("New column created successfully with the title:", column_title)
    else:
        print("Failed to create the new column. Response status code:", response.status_code)
