from sql_connection import get_sql_connection



def get_unit(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM unit"
    cursor.execute(query)
    response = []
    for (unit_id, unit_type) in cursor:
        response.append({
            'unit_id': unit_id,
            'unit_type': unit_type
        })
   # cursor.close()

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_unit(connection))
