import pandas as pd

# Define the header and data as strings
header = """Account Number|Account Type|HIN|ExternalAccount Reference|Legal Entity ID|Legal Entity Name|Legal Entity Status|Legal Entity Type|Trust Type|Other Trust Type|Account Status|Account Name|Linked Options Account Number|CFD Account Number|Option Level|Sell Only|Warrants Flag|CFD Service|Home Phone|Work Phone|Mobile Phone|Fax|Email Address|Postal Address Recipient|Postal Address Line 1|Postal Address Line 2|Postal Address Line 3|Postal Address Suburb|Postal Address State|Postal Address Post Code|Postal Address Country|CHESS Addr 1|CHESS Addr 2|CHESS Addr 3|CHESS Addr 4|CHESS Addr 5|CHESS Addr 6|CHESS Addr PostCode|Date/Time Account Created|First Settlement BSB|First Settlement Account Number|First Settlement Account Name|First Settlement CR/DR Identifier|Second Settlement BSB|Second Settlement Account Number|Second Settlement Account Name|Second Settlement CR/DR Identifier|Third Settlement BSB|Third Settlement Account Number|Third Settlement Account Name|Third Settlement CR/DR Identifier|BRAY Reference|ML Settlement PID|ML Account Reference|Trading Group Name|Brokerage Charge Code|Account Closed Date|Settlement Type|Adviser Code|Contract Note Indicator"""

data = """50000071|AXEQCUSDVP|||1606781|MR PITCH PITCH|Active|Individual|||Active|MR PITCH PITCH||||False|False|False|||0000000000||soumyagh@nrifintech.com||123 FAKE STREET|||SYDNEY|NSW|2000|AUS|MR PITCH PITCH,|123 FAKE STREET|SYDNEY NSW||||2000|2024/01/23 12:44:22|||||||||||||500000716|21028|MR PITCH PITCH|AXEQCUSDVP - Default|BXA|||DUMD6|Electronic Contract Note
50000072|AXEQMAC|||1606782|MR PITCH2 PITCH2|Active|Individual|||Active|MR PITCH2 PITCH2||||False|False|False|||0000000000||soumyagh@nrifintech.com||123 FAKE STREET|||SYDNEY|NSW|2000|AUS|MR PITCH2 PITCH2,|123 FAKE STREET|SYDNEY NSW||||2000|2024/01/23 12:59:27|182512|123456789|MR PITCH2 PITCH2|B|||||||||500000724|||AXEQMAC - Default|BXA|||DUMD6|Electronic Contract Note"""

# Split the header and data into lists
columns = header.split("|")
rows = [row.split("|") for row in data.split("\n")]

# Create a DataFrame
df = pd.DataFrame(rows, columns=columns)

# Display the DataFrame

import unittest
import pandas as pd

# Giả sử đây là dữ liệu trả về từ API
api_response = [
    {"API_name": "John Doe", "API_age": 30, "API_country": "USA"},
    {"API_name": "Jane Smith", "API_age": 25, "API_country": "UK"},
    {"API_name": "Nguyen Van A", "API_age": 28, "API_country": "Vietnam"},
]


# Hàm để đọc file Excel và trả về danh sách các từ điển
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


# Hàm để kiểm tra mapping
def check_mapping(excel_data, api_data):
    for excel_row, api_row in zip(excel_data, api_data):
        if (
            excel_row["name"] != api_row["API_name"]
            or excel_row["age"] != api_row["API_age"]
            or excel_row["country"] != api_row["API_country"]
        ):
            return False
    return True


class TestMapping(unittest.TestCase):
    def test_mapping(self):
        # Đường dẫn tới file Excel
        file_path = "path_to_your_excel_file.xlsx"

        # Đọc dữ liệu từ file Excel
        excel_data = read_excel(file_path)

        # Kiểm tra mapping
        self.assertTrue(check_mapping(excel_data, api_response))


if __name__ == "__main__":
    unittest.main()
