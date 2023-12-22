# read file in pyspark and then create data frame and create another dataframe and join them
# create a function which will read any(csv) file and will return dataframe

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ipl_data").getOrCreate()
# df_spark = spark.read.csv(r"pyspark\ipl_data.csv", header=True, inferSchema=True)
# df_spark.show()

# defined a function
def file_to_data_frame(path):
    # read file
    df_spark = spark.read.csv(path,header=True, inferSchema=True)
    # return function
    return df_spark
data = file_to_data_frame(r"pyspark\ipl_data.csv")
data.show()
