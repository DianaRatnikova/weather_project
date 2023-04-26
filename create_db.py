from webapp import db, create_app

#db.create_all(create_app())
create_app()

#Use app.app_context() inside create_database. 
# This will solve your issue. I too had this issue recently after a Alchemy update.
