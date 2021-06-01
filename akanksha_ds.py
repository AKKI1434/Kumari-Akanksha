# !/usr/bin/python
# -*- coding: utf-8 -*

__author__ = "Bharat Sharma"

"""
Doc_Type            : Akanksha_DS Utility
Tech Description    : To detect whether a person is slouching or not
Pre_requisites      : N/A
Inputs              : Plain text file which has the numbers in the forms
Outputs             : Printing if the Person is slouching or not
Config_file         : N/A
Last modified by    : Akanksha Singh
Last modified on    : 30th March 2021
"""

import logging
import pandas as pd
import re
import math

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
MODULE_NAME = "Akanksha Ds Algorithm"
logger = logging.getLogger(MODULE_NAME)

# The usage sting to be displayed to the user for the utility
USAGE_STRING = """
SYNOPSIS
    python3 akashksha_ds.py
"""


class akanksha_ds:
    """
    Description: It will print whether the person is slouching or not
    """
    def __init__(self):
        """
        Purpose: Call all the relevant functions
        :return: Output encrypted text
        """
        var = "str"

    def read_file(self):
        """
        Purpose: Read file and return the list
        :return: Output list
        """
        try:
            coordinate_data = list()
            with open("D:\Chegg_Code\Mudra Dataset.txt") as f:
                for line in f:
                    coordinate_data.append(line[3:17])
            return coordinate_data
        except Exception as ex:
            o_error = "Failed to process the plain text. ERROR: %s" % str(ex)
            logger.error(o_error)

    def convert_data(self, data):
        """
        Purpose: Read file and return the list of hexadecimal to coordinates
        :return: Output coordinates
        """
        try:
            list_new_coordinate_list = list()
            for rows in data:
                row_list = re.split(",", rows)
                new_coordinate_list = list()
                for each_row in row_list:
                    data_row = int(each_row, 16)
                    if data_row >32767:
                        data_row = data_row-65535
                    data_row = data_row/10000
                    # print(data_row)
                    new_coordinate_list.append(data_row)
                list_new_coordinate_list.append(new_coordinate_list)
            return  list_new_coordinate_list
        except Exception as ex:
            o_error = "Failed to process the plain text. ERROR: %s" % str(ex)
            logger.error(o_error)

    def calulcate_angle(self, data_list_of_list):
        """
        Purpose: Calculate the angle between two points
        :return: Output angle list
        """
        a1 = 1
        b1 = 0
        c1 = 0
        count = 0
        count2 = 0
        for data in data_list_of_list:
            a2 = data[0]
            b2 = data[1]
            c2 = data[2]
            d = (a1 * a2 + b1 * b2 + c1 * c2)
            e1 = math.sqrt(a1 * a1 + b1 * b1 + c1 * c1)
            e2 = math.sqrt(a2 * a2 + b2 * b2 + c2 * c2)
            d = d / (e1 * e2)
            # print(d)
            A = math.acos(d)
            # print("Angle is degree")
            # print(math.degrees(A))
            if math.degrees(A) < 15:
                # print("Not Slouching")
                count = count + 1
            else:
                count2 = count2 + 1
                # print("Slouching")

        print(count)
        print(count2)

    def main(self):
        """
        Purpose: Call all the relevant functions
        :return: Output Status
        """
        try:
            data = self.read_file()
            print(data)
            converted_data = self.convert_data(data)
            print(converted_data)
            self.calulcate_angle(converted_data)
            return "Code Ended Successfully"
        except Exception as ex:
            o_error = "Failed to process the plain text. ERROR: %s" % str(ex)
            logger.error(o_error)


if __name__ == "__main__":
    """
    Description: The Akanksha Ds module is used to calulate whether the person is slouching. It takes
                 Plain numbers from a file as a input.
    """
    try:
        akanksha_ds_obj = akanksha_ds()
        output = akanksha_ds_obj.main()
        logger.info(output)
    except Exception as exc:
        out_error = "Failed to process the plain text. ERROR: %s" % str(exc)
        logger.error(out_error)
