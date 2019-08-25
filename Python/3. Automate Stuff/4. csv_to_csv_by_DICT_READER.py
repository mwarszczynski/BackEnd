import csv

with open('cars_model.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_cars_model.csv','w') as new_csv_file:
        fieldnames = ['car','model']

        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()


# To be continued