import redis

# Connexion
r = redis.Redis(host='localhost', port=6379, db=0)

# CREATE
def create_user(user_id, name):
    r.set(user_id, name)
    print(f" user {user_id} ==>  {name}")

# READ
def get_user(user_id):
    name = r.get(user_id)
    if name:
        print(f"user found : {name}")
    else:
        print(f"user {user_id} not found ")
    return name

# UPDATE
def update_user(user_id, new_name):
    if r.exists(user_id):
        r.set(user_id, new_name)
        print(f" user {user_id} updated : {new_name}")
    else:
        print(f"user {user_id} not found ")

# DELETE
def delete_user(user_id):
    if r.exists(user_id):
        r.delete(user_id)
        print(f" user {user_id} deleded")
    else:
        print(f"user {user_id} not found ")

# Test CRUD
if __name__ == "__main__":
    create_user('user:1:name', 'John Doe')
    get_user("user:1")

    # update_user("user:1", "moz")
    # get_user("user:1")

    # delete_user("user:1")
    # get_user("user:1")
