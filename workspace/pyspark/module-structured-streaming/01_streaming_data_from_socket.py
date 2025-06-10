from pyspark.sql import SparkSession
if __name__ == '__main__':
    spark = (SparkSession
             .builder
             .appName("Streaming App")
             .master("local")
             .config("spark.sql.shuffle.partitions",10).getOrCreate())

    #  Input Table
    input_table = spark.readStream.load(format="socket", host="localhost", port="9900")

    # INcremental Query


    # Sink
    input_table.writeStream.start(format="console", outputMode="append").awaitTermination()