# quick and dirty destroy
set -ex

gcloud pubsub topics delete beam-example-input
gcloud pubsub topics delete beam-example-output

echo $(gcloud pubsub topics list)
