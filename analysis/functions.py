import sqlite3
import pandas as pd

conn = sqlite3.connect("tesla_financials.db")
c = conn.cursor()

def backup_tables(current_name, backup_name):
    query = f"ALTER TABLE {current_name} RENAME TO {backup_name}"
    return c.execute(query)

backup_tables("BalanceS", "BalanceS_backup") 
backup_tables("IncomeS", "IncomeS_backup") 
backup_tables("CashFlowS", "CashFlowS_backup")
    
def create_new_tables(table_name):
    new_table_name = table_name
    query = f"CREATE TABLE {new_table_name} (PeriodEnding TEXT, '12/31/2022' INTEGER, '12/31/2021' INTEGER, '12/31/2020' INTEGER, '12/31/2019' INTEGER)"
    return c.execute(query)

create_new_tables("BalanceS_new")
create_new_tables("IncomeS_new")
create_new_tables("CashFlowS_new")

def insert_data(into_table, from_table):
    new_table = into_table
    old_table = from_table
    query = f"INSERT INTO {new_table} SELECT * FROM {old_table}"
    c.execute(query)
    conn.commit()
    
insert_data("BalanceS_new", "BalanceS_backup")
insert_data("IncomeS_new", "IncomeS_backup")
insert_data("CashFlowS_new", "CashFlowS_backup")