# quick and dirty resource creation
set -ex

gcloud pubsub topics create beam-example-input
gcloud pubsub subscriptions create beam-example-input-sub1 --topic beam-example-input

gcloud pubsub topics create beam-example-output
gcloud pubsub subscriptions create beam-example-output-sub1 --topic beam-example-output

echo $(gcloud pubsub topics list)