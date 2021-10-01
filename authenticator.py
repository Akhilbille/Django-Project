def authenticator_key(name,payment_id):
    name = str(name)
    payment_id = str(payment_id)
    valid_key = name[::2]+payment_id[::2]+'key'
    print(valid_key)


authenticator_key("akhil","11515sdada3s2d")    
    
    
