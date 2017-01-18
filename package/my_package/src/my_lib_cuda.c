#include <THC/THC.h>

// this symbol will be resolved automatically from PyTorch libs
extern THCState *state;

int my_lib_add_forward_cuda(THCudaTensor *input1, THCudaTensor *input2,
		       THCudaTensor *output)
{
  if (!THCudaTensor_isSameSizeAs(state, input1, input2))
    return 0;
  THCudaTensor_resizeAs(state, output, input1);
  THCudaTensor_cadd(state, output, input1, 1.0, input2);
  return 1;
}

int my_lib_add_backward_cuda(THCudaTensor *grad_output, THCudaTensor *grad_input)
{
  THCudaTensor_resizeAs(state, grad_input, grad_output);
  THCudaTensor_fill(state, grad_input, 1);
  return 1;
}
