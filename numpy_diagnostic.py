import numpy as np
print(np.__version__)
print(np.__file__)
try:
    import numpy._core
    print('imported numpy._core')
except Exception as e:
    print('numpy._core import failed:', type(e).__name__, e)
