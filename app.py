import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Env vars from Lambda config
s3_output_path = os.environ['s3_cleansed_layer']
glue_db = os.environ['glue_catalog_db_name']
glue_table = os.environ['glue_catalog_table_name']
write_mode = os.environ.get('write_data_operation', 'overwrite')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        # Read raw JSON
        df_raw = wr.s3.read_json(f"s3://{bucket}/{key}")

        # Flatten the 'items' list
        df_flat = pd.json_normalize(df_raw['items'])

        # Write to Parquet + register in Glue
        result = wr.s3.to_parquet(
            df=df_flat,
            path=s3_output_path,
            dataset=True,
            database=glue_db,
            table=glue_table,
            mode=write_mode
        )

        return {
            "status": "success",
            "written_rows": len(df_flat),
            "glue_table": glue_table,
            "s3_output": s3_output_path
        }

    except Exception as e:
        print(f"Error: {e}")
        raise
