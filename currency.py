from forex_python.converter import CurrencyRates,CurrencyCodes


class Currencies():
    """Class to check for valid code
    and convert from input"""

    
    def check_valid_from(self, from_input):
        """check the convert from input is a string country code and has the length of three. After wards makes sure it is in upper case"""

        if isinstance(from_input, str) and len(from_input) == 3:
            return (from_input).upper()


    def check_valid_to(self, to_input):
        """check the convert to input is a string country code and has the length of three. After wards makes sure it is in upper case"""

        if isinstance(to_input, str) and len(to_input) == 3:
            return (to_input).upper()

    def get_symbol(self, to_input):
        """ Gets a country's currency symbol"""
        cs = CurrencyCodes()
        symbol = cs.get_symbol(to_input)
        return symbol

    def converter(self, from_input, to_input, amount):
        """ Takes the input provided and converts the amount from one country currency(from_input) to another(to_input) """
        c = CurrencyRates()
        res = c.convert(from_input,to_input, amount)
        result = round(res,2)
        return result
    
    
    

