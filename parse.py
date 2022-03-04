import ipaddress
import xlsxwriter

# Setup Excel File
workbook = xlsxwriter.Workbook("Networks.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Name')
worksheet.write('B1', 'Active')
worksheet.write('C1', 'Attributes')
worksheet.write('D1', 'Ending IP')
worksheet.write('E1', 'Network mask (or bits)')
worksheet.write('F1', 'Network IP')
worksheet.write('G1', 'Discovery range')
worksheet.write('H1', 'Schedule')
worksheet.write('I1', 'Starting IP')
worksheet.write('J1', 'Summary')
worksheet.write('K1', 'Created')
worksheet.write('L1', 'Type')

# Do the logic
file = open('networks.csv', 'r')
networks_list = file.read().splitlines()

# Generate the Data
network_objects = []
for network in networks_list:
    net = ipaddress.IPv4Network(network)
    network_obj = []
    # Set name
    network_obj.append(network)

    # Set Active
    network_obj.append(True)

    # Set Attributes
    network_obj.append('')

    # Set Ending IP
    network_obj.append('')

    # Set Network mask
    network_obj.append(int(network[-2:]))

    # Set Network IP
    network_obj.append(str(net.network_address))

    # Set Discovery Range
    network_obj.append('')

    # Set Schedule
    network_obj.append('')

    # Set Starting IP
    network_obj.append('')

    # Set Summary
    network_obj.append(network)

    # Set Created
    network_obj.append('')

    # Set Type
    network_obj.append('IP Network')

    network_objects.append(network_obj)

# Save data in Excel-File

# Exclude Header
row = 1
for obj in network_objects:
    col = 0
    for attribute in obj:
        worksheet.write(row, col, attribute)
        col += 1
    row += 1



workbook.close()




