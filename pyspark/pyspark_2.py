from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Join_data").getOrCreate()

def joining_df(path):
    read_csv = spark.read.csv(path, header= True, inferSchema =True)
    return read_csv
dataframe_1 = joining_df(r"pyspark/Book1.csv")
dataframe_2 = joining_df("pyspark/sample.csv")
join_dataframe = dataframe_1.join(dataframe_2, dataframe_1.number == dataframe_2.number, 'inner')
join_dataframe.show()
