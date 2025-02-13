#!/usr/bin/env python3
# Author ID: 162458210

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        return f"File '{file_name}' not found"

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            cleaned_lines = [line.strip() for line in lines]
        return cleaned_lines
    except FileNotFoundError:
        return f"File '{file_name}' not found"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))