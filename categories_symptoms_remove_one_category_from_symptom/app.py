import json
import postgre

def lambda_handler(event, context):
    cat_id = event['queryStringParameters']['cat_id']
    sym_id = event['queryStringParameters']['sym_id']

    query = "delete from categories_symptoms where (cat_id = '"+ cat_id +"' AND sym_id = '"+ sym_id +"')"
    
    results = postgre.query_postgresql(query)
    
    return {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                   },
        "body": json.dumps(results)
    }