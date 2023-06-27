from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, UniqueConstraint, Date, Enum, Time
from sqlalchemy.orm import relationship

from core.database.connection import Base
# from core.models.mixin import TimeStamp, GenderType

class Employees(Base):

    __tablename__ ="employees"
    id                           = Column(Integer, primary_key=True)
    employee_temp_id             = Column(String(6), nullable=False, unique=True)
    employee_id                  = Column(String(6),nullable=False, unique=True)
    name                         = Column(String(100), nullable=False)
    email                        = Column(String(100), nullable=False, unique=True)
    password                     = Column(String(200), nullable=False)
    gender                       = Column(String(20), nullable=False)
    birthdate                    = Column(String(20), nullable=False)
    profile_image                = Column(String(1024))
    primary_contact_number       = Column(String(20), nullable=False, unique=True)
    secondary_contact_number     = Column(String(20), nullable=False, unique=True)
    emergency_contact_number     = Column(String(20), nullable=False, unique=True)
    address_line1                = Column(String(255), nullable=True)
    address_line2                = Column(String(255), nullable=True)
    address_line3                = Column(String(255), nullable=True)
    address_line4                = Column(String(255), nullable=True)
    pincode                      = Column(String(200))
    designation                  = Column(String(100), nullable=False)
    level                        = Column(String(100), nullable=False)
    hire_date                    = Column(String(100), nullable=False)
    joining_date                 = Column(String(100), nullable=False)
    resignation_date             = Column(String(100), nullable=False)
    reporting_manager            = Column(String(100), nullable=False)
    reporting_manager_empid      = Column(String(100), nullable=False)