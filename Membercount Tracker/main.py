import time
import gspread
import requests
import datetime

gc = gspread.oauth()

while True:
    def get_empty_row(sheet):
        num_rows = len(sheet.get_all_values())
        return num_rows + 1

    def update_row_values(sheet, empty_row, col1_value, col2_value, col3_value, col4_value, col5_value):
        sheet.update_cell(empty_row, 1, col1_value)
        sheet.update_cell(empty_row, 2, col2_value)
        sheet.update_cell(empty_row, 3, col3_value)
        sheet.update_cell(empty_row, 4, col4_value)
        sheet.update_cell(empty_row, 5, col5_value)
        sheet.update_cell(empty_row, 6, f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    def update_google_sheet(sheet_name, col1_value, col2_value, col3_value, col4_value, col5_value):
        sheet = gc.open(sheet_name).sheet1

        empty_row = get_empty_row(sheet)

        update_row_values(sheet, empty_row, col1_value, col2_value, col3_value, col4_value, col5_value)
        print(f"Group Member Count Updated @{datetime.datetime.now()}")

    def get_member_count(group_id: int):
        response = requests.get(f'https://groups.roblox.com/v1/groups/{group_id}')
        data = response.json()['memberCount']
        return str(data)

    print(f"Updating Group Member Count! @{datetime.datetime.now()}")
    sheet_name = 'FORSCOM | Group Tracker' # <= Name of your Spreasheet

    col1_value = get_member_count(3198375) # <= Group ID of FORSCOM
    col2_value = get_member_count(3725812) # <= Group ID of 1ID
    col3_value = get_member_count(3735974) # <= Group ID of 101ST
    col4_value = get_member_count(6245987) # <= Group ID of 1AD
    col5_value = get_member_count(3198387) # <= Group ID of 82ND

    update_google_sheet(sheet_name, col1_value, col2_value, col3_value, col4_value, col5_value)
    time.sleep(3600) # <= Time interval between each update in seconds.