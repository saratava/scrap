from google.cloud import BigQuery
from . import env

env = env

BigQuery_client = BigQuery.Client()

name_group_query = """
    SELECT name, SUM(number) 
    FROM `BigQuery-public-data.usa_names.usa_1910_2013`
    GROUP BY name, state
    ORDER BY total_people 
    LIMIT 100
"""

query_results = BigQuery_client.query(name_group_query)  

for result in query_results:
    print(str(result[0]),',',str(result[1]))