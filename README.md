# Best Exchange Currency Rate Finder  

This program is a simple Python script that parses different websites to finds the best exchange rate in the Lower Mainland area for a provided currency code 

## Exchange Rates Data References
* [VBCE](https://www.vbce.ca/rates)
* [The Bank of Nova Scotia](http://www.scotiabank.com/ca/en/0,,1118,00.html)
* [Kingmark Currency Exchange](http://www.kingmark.ca/exchange-rates)
* [Happy Currency Exchange](http://www.happycurrency.com/rates)
* [Charlie's Currency Exchange](http://www.charliescurrency.ca/rates.html)

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

To install all the libraries run the setup script:

`$ ./install_requirements.sh`

If you are not using a Linux environment, use the commands from [here](install_requirements.sh).

After this step we can assume that all the libraries required by the program will be installed in your local machine.

## Running The Program
run the currency.py program

`$ python currency.py <currency code>`

### Input

The predict_weather.py program takes in a `currency code` as a command line argument.
Currency code can be any of the following:
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
