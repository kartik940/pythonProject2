from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ipl_data").getOrCreate()
def file_to_data_frame(path):
    return spark.read.csv(path, header=True, inferSchema=True)
df_1 = file_to_data_frame(r"pyspark/Book1.csv")
df_2 = file_to_data_frame(r"pyspark/sample.csv")
df_3 = file_to_data_frame(r"pyspark/sample.csv")
join_df = df_1.join(df_2, df_1.number == df_2.number, 'left')
join_df.show()

