import json
import postgre

def lambda_handler(event, context):
    
    query = "select * from symptoms"
    results = postgre.query_postgresql(query)
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
