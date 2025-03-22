from django.db import models

# Create your models here. This is the file you will use to define database objects and schema
    #define Django database called StockData

#'symbol' field stores ticker string of the stock. eg. 'AAPL'
#'data' field stores hiostorical prices and moving average values for a giver ticker
 
class StockData(models.Model):
    symbol = models.TextField(null=True)
    data = models.TextField(null=True)