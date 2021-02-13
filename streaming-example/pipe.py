import os
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions


PROJECT_ID = "beam-udemy"
TOPIC_ID = "beam-example-input"
SUBSCRIPTION_ID = "beam-example-input-sub1"

service_account_path = '/Users/ericbragas/dev/exploratory-beam-pipelines/credentials/durable-return-304504-7bda905b0edc.json'
print("Service account file : ", service_account_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

pipeline_options = PipelineOptions(streaming=True, save_main_session=True)
# pipeline_options.view_as(StandardOptions).streaming = True

p = beam.Pipeline(options=pipeline_options)

result = (
    p
    | beam.io.ReadFromPubSub(subscription=f"projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}")
    | beam.io.WriteToText("./data/pubsub/output")
)

result = p.run()
result.wait_until_finish()
