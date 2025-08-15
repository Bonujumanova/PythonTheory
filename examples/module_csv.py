import csv

ENCODING = "UTF-8"

with open("data/users_data.csv", mode="r", encoding=ENCODING) as file:
    rows = csv.reader(file)

    header = next(rows)
    print(header)

    # for row in rows:
    #     print(row)
    #     break

    with open("data/pipe.csv", mode="w", encoding=ENCODING) as f:
        wr = csv.writer(f, dialect="excel", delimiter="|")
        wr.writerow(['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address'])
        for row in rows:
            # print(type(row))  # list
            wr.writerow(row)

with open("data/users_data.csv", mode="r", encoding=ENCODING) as file:
    rows = csv.DictReader(file)
    print(rows)

    # for row in rows:
    #     print(row)

    with open("data/ampersand_dict_writer.csv", mode="w", encoding=ENCODING) as f:
        # wr = csv.DictWriter(
        #     f,
        #     ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'addit'],
            # delimiter="&",
            # restval="N/A"
        # )

        wr = csv.DictWriter(
            fieldnames=['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'addit'],
            f=f,
            delimiter="&",
            restval='N/A'
        )
        wr.writeheader()
        for row in rows:
            wr.writerow(row)

# users_data = {
#     '1': {
#         'first_name': 'Brenna',
#         'last_name': 'Sconce',
#         'email': 'bsconce0@stumbleupon.com',
#         'gender': 'Female',
#         'ip_address': '124.108.4.132'
#     }
# }
