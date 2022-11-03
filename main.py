import csv, hashlib, json

'''Output CSV File'''
output_file = 'files/output.csv'

with open(output_file, 'w') as write_file:
    write_to_file = csv.writer(write_file)
    write_to_file.writerow(['TEAM NAMES','S/N', 'Filename', 'Description', 'Gender', 'Attributes', 'UUID', 'Output File Name'])

    with open('files/nft.csv', 'r') as csv_file:
        read = csv.reader(csv_file, delimiter=',')
        next(read)
        data = [i for i in read]  
        for row in data:
            if row[1] and row[2]:
                teamname, sn, file_name, name, description, gender, trait_types, uuid = row[0], row[1], row[2], row[3], row[4], row[5], row[6].split(';'), row[-1]
                hair_trait = trait_types[0].split(': ')
                eye_trait = trait_types[1].split(': ')
                teeth_trait = trait_types[2].split(': ')
                clothing_trait = trait_types[3].split(':')
                accesories_trait = trait_types[4].split(':')
                expression_trait = trait_types[5].split(':')
                strength_trait = trait_types[6].split(':')
                weakness_trait = trait_types[-1].split(':')
               
                nft = {
                    'format' : 'CHIP-0007',
                    'id' : uuid,
                    'name' : name,
                    'filename': file_name,
                    'description' : description,
                    'gender': gender,
                    'attributes': [
                        {
                            'trait_type': hair_trait[0],
                            'value': hair_trait[1]
                        },

                        {
                            'trait_type': eye_trait[0],
                            'value': eye_trait[1]
                        },
                        
                        {
                            'trait_type': teeth_trait[0],
                            'value': teeth_trait[1]
                        },
                        {
                            'trait_type': clothing_trait[0],
                            'value': clothing_trait[1]
                        },
                        {
                            'trait_type': accesories_trait[0],
                            'value': accesories_trait[1]
                        },
                        {
                            'trait_type': expression_trait[0],
                            'value': expression_trait[1]
                        },
                        {
                            'trait_type': strength_trait[0],
                            'value': strength_trait[1]
                        },
                        {
                            'trait_type': weakness_trait[0],
                            'value': weakness_trait[1]
                        },
                    ],
                    
                    'minting_tool' : teamname,
                    'sensitive_content' : False,
                    'series_number' : sn,
                    'series_total' : data[-1][1],
                    'collection' : {
                        'name' : 'Zuri NFT tickets for free lunch',
                        'id' : 'e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57'
                    },
                    'attribute': [
                        {
                            'type': 'description',
                            'value': 'Rewards for accomplishments during HNGi9'
                        }
                    ]
                }
                jsonObj = json.dumps(nft, indent=4)
                with open(f'files/json_dump/{file_name}.json', 'w') as output:
                    output.write(jsonObj)
                output.close()
                hashString = hashlib.sha256(jsonObj.encode()).hexdigest()
                row.append(f'{file_name}.{hashString}.csv')
                write_to_file.writerow(row)
        