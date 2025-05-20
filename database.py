from databases import Database

DATABASE_URL = "sqlite+aiosqlite:///./rainharder.db"

database = Database(DATABASE_URL)