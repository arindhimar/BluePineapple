def find_underscore_lower(st):
    words=st.split()
    res=[]
    for w in words:
        if "_" in w and w.replace("_","").islower():
            res.append(w)
    print(res)

find_underscore_lower("abc_def XYZ x_y test_case A_b c_d_e")