print('****************************************************************************************************')
print('PYTORCH - BACKWARD - TENSOR')
print('****************************************************************************************************')

import torch

v = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
f = v**2 + 3*v + 1
print(f) # output is: tensor([5., 11., 19.] ...)

f_sum = f.sum()
print(f_sum) # outpus is 5 + 11 + 19 = 35 : tensor(35. ...)

# run backward propagation
# by default, .backward() requires a scalar, and sum is a standard idiom for backward propagation
f_sum.backward()
# df/dv = 2v + 3
print("df/dv =", v.grad) # output is: tensor([5., 7., 9.] ...)
