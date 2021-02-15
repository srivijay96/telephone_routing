'''
Routing of telephone calls;
writen by: Srivijay Manjunath

'''

import numpy as np
import csv

file_path = 'prefixes_and_prices.csv'


def csv_data_read(file_path):
    """To read and store data from the csv,
    remove empty strings
    """

    operator_data, prefix_price_lists = ([] for l in range(2))

    with open(file_path, 'r') as _file:
        _reader = csv.reader(_file)

        for row in _reader:
            operator_data.append(row)

        # Removing empty elements from the list
        for index in range(len(operator_data)):
            prefix_price_lists.append(
                [element for element in operator_data[index]
                    if element])

    return prefix_price_lists


def searching_algorithm(dialed_number, telephone_prefixes, prices):
    """To find all the prefix matches and return the longest
    prefix from the matches and the corresponding price.

    Assumption : length of longest prefix in the csv is 7.
    """

    comparing_len = 7
    matched_prefixes = []

    for i in range(1, comparing_len + 1):
        for j in range(len(telephone_prefixes)):
            if telephone_prefixes[j] == dialed_number[:i]:
                matched_prefixes.append(telephone_prefixes[j])

    # if any match is found
    if len(matched_prefixes) > 0:
        index = telephone_prefixes.index(max(matched_prefixes, key=len))
        longest_prefix = telephone_prefixes[index]
        corresponding_price = prices[index]
        # print("You can use the extension {} and the price per minute is {}"
        # .format(longest_prefix,corresponding_price))
    else:
        longest_prefix = -1
        corresponding_price = -1
        #print("This number cannot be dailed using this operator")

    return longest_prefix, corresponding_price


def price_comparison(prefixes, prices):
    """To find the cheapest price b/w all the operators.
    Eliminating the buffer values(-1) from the list and
    finding the cheapest_price price and the corresponding prefix
    given by the operator.
    """

    filtered_prices, cheapest_price_list = ([] for l in range(2))

    # converting to float for price comparison
    prices = list(map(float, prices))

    # filtering the unmatched operator prices
    for index in range(len(prices)):
        if prices[index] != -1:
            filtered_prices.append(prices[index])

    if len(filtered_prices) > 0:
        cheapest_price = min(filtered_prices)
        # To check for multiple operators offereing the cheapest price
        print("Operators offering the cheapest price is as follows:")
        for index in range(len(prices)):
            if cheapest_price == prices[index]:
                cheapest_price_list.append(prices[index])
                indexx = index

                if len(cheapest_price_list) > 1:
                    print('---------------------------')
                    print("Operator No : {}".format(index + 1))
                    print("The extension you can use from this operator is {}"
                          .format(prefixes[indexx]))
                    print("For the price {} $ per minute".format(cheapest_price))
        # To diaplay the operator providing the cheapest price
        if len(cheapest_price_list) == 1:
            print("Operator No : {}".format(indexx + 1))
            print("The extension you can use from this operator is {}"
                  .format(prefixes[indexx]))
            print("For the price {} $ per minute".format(cheapest_price))
    else:
        cheapest_price = -1
        print("No prefixes found by any operator, Sorry!!")

    return filtered_prices, cheapest_price


def individual_operator_search(dialed_number, data_lists):
    """To check individual operators for the prefix matches,
    and return 2 lists containing the prefix matches and thier
    corresponding prices.
    """
    total_operators = len(data_lists) // 2
    matched_prefixes, matched_prices = ([] for l in range(2))

    for operator_no in range(1, total_operators + 1):
       # print("Checking for Operator-{}".format(operator_no))
        telephone_prefixes = data_lists[(operator_no * 2) - 2]
        prices = data_lists[(operator_no * 2) - 1]
        matched_parameters = searching_algorithm(dialed_number,
                                                 telephone_prefixes, prices)
        matched_parameters = list(matched_parameters)
        matched_prefixes.append(matched_parameters[0])
        matched_prices.append(matched_parameters[1])

    return matched_prefixes, matched_prices


def main():
    while(True):
        dialed_number = input("Please dial the number: ")

        if dialed_number.isnumeric():
            data_lists = csv_data_read(file_path)
            matched_prefixes, matched_prices = ([] for l in range(2))
            matched_prefixes, matched_prices = individual_operator_search(
                dialed_number, data_lists)
            price_comparison(matched_prefixes, matched_prices)

        else:
            print('Please enter an input containing only digits')


if __name__ == '__main__':
    main()
