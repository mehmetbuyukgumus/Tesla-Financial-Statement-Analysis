from functions import backup_tables, create_new_tables, insert_data

def main():
    backup_tables("BalanceS", "BalanceS_backup") 
    backup_tables("IncomeS", "IncomeS_backup") 
    backup_tables("CashFlowS", "CashFlowS_backup")
    create_new_tables("BalanceS_new")
    create_new_tables("IncomeS_new")
    create_new_tables("CashFlowS_new")
    insert_data("BalanceS_new", "BalanceS_backup")
    insert_data("IncomeS_new", "IncomeS_backup")
    insert_data("CashFlowS_new", "CashFlowS_backup")

if __name__ == "__name__":
    main()
    
     
    
    
    