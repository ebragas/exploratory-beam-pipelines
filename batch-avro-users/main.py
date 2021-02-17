import apache_beam as beam


with beam.Pipeline() as p:

    results = (
        p
        | beam.io.ReadFromText("./data/reddit_wsb.csv")
        | beam.io.WriteToText("./output/out", file_name_suffix=".csv")
    )
