# quick and dirty resource creation
set -ex

gcloud pubsub topics create beam-example-input
gcloud pubsub topics create beam-example-output

echo $(gcloud pubsub topics list)