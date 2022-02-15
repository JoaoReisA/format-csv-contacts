import csv
import random
def csvToMap():
    contacts = {'Nome': [], 'Telefone' : [],}
    newPhones = []
    
    with open('contacts.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file,delimiter=';',fieldnames=["NOME", "TELEFONE"])
        reader.__next__()
        for row in reader:
            contacts['Nome'].append(str(row["NOME"]))
            contacts['Telefone'].append(str(row["TELEFONE"]))
        for item in contacts['Telefone']:
            if len(item) == 13:      
                subString = item[2:-1]
            else:
                subString = item
            newPhones.append(subString)
        contacts['Telefone'].clear()
        contacts['Telefone'].extend(newPhones)
    return contacts

def generateNewCsv(map):
    with open(f'new_contacts{random.randint(0,1000)}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nome', 'Telefone']
        writer = csv.DictWriter(csvfile, delimiter=';',fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(map["Nome"])):
            writer.writerow({"Nome" : map["Nome"][i], "Telefone" : map["Telefone"][i]})
            

            
        

def main():
    map =  csvToMap()
    generateNewCsv(map)
    
if __name__ == '__main__':
    main()