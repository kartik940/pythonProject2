# read file in pyspark and then create data frame and create another dataframe and join them
from pyspark.sql import SparkSession
# creating a variable
spark = SparkSession.builder.getOrCreate()
df_spark = spark.read.csv("IPL Matches 2008-2020.csv", inferSchema = True, header = True)
df_spark.show()
