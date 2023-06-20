import mysql.connector
import os
from dotenv import load_dotenv

############################################
### Insert WIP Score into MySQL Database ###
############################################

class MySqlDb:
  def __init__(self):
    load_dotenv()
    self.conn = mysql.connector.connect(
        database=os.getenv('MYSQL_DB'),
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PW'),
        charset='utf8mb4',
        autocommit=True,
        connection_timeout=60
    )
  
  #####################
  # Insert WIP score into the table
  #####################

  def insert_wip_score(self, score_json):
    print('insert_wip_score')
    cur = self.conn.cursor()
    
    wip_tbl = os.getenv('MYSQL_TBL')

    sql = f"""
    INSERT INTO { wip_tbl } 
      (company_id, 
      chat_sys, 
      origin, 
      display_name, 
      user_id, 
      doc_id,
      conversation_id, 
      thread_id, 
      message_id, 
      date, 
      time, 
      who_to_do, 
      by_when, 
      from_when, 
      until_when, 
      at_where, 
      in_where, 
      from_where, 
      to_where, 
      how_to_do, 
      how_much, 
      how_many, 
      what_to_do, 
      why)
    VALUES
      (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data = (
      score_json['company_id'], 
      score_json['chat_sys'], 
      score_json['origin'], 
      score_json['display_name'], 
      score_json['user_id'], 
      score_json['doc_id'], 
      score_json['conversation_id'], 
      score_json['thread_id'], 
      score_json['message_id'], 
      score_json['date'], 
      score_json['time'], 
      score_json['who_to_do'], 
      score_json['by_when'], 
      score_json['from_when'], 
      score_json['until_when'], 
      score_json['at_where'], 
      score_json['in_where'], 
      score_json['from_where'], 
      score_json['to_where'], 
      score_json['how_to_do'], 
      score_json['how_much'], 
      score_json['how_many'], 
      score_json['what_to_do'], 
      score_json['why'])

    print(data)

    cur.execute(sql, data)
    self.conn.commit()

    return True
  

  #################
  #  !!!! Use for DEV only !!!!
  # Delete all scores
  #################
  def delete_scores_all(self):
    cur = self.conn.cursor()
    wip_tbl = os.getenv('MYSQL_TBL')
    sql = f""" DELETE FROM { wip_tbl }; """
    cur.execute(sql)
    self.conn.commit()



  def close(self):
    self.conn.close()

  def __del__(self):
    self.close()


if __name__ == "__main__":
  
  print('Delete All Records!!!')
  db = MySqlDb()
  db.delete_scores_all()

  
