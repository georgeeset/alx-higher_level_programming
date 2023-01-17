#!/usr/bin/python3
""" This module contains the Base class"""

import json
import os
import csv

class Base:
    """Base class with private class attributes and constructors"""


    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file
        args:
            cls: Which ever class you need to save
            lst_objs; list of class instances you want to save
        """
        new_list = []
        if list_objs:
            for inst in list_objs:
                new_list.append(cls.to_dictionary(inst))
            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string
        args:
            json_string: is a string representing a list of dictionaries
        return:
            Empty list if Json_string is None or empty
            returns the list represented by json_string
        """
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribures already set"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """ Read a file and return list of instances"""
        file_name = f"{cls.__name__}.json"
        if not os.path.exists(file_name):
            return[]

        with open(file_name, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_inst = []

        for item in range(len(list_cls)):
            list_inst.append(cls.create(**list_cls[item]))

        return (list_inst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialize and deserialize in csv
        args:
            list_objs: list of objects to convert and save
        """
        filename = f"{cls.__name__}.csv"
        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if list_objs:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)


    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
