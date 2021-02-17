import os
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions


PROJECT_ID = "beam-udemy"
TOPIC_ID = "beam-example-input"
SUBSCRIPTION_ID = "beam-example-input-sub1"

pipeline_options = PipelineOptions(streaming=True)

p = beam.Pipeline(options=pipeline_options)

result = (
    p
    | beam.io.ReadFromPubSub(subscription=f"projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}")
    | beam.io.WriteToText("./data/pubsub/output")
)

result = p.run()
result.wait_until_finish()
