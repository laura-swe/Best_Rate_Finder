# Best Exchange Currency Rate Finder  

This program will find exchange rates for a provided currency from foreign-exchange providers listed in the data references below. The base currency for all exchange rates is Canadian Dollar (CAD).

## Exchange Rates Data References
* [VBCE](https://www.vbce.ca/rates)
* [The Bank of Nova Scotia](http://www.scotiabank.com/ca/en/0,,1118,00.html)
* [Kingmark Currency Exchange](http://www.kingmark.ca/exchange-rates)
* [Happy Currency Exchange](http://www.happycurrency.com/rates)
* [Charlie's Currency Exchange](http://www.charliescurrency.ca/rates.html)
* [Gastown Collectables Inc. Currency Exchange](http://www.gciexchange.com/rates.php)

## Getting Started

Clone the repository in your local machine:

`$ git clone git@github.com:lauraguevara97/Best_Rate_Finder.git`

## Prerequisites

### Python 3

Install Python in Linux with:

`$ sudo apt-get install python3`

For other operating systems follow the instructions [here](https://python.org/downloads).

### Extra Libraries

The libraries used in this project are:

* Pandas
* Element Tree XML
* Requests
* OpenPyXL 

To install the required libraries, run the following command:

`pip3 install -r requirements.txt`

We will now assume that Python 3 and the required libraries are installed on your machine.

## Running The Program

Run the program:

`$ python currency.py <currency code>`

### Input

The currency.py program takes an input for the counter currency.
The `<currency code>` command line argument must be one of the following:
* USD
* AUD
* GBP
* CHF
* COP 
* EUR
* JPY
* NZD
* ZAR

### Output

The output will be an excel file named `output.xlsx` (located in the project directory) containing four sheets: 
1. Currency code Buys: Data for given currency code
2. Buys: Buying data for all currency codes
3. Sells: Selling data for all currency codes
4. Best Buys: Place that buys currency highest

## Example

To see a simple example use this command:

`$ python currency.py USD`

A new file named output.xlsx is created in project directory. Use Excel to view the data

## Version Control

GitHub was used to track all modifications and new implementations. For the full history, see the [commits on this repository](https://github.com/lauraguevara97/Best_Rate_Finder/commits/master).

## Authors

* Laura Guevara

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
