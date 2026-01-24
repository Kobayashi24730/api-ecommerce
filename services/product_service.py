from utils.file_db import read_data, write_data

def get_all_products():
    return read_data()

def add_product(product):
    data = read_data()
    product["id"] = max([p["id"] for p in data], default=0) + 1
    data.append(product)
    write_data(data)
    return product

def delete_product(pid):
    data = read_data()
    data = [p for p in data if p["id"] != pid]
    write_data(data)
