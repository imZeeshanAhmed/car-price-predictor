import pickle
import pickletools
with open('LinearRegressionModel.pkl', 'rb') as f:
    data = f.read()
for op, arg, pos in pickletools.genops(data):
    if op.name in ('GLOBAL', 'STACK_GLOBAL'):
        print(op.name, arg)
