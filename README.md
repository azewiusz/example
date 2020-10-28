# example
An example Python script for finding IPhone price tags on Allegro website

In order to run script from command line you need to have Python interpreter version 3.7.2 at least
Please ensure you have installed also selenium package for python using e.g.

```
pip install selenium
```

As described here: https://selenium-python.readthedocs.io/installation.html

And install chromedriver as instructed here: https://chromedriver.chromium.org/home

Also please edit main.py and set the path to chrome driver e.g.
```python
 # Here you need to set path to constructor if is not available related configuration ev variable - PATH
 driver = webdriver.Chrome('C:\gecko\chromedriver.exe')
```

How to run it from command line:

```
python main.py
```

Procedure:

Repeat below until succesfull loading of price list or retry_count exceeded
1. Go to web page www.allegro.pl
2. Type in search box 'Iphone 11'
3. Select black color 'czarny'
4. Display in console number of presented phones on the first page
5. Look for the most expensive price and display it to console
6. Add 23% to most expensive phone, [Here I decided to display it]

Application should give results similar to the following one:

```
Attempt 1 out of 10
Total products found on first page : 68
Most expensive price : 5849.00 zł
Most expensive price + 23% VAT : 7194.27 zł
```

Application uses mix of REGEXP + XPATH pattern matching to extract data.

In worst case it will keep retrying up to 10 times the procedure of price retrieval and will eventually
give no price results.
