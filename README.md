# Stock analysis app

This app is made using pythons django web framework to make an app that collects, cleans, and displays data about some stocks.  
This will include changes, prices, and more to come.

### Data collection/processing

The data is collected from the yahoo finance api via the pip library, yfinance. It is then stored and processed using pandas.

### Data Visualization

After processing the data, matplotlib and django are used to visualize the data. Matplotlib will provide the charts/graphs and then using django a web app will be made to help display it.
