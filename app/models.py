from app import db

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(50), nullable=False)
    job_title = db.Column(db.String(50), nullable=False)
    work_phone_extension = db.Column(db.String(20), nullable=True)
    department = db.Column(db.String(50), nullable=False, default="Unknown")
    supervisor = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Employees {self.display_name}>"
