def get_user(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    user = cursor.fetchone()
    print("Resultado de la consulta:", user)
    if user is None:
        print("No se encontró ningún usuario.")
    return user