# restutil_api
Higher-level API for accessing restul services.

<p align="center">
    <a href="https://github.com/tjdaley/restutil_api/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/tjdaley/restutil_api"></a>
    <a href="https://github.com/tjdaley/restutil_api/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/tjdaley/restutil_api"></a>
    <a href="https://github.com/tjdaley/restutil_api/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/tjdaley/restutil_api"><a>
    <a href="https://github.com/tjdaley/restutil_api/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/tjdaley/restutil_api"></a>
    <img alt="Stage: Development" src="https://img.shields.io/badge/stage-Development-orange">
</p>
<p align="center">
    <a href="#purpose">Purpose</a> &bull;
    <a href="#installation">Installation</a> &bull;
    <a href="#utilities">Utilities</a> &bull;
    <a href="#author">Author</a>
</p>

<a href="#purpose"></a>
# Installation

```
pip install https://github.com/tjdaley/restutil
```

<a href="#purpose"></a>

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

<a href="#installation"></a>

## Installation
```
pip install restutil-tjdaley
```

<a href="#utilities"></a>

## Implemented Utilities

### Attorney Search
*AttorneySearch* is a class for retrieving information about attorneys from
public data sources given a bar number and state. For now, 'TX' is the only
state that is implemented.

**Example**
```python
searcher = AttorneySearch()
atty = searcher.find('24059643')
print(json.dumps(atty, indent=4))
>>>
{
    "name": "Thomas James Daley",
    "bar_number": "24059643",
    "license_date": "11/02/2007",
    "primary_practice": "Plano , Texas",
    "address": "825 Watters Creek Blvd Ste 395. Allen, TX 75013."
}
```

This class scrapes the State Bar of Texas web site, which is not constructed for
easy scraping of data. Therefore, sometimes some junk appears at the end of the
address field.

**Methods**
*find* - Retrieve name, license date, primary practice location, and address for
a given attorney.

| arg | Description | Notes |
|-----|-------------|-------|
| bar_number | State Bar number | str. Required |
| state | Two-letter abbreviation for state we are searching in. | str. Values={'TX'}. Default='TX'. |

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
package on your site by cloning the [server project](https://github.com/tjdaley/restutil).

**Methods**
*average_mortgage_rate* - Retrieves the average mortgage interest rate from
the Federal Reserve Bank of St. Louis for the given year, month, and term.

| arg | Description | Notes |
|-----|-------------|-------|
| year | Year being inquired about. | int. Range 1971-current. Required |
| month | Month being inquired about. | int. Range 1-12. Default=6 |
| term | Loan term in years. | int. Values={5, 15, 30}. Default=30 |

<a href="#author"></a>

## Author
Thomas J. Daley, J.D. is an active family law litigation attorney practicing primarily in Collin County, Texas, an occassional mediator, and 
software developer.