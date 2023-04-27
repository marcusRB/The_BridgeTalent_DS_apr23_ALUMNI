'''
Titular

author:
date:
version:
description: 
    PEqueña descripcion del fichero

'''

def get_avg_age(birth_year):
    """
    Parameters:
    ----------
        birth_year list int
        
    Return:
    ------
        out float
    """
    
    '''
    Recogemos el valor year actual del datetime.today.year
    '''
    import numpy as np
    from datetime import datetime
    this_year = datetime.today().year # extrae el anyo
    
    # Calculamos las edades
    ages = []
    for anyo in birth_year:
        age = this_year - anyo
        ages.append(age)
    print("***"*20)
    print(ages) # mostramos el resultado parcial en pantalla

    # calculamos el promedio
    age_sum = sum(ages)
    n_people = len(ages)
    age_mean = age_sum / n_people

    print("/#"*20)

    # print(ages)
    return print(np.round(age_mean, 1))