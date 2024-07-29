from pyspark.sql import SparkSession


class SparkTask:
    def __init__(self, spark_session):
        self.job_count_dict = None
        self.sc = spark_session.sparkContext
        self.spark = spark_session

    def group_sort(self, input_path):
        # Read data from the CSV file and create an RDD
        lines = self.sc.textFile(input_path)

        # Split each line into a tuple (job, 1) and reduce by key to get job counts
        job_counts = lines.map(
            lambda line: (line.split(",")[1], 1)
        ).reduceByKey(lambda x, y: x + y)

        # Sort by count and then by job name (ascending order)
        sorted_job_counts = job_counts.sortBy(lambda x: (x[1], x[0]))

        # Collect the result as a dictionary
        self.job_count_dict = dict(sorted_job_counts.collect())

        return self.job_count_dict


# Example usage:
spark = SparkSession.builder.appName("JobGroupSort").getOrCreate()
spark_task = SparkTask(spark)
input_path = "jobs.csv"
result = spark_task.group_sort(input_path)
print(result)
