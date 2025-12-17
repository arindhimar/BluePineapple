def find_under_score_lower(st):
    words=st.split()
    res=[]
    for w in words:
        if "_" in w and w.replace("_","").islower():
            res.append(w)
        
    print(res)
    

# find_under_score_lower("abc_def XYZ x_y test_case A_b c_d_e ")
find_under_score_lower("valid: abc_def, x_y; invalid: Abc_def, abc__def, hello-World")