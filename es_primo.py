def es_primo(x):
        primo = 0
        if x < 2:
            return False
        else:
            for i in range(1, x):
                if x % i == 0:
                    primo += 1
        if primo <= 1:
            return True
        else:
            return False
