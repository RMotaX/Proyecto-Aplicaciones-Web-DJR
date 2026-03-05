def validate_category(id_categoty:int):
    
    category = ""

    if(id_categoty == 1):
        category = "Botanas"
    elif(id_categoty == 2):
        category = "Electronicos"
    else:
        category = "Categoria inexistente"
    
    return category