terraform init

cp -r /home/chow/miniconda3/envs/aws-sdk/lib/python3.8/site-packages/spotipy ../lambda_payload/viral_hits/

cp ../viral_hits.py ../lambda_payload/viral_hits/
cp ../config/playlists.py ../lambda_payload/viral_hits/config/
cp ../config/aws.py ../lambda_payload/viral_hits/config/

cd ../lambda_payload/viral_hits/

zip -r ../../payload.zip *

cd ../../.tf/

terraform plan
