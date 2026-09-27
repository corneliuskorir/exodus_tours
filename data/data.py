exodus_db = {
    "buses": [],
    "routes": [],
    "trips": [],
}


def reset():
    for value in exodus_db.values():
        value.clear()


def seed_data():
    reset()
