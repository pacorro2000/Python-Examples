def mediana(m):
    m = sorted(m)
    l = len(m)
    mit = l / 2
    if (l % 2 == 0):        
        ok = (m[mit] + m[mit - 1]) / 2.0 
    else:
        ok = m[mit]
    return ok    
print mediana([6, 8, 12, 2, 23])
