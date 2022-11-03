import csv, hashlib, json

'''Output CSV File'''
output_file = 'files/output.csv'

with open(output_file, 'w') as write_file:
    write_to_file = csv.writer(write_file)
    write_to_file.writerow(['S/N', 'Filename', 'Description', 'Gender', 'Attributes', 'UUID', 'Output File Name'])

    with open('files/nft.csv', 'r') as csv_file:
        read = csv.reader(csv_file, delimiter=',')
        next(read)
        data = [i for i in read]  
        for row in data:
            if row[1] and row[2]:
                sn, file_name, name, description, gender, attributes, uuid = row[0], row[1], row[2], row[3], row[4], row[5], row[-1]
                
                nft = {
                    'format' : 'CHIP-0007',
                    'id' : uuid,
                    'name' : name,
                    'filename': file_name,
                    'description' : description,
                    'gender': gender,
                    'attributes': '[]',
                    'minting_tool' : 'OEDJOAT ######',
                    'sensitive_content' : False,
                    'series_number' : sn,
                    'series_total' : data[-1][0],
                    'collection' : {
                        'name' : 'HNG task',
                        'id' : 'e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57'
                    }
                }
                jsonObj = json.dumps(nft, indent=4)
                with open(f'files/json_dump/{file_name}.json', 'w') as output:
                    output.write(jsonObj)
                output.close()
                hashString = hashlib.sha256(jsonObj.encode()).hexdigest()
                row.append(f'{file_name}.{hashString}.csv')
                write_to_file.writerow(row)
        