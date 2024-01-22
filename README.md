# Convert rife models to ncnn online
- Steps to convert:
- Fork repo, and replace train_log with desired model, -- note - have tested with 4.14, but should work with later versions unless an arch change.
- edit config, at the top is the ensemble option. by default it should be false,-
  * fp16 just means 16 bit limit, if disabled it will export 32 bit, usually doesnt make difference.
  * conversion_method, 2 options are pnnx and onnx, they will export the same model but one will do it with pnnx and one with onnx.
- Run CI in github actions.
- Download model from output (flownet.bin/flownet.param).
