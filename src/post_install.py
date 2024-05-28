import os

def create_env_file():
    env_vars = {
        "API_ID": "",
        "API_HASH": "",
        "PHONE_NUMBER": "+55",
        "USERNAME": "",
        "START_DATE": "2024-05-01T00:00:00",
        "END_DATE": "2024-05-31T23:59:59",
        "GROUP_URL": ""
    }

    with open('.env', 'w') as f:
        for var, value in env_vars.items():
            f.write(f"{var}={value}\n")

if __name__ == "__main__":
    create_env_file()
