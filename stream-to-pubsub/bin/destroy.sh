# quick and dirty destroy
set -ex

gcloud pubsub topics delete beam-example-input
gcloud pubsub subscriptions delete beam-example-input-sub1

gcloud pubsub topics delete beam-example-output
gcloud pubsub subscriptions delete beam-example-output-sub1

echo $(gcloud pubsub topics list)
