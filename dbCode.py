import pymysql
import pymysql.cursors
import creds
import boto3

def get_countries_list():
    query = "SELECT Name, Population FROM country LIMIT 15"
    return execute_query(query)

def connect():
    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query, args=()):
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows
    finally:
        conn.close()


def get_top_cities(country_name):
    query = """
        SELECT City.Name, City.Population 
        FROM City
        JOIN Country ON City.CountryCode = Country.Code
        WHERE Country.Name = %s
        ORDER BY City.Population DESC
        LIMIT 5
    """
    return execute_query(query, (country_name,))

if __name__ == "__main__":
    countries = get_countries_list()
    for country in countries:
        print(f"{country['Name']}: {country['Population']}")
