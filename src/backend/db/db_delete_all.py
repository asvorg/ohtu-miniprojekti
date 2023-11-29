from db_func import connect_to_db

def delete_all_from_db():
    '''CARE'''
    collection, db, client,uri = connect_to_db()
    result = collection.delete_many({})

    # Print the result
    print(f"{result.deleted_count} document(s) deleted")

    # Close the MongoDB connection
    client.close()


delete_all_from_db()