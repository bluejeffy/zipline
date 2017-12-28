import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

SESSION_BAR_TABLE = 'bars'

class full(Base):
    __tablename__ = 'full'

    code = Column(String, primary_key=True)
    report_date = Column(Date)
    trade_date = Column(Date, primary_key=True)
    quarter = Column(Integer)
    name = Column(String)
    eps = Column(Float)
    eps_yoy = Column(Float)
    bvps = Column(Float)
    roe = Column(Float)
    epcf = Column(Float)
    net_profits = Column(Float)
    profits_yoy = Column(Float)
    distrib = Column(Float)
    net_profit_ratio = Column(Float)
    gross_profit_rate = Column(Float)
    business_income = Column(Float)
    bips = Column(Float)
    arturnover = Column(Float)
    arturndays = Column(Float)
    inventory_turnover = Column(Float)
    inventory_days = Column(Float)
    currentasset_turnover = Column(Float)
    currentasset_days = Column(Float)
    mbrg = Column(Float)
    nprg = Column(Float)
    nav = Column(Float)
    targ = Column(Float)
    epsg = Column(Float)
    seg = Column(Float)
    currentratio = Column(Float)
    quickratio = Column(Float)
    cashratio = Column(Float)
    icratio = Column(Float)
    sheqratio = Column(Float)
    adratio = Column(Float)
    cf_sales = Column(Float)
    rateofreturn = Column(Float)
    cf_nm = Column(Float)
    cf_liabilities = Column(Float)
    cashflowratio = Column(Float)


class Shares(Base):
    __tablename__ = 'shares'
    sid = Column(Integer, primary_key=True)
    effective_date = Column(Integer, primary_key=True)
    shares = Column(Float)
    circulation = Column(Float)


class SessionBar(Base):
    __tablename__ = SESSION_BAR_TABLE
    id = Column(Integer, primary_key=True)
    day = Column(Float, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)



class fundamental(Base):
    __tablename__ = 'fundamental'

    code = Column(String, primary_key=True)
    report_date = Column(Date, primary_key=True)
    quarter = Column(Integer, primary_key=True)
    name = Column(String)
    eps = Column(Float)
    eps_yoy = Column(Float)
    bvps = Column(Float)
    roe = Column(Float)
    epcf = Column(Float)
    net_profits = Column(Float)
    profits_yoy = Column(Float)
    distrib = Column(Float)
    net_profit_ratio = Column(Float)
    gross_profit_rate = Column(Float)
    business_income = Column(Float)
    bips = Column(Float)
    arturnover = Column(Float)
    arturndays = Column(Float)
    inventory_turnover = Column(Float)
    inventory_days = Column(Float)
    currentasset_turnover = Column(Float)
    currentasset_days = Column(Float)
    mbrg = Column(Float)
    nprg = Column(Float)
    nav = Column(Float)
    targ = Column(Float)
    epsg = Column(Float)
    seg = Column(Float)
    currentratio = Column(Float)
    quickratio = Column(Float)
    cashratio = Column(Float)
    icratio = Column(Float)
    sheqratio = Column(Float)
    adratio = Column(Float)
    cf_sales = Column(Float)
    rateofreturn = Column(Float)
    cf_nm = Column(Float)
    cf_liabilities = Column(Float)
    cashflowratio = Column(Float)