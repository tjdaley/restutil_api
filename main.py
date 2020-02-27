from restutil.mortgage_rates import MortgageRates
mr = MortgageRates('tjdaley', '192.168.1.81')
print(mr.average_mortgage_rate(2020, 1, 30))
