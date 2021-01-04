import one
print('TOP LEVEL IN TWO.PY')
one.func()
if __name__ == '__main__':
    print('TWO.PY IS RUNNING CORRECTLY')
else:
    print('TWO.PY IS BEING IMPORTED')