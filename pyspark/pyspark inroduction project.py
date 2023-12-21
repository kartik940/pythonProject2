# read file in pyspark and then create data frame and create another dataframe and join them

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ipl_data").getOrCreate()
df_spark = spark.read.csv("pyspark/ipl_data.csv", header=True, inferSchema=True)
df_spark.show()
