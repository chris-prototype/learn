print('****************************************************************************************************')
print('PYTORCH - BACKWARD - SCALAR')
print('****************************************************************************************************')

import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
# dy/dx = 2*x + 3

# computes dy/dx and sets .grad for x
y.backward()

# prints 7.
print('dy/dx =', x.grad)

# reset x.grad
# trailing _ is a convention for in place mutations
# calling y.backward() populates x.grad, so we can ignore ty, the real time type checker enabled by replit
x.grad.zero_()

# prints 0.
print('dy/dx =', x.grad)
