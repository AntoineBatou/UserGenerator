"""Use to generate users"""

import faker
import logging
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / "user.log", level=logging.INFO)

fake = faker.Faker()

def get_user() -> str: 
    """Generate fake name and lastname

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"
    

def get_users(nb_user: int) -> list: 
    logging.info(f"Generating a list of {nb_user} users.")
    """Génère le nombre de noms indiqué dans nb_user, dans une liste

    Args:
        nb_user (int): number of user needed to create

    Returns:
        list[str]: users
    """
    return [get_user() for _ in range(nb_user)]

if __name__ == "__main__":
    user = get_users(3)
    print(user)