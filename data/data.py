exodus_db = {
    "buses": [],
    "routes": [],
    "trips": [],
}


def reset():
    for value in exodus_db.value():
        value.clear()


def seed_data():
    reset()
