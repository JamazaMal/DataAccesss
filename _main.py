import pypyodbc
conn = pypyodbc.connect('Driver={SQL Server};Server=CGOD1253874;Database=AxMaster;Trusted_Connection=yes')
curs = conn.cursor()
ssql = (
    'select t1.USERID, t3.EMPLID, t3.NAME, t1.EVCROLEID, t3.dimension '
    'from EVCUSERROLELIST t1, SYSCOMPANYUSERINFO t2,	EMPLTABLE t3 '
    'where t1.USERID = t2.USERID and t2.EMPLID = t3.EMPLID')
vals = curs.execute(ssql)
for l in vals:
    print(l)

