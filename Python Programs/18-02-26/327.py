def is_isosceles(s1, s2, s3):
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        if s1 == s2 or s2 == s3 or s1 == s3:
            return True
        else:
            return False
    else:
        return False
