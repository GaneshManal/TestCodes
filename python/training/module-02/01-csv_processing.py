"""
document
"""
import json


def read_data_from_file():
    """
    read the data from csv file
    input: None
    output: list of parameters from csv file
    """
    filename = "cpu_memory_input.csv"
    timestamp, cpu_util, ram_util = [], [], []
    with open(filename, "r", encoding="utf-8") as file_handler:
        all_lines = file_handler.readlines()
    for line in all_lines[1:]:
        values = line.split(',')
        timestamp.append(values[0])
        cpu_util.append(float(values[1].strip(" %\n")))
        ram_util.append(float(values[2].strip(" %\n")))
    return timestamp, cpu_util, ram_util


def read_info_from_data(input_cpu, input_ram):
    """
    Extract information from data required by user
    input: data like timestamp, cpu, ram as a list
    return: user data as dict
    """
    data = {"cpu": {}, "ram": {}}
    cpu_dict = data["cpu"]
    ram_dict = data["ram"]

    # calculate cpu/ram min
    cpu_dict.update({"min": min(input_cpu)})
    ram_dict.update({"min": min(input_ram)})

    # calculate cpu/ram max
    cpu_dict.update({"max": max(input_cpu)})
    ram_dict.update({"max": max(input_ram)})

    # calculate cpu/ram mean
    cpu_avg = sum(input_cpu) / len(input_cpu)
    ram_avg = sum(input_ram) / len(input_ram)
    cpu_dict.update({"mean": cpu_avg})
    ram_dict.update({"mean": ram_avg})

    return data


if __name__ == "__main__":
    ts, cpu, ram = read_data_from_file()
    # time_cpu_data = zip(timestamp, cpu, ram)
    user_data = read_info_from_data(cpu, ram)
    print(user_data)
    print(json.dumps(user_data))
