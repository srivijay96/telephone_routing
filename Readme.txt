
The directory consists of two python
(telephone_routing.py, test_telephone_routing.py),
a csv file(prefixes_and_prices.csv),
a pdf file(Question.pdf) and a txt file(Readme.txt)



Structure of data stored in 'prefixes_and_prices.csv':
operator_1_prefixes:
operator_1_prices:
operator_2_prefixes:
operator_2_prices:
.
.
operator_n_prefixes:
operator_n_prices:


Execution:
1. unzip the folder
2. open telephone_routing.py
3. To check know the findings of individual operators,
    please uncomment the print statements in the functions
    searching_algorithm and individual_operator_search
4. run telephone_routing.py
5. Unittest cases are written in test_telephone_routing
6. to run this file, please use the following command:
    python3 -m unittest test_telephone_routing.py


Assumption:
The maximum length of the telephone extension in
the csv file is is 7.
