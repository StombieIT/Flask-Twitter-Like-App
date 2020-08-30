from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from views import (
	index,
	page_not_found,
	forbidden
)
from services.db import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
