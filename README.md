# RangeItemParser
This simple script takes a flat list of networks in CIDR notation and parses the list to a importable Excel file. So you can import a flat list of networks to a ServiceNow instance and use it there as a "Discovery Range Item".

# Usage
* Install dependencies via "pip install -r requirements.txt"
* Put a "networks.csv" next to the "parse.py" (see formating in the "networks.csv.example")
* Run the script via "python parse.py"
* Import the generated "Networks.xlsx" to your ServiceNow instance
