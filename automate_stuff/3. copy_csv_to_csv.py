import csv

# open metioned file
with open('cars_model.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # open new file, where we want to copy data from csv_file
    with open('copy_cars_model.csv','w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter='\t')

        # iterate over first file (csv_file) and save data in csv_writer
        for line in csv_reader:
            csv_writer.writerow(line)


