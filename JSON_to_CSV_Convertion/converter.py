import json #Importing the JSON Module

if __name__ == '__main__': #Main Program Execution
    try: #Try-Except Block
        with open('input.json', 'r') as f: #Reading JSON Data
            data = json.loads(f.read())

        output = ','.join([*data[0]]) #Preparing Output Data
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f: #Writing to a CSV File
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
