'''
Testing telephone_routing
written by: Srivijay Manjunath

The operator number is chosen in random for testing.
'''

import unittest
import calc

from telephone_routing import csv_data_read, searching_algorithm, price_comparison, individual_operator_search

from random import randint


class Testing_telephone_routing(unittest.TestCase):

    def setUp(self):
        self.dialed_number = '4677878'
        self.file_path = 'prefixes_and_prices.csv'
        self.data_list = csv_data_read(self.file_path)
        self.total_operators = len(self.data_list) // 2
        self.operator_no = randint(1, self.total_operators)
        self.telephone_prefixes = self.data_list[(self.operator_no * 2) - 2]
        self.prices = self.data_list[(self.operator_no * 2) - 1]
        self.chosen_prefixes, self.chosen_prices = ([] for l in range(2))
        self.chosen_prefixes, self.chosen_prices = individual_operator_search(
            self.dialed_number, self.data_list)

    def test_csv_data(self):
        # Action
        result = csv_data_read(self.file_path)

        # Assert
        # TO check if the csv file is empty
        self.assertTrue(len(result) > 1)

    def test_searching_algorithm(self):
        # Action
        result = searching_algorithm(
            self.dialed_number,
            self.telephone_prefixes,
            self.prices)

        matched_parameters = list(result)
        length = len(str(matched_parameters[0]))

        # Assert
        # Checking the operator prefixes consists of corresponding prices
        self.assertTrue(len(self.telephone_prefixes) == len(self.prices))

    def test_price_comparison(self):

        # Action
        result = price_comparison(self.chosen_prefixes, self.chosen_prices)

        # Assert
        # To check if the minimum price is returned as cheapest
        self.assertTrue(min(result[0]) == result[1])


if __name__ == '__main__':
    unittest.main()
