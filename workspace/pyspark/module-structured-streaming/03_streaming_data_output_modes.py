from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import  col
if __name__ == '__main__':
    spark = (SparkSession
             .builder
             .appName("Streaming App")
             .master("local")
             .config("spark.sql.shuffle.partitions",10).getOrCreate())

    CRIME_SCHEMA = StructType([
        StructField("code", StringType()),
        StructField("region", StringType()),
        StructField("category", StringType())
    ])
    #  Input Table
    input_table = spark.readStream.load(format="csv",
                                        path="../resources/dataset/crime_data/input",
                                        schema=CRIME_SCHEMA)

    # INcremental Query
    result_table = input_table.groupBy(col("region")).count()

    # Sink
    result_table.writeStream.start(format="console", outputMode="update").awaitTermination()