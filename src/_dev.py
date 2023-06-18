

###############################
## !!! DEV Use only
###############################
import mysql_proc
mysqldb = mysql_proc.MySqlDb()
mysqldb.delete_scores_all()
print("All Scores have been deleted!!!!")