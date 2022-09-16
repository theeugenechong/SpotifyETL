# SpotifyETL

## Description
A simple ETL data pipeline which extracts data from Spotify's Web API, specifically data on the latest hits and builds a datalake on an S3 bucket.

This datalake is built on a weekly basis with AWS Cloudwatch, which runs an AWS Lambda function every week.

SpotifyETL employs the use of Terraform, an "infrastructure as code" tool to:
 - define IAM roles and policies
 - specify the AWS lambda function to be performed for data extraction
 - configure the AWS Cloudwatch alarm to run the lambda function weekly

## How Can This Data be Used?
SpotifyETL extracts information about the latest, trending tracks, specifically from Spotify's playlist 'Viral Hits'. The type of information extracted is as follows:
| Column | Remarks |
| --- | --- |
| Year of Release | To analyze songs by the time they were released |
| Song Title | Not needed, but useful for future queries |
| Artist Name | Name of main artist  |
| Artist Genre | To analyze what song genres go viral |
| Popularity of artist | From Spotify Docs: The artist's popularity is calculated from the popularity of all the artist's tracks. The popularity score allows us to see how many of these TikTok hits are one-hit wonders, from a well-known artist, etc. |

## Architecture
![Architecture](/img/architecture.png)

## Usage
### Required packages
- spotipy (`pip install spotipy`)
- boto3 (`pip install boto3`)

### Running locally
The Python script for extracting Spotify data can be run locally via the command
```
python viral_hits.py
```
Running the following command will generate a `.csv` file locally containing data on tracks currently in the 'Viral Hits' playlist on Spotify.

### Running on the cloud
Based on how Terraform has been configured, the AWS lambda function runs the [`lambda_handler()`](https://github.com/theeugenechong/SpotifyETL/blob/c357210be5dd7e00e69f7e6ebde3243cffc4b3c1/viral_hits.py#L72) method in `viral_hits.py` and uploads the generated csv to an S3 bucket.
