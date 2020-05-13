from sqlalchemy import Boolean, Column, Integer, String, LargeBinary, ForeignKey, REAL, Numeric, DateTime, DECIMAL, \
    BIGINT
from sqlalchemy.orm import relationship
from datetime import datetime
from source import Base


class Log(Base):
    __tablename__ = 'log'
    site_id = Column(String, primary_key=True, nullable=False, default='3068432376c0c2d957a0bdc9cff202e7')
    log_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    timestamp_utc = Column(Integer, nullable=False)
    uri = Column(String, nullable=False)
    header = Column(String, nullable=False)
    remote_addr = Column(String, nullable=False)
    scheme = Column(String, nullable=False)
    method = Column(String, nullable=False)
    body_or_param = Column(String, nullable=False)
    hs256_token = Column(String)
    token = Column(String)
    status = Column(Boolean, nullable=False, default=False)
    reason = Column(String)
    stop_at_layer = Column(Integer, nullable=False, default=1)

    def __repr__(self):
        return '<Site id: {} - Log id: {}>'.format(self.site_id, self.log_id)
