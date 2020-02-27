# restutil_api
Higher-level API for accessing restul services.

## Purpose
I have developed a scattering of utilities that retreive various pieces of
information from around the Internet such as average mortgage rates for a
given year, month, and term; Zillow value of a piece of real estate; information
about a Texas attorney, etc.

My *restutil* project is a server process that consolidates these utilities
into a single point of access via a restful API. This project provides a
higher-level Python 3 API for accessing those services. The services are
available via http GET calls but this API makes it simpler to access the
services and in some ways future-proofs the applications that consume these
services by providing a level of abstraction between using the services and
the underlying implementation of the services. E.G. it is very likely that the
HTTP interface will change in the future, but this API will remain the same.

## Implemented Utilities

### Historical Mortgage Interest Rates
*MortageRates* is a class for retrieving historical interest rates given a
year, month, and term of loan in years (5, 15, or 30).

**Example**
```python
from restutil.mortgage_rates import MortgageRates
mr = MortgageRates('my_api_key')
print(mr.average_mortgage_rate(year=2020, month=1, term=30))
>>> 0.0362
```

**Instantiation**
Instantiating MortgageRates requires an API_KEY and an optional address of
the utility server providing data to the API. API_KEY values can be obtained
from the package author by email request. Or, you can install the server
package on your site by cloning the (server project)[https://github.com/tjdaley/restutil].

**Methods**
*average_mortgage_rate* - Retrieves the average mortgage interest rate from
the Federal Reserve Bank of St. Louis for the given year, month, and term.

| arg | Description | Notes |
|-----|-------------|-------|
| year | Year being inquired about. | int. Range 1971-current. Required |
| month | Month being inquired about. | int. Range 1-12. Default=6 |
| term | Loan term in years. | int. Values=[5, 15, 30]. Default=30 |
