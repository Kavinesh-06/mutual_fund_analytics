from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///bluestock_mf.db")

with open("./sql/schema.sql", "r") as file:
    schema = file.read()

with engine.begin() as conn:
    for statement in schema.split(";"):
        statement = statement.strip()
        if statement:
            conn.execute(text(statement))

print("Database and tables created successfully!")