#!/usr/bin/env python
import argparse
from operator import itemgetter


def extract_symbols_text(map_file_text):
    start_pattern = "Common symbol       size              file"
    stop_pattern = "Discarded input sections"
    start_index = map_file_text.index(start_pattern) + len(start_pattern)
    stop_index = map_file_text.index(stop_pattern)
    map_file_text = map_file_text[start_index:stop_index]
    return map_file_text


def extract_symbols_dicts(symbols_text):
    symbols_dicts = []
    line = {}
    words = symbols_text.split()
    stop = len(words)
    step = 3
    start = step
    for i in range(start, stop, step):
        variable = words[i-3]
        size_str = words[i-2]
        size = int(size_str, 16)
        filename = words[i-1]
        line = {
            "variable": variable,
            "size": size,
            "filename": filename,
        }
        symbols_dicts.append(line)
    return symbols_dicts


def sort_symbols(symbols_dicts):
    sorted_symbols_dicts = sorted(symbols_dicts, key=itemgetter('size'))
    return sorted_symbols_dicts


def print_symbols(symbols_dicts):
    string_format = "%20s\t%20s\t%20s"
    print(string_format % ("variable", "size", "filename"))
    for symbols in symbols_dicts:
        variable = symbols['variable']
        size = symbols['size']
        filename = symbols['filename']
        print(string_format % (variable, size, filename))


def process(map_file):
    map_file_text = map_file.read()
    map_file.close()
    symbols_text = extract_symbols_text(map_file_text)
    symbols_dicts = extract_symbols_dicts(symbols_text)
    sorted_symbols_dicts = sort_symbols(symbols_dicts)
    print_symbols(sorted_symbols_dicts)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Order map file symbols from command line.")
    parser.add_argument('--map', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    map_file = args.map
    return map_file


def main():
    map_file = parse_args()
    process(map_file)

if __name__ == "__main__":
    main()
