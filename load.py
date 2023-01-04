from classes.aws_bucket import AwsBucket
import os
from dotenv import load_dotenv



# load_dotenv('.env')
# BUCKET_NAME = os.getenv('BUCKET_NAME')
# bucket_url = "https://" + BUCKET_NAME + ".s3.amazonaws.com/"
# https://paas-s3-broker-prod-lon-3f1af4a0-af3d-40fc-9abe-0663810d8717.s3.amazonaws.com/attachments/2022_2023_8-digit_Correlation_Table.docx
# https://paas-s3-broker-prod-lon-3f1af4a0-af3d-40fc-9abe-0663810d8717.s3.amazonaws.com/images/fruit_vegetables.png

# file = "/Users/MLavis.Admin/sites and projects/1. Online Tariff/02. loaders and downloaders/adhoc-aws-load/resources/source/2022_2023_8-digit_Correlation_Table.docx"
# file = "/Users/Matt.Lavis/Desktop/guides/guides images/exported images/fruit_vegetables.png"
file = "/Users/MLavis.Admin/sites and projects/1. Online Tariff/02. loaders and downloaders/download-taric-files/resources/commodities_xlsx/eu_commodities_2023-01-01.xlsx"
base_file_name = os.path.basename(file)
base_file_name = "2023 commodities.xlsx"

aws_path = os.path.join("images", base_file_name)
aws_path = os.path.join("documents", "commodities", base_file_name)
print(aws_path)
bucket = AwsBucket()
bucket.upload_file(file, aws_path)
