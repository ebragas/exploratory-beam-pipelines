# Overview
publish data from a local data source to Pub/Sub, then consume/transform it with Beam (DirectRunner), then publish back to Pub/Sub. Finally, subscribe and acknowledge msgs locally to verify work.

## Setup
1. Authenticate to your desired GCP Project/User using Application Default Credentials
2. Execute `run.sh`
