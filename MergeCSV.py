import csv

with open('apple.csv', 'rb') as file_a, open('orange.csv', 'rb') as file_b:
    data_a = csv.reader(file_a)
    data_b = dict(csv.reader(file_b))  # <-- dict
    with open('out.csv', 'wb') as file_out:
        csv_out = csv.writer(file_out)
        for word, num_a in data_a:
            if word in data_b:
                csv_out.writerow(str(word) + str(num_a) + str(data_b[word]))