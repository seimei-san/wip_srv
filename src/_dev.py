

###############################
## !!! DEV Use only
###############################
import src.mysql_func as mysql_func
mysqldb = mysql_func.MySqlDb()
mysqldb.delete_scores_all()
print("All Scores have been deleted!!!!")