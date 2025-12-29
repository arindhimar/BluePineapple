def snake_to_camel(st):
    splitStr=st.split("_")
    camelCase=""
    for i in splitStr:
        # print(i)
        camelCase+=(i[0].upper())+i[1:]
    
    return camelCase


print(snake_to_camel("arin_is_the_best"))