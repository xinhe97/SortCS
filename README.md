# SortCS
Sort the assets in the cross-section, and form portfolios.



1. Calculate equity characteristics and returns with [codes](https://github.com/Feng-CityUHK/EquityCharacteristics) and [wrds](https://wrds-www.wharton.upenn.edu)
2. Run the main.py



You get an object, in the class `cs` definded in folder `./tools/`. The object contains 61 groups of univariate (quintile) sorted portfolios and 60 groups of bivariate (ME2 x Char3) sorted portfolios, where portfolio returns, long-short factors, portfolio characteristics are very convenient to access via the class `cs`.