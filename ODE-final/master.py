import my_func

#get a new list of accounts from the tags
my_func.get_new_accounts()

#get new accounts to say if they are true accounts
accounts_to_verify = my_func.delete_repeated_and_errors()

#verify manually if the accounts are  correct
my_func.verify_and_update(accounts_to_verify)

#do the scrap
my_func.scrap()