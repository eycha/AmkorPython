import pymssql
from pandasql import *

    conn = pymssql.connect(server='10.101.1.102', user='autosw', password='Amkor123!', database='[Internal_Test].[dbo].[ECID_Test]')

sql = """
select * from ECID_Test

insert into ECID_Test values (
12341235, 1, 811, 'T8V727.00', '01', 'lid_id', 'KKC2204T8V72710547000', 'T8V727_11', 11, 11, '20220101111111', '20220101111111', '20220101111111', 'Python', 'EYCHA')
"""

data = pd.read_sql(sql=sql, con=conn)
