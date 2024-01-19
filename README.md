# Convert rife models to ncnn online
- Steps to convert:
- Fork repo, and replace train_log with desired model, -- note - have tested with 4.14, but should work with later versions unless an arch change.
- edit modify_train_log.py, at the top is the ensemble option. by default it should be false.
- Run CI in github actions.
- Download model from output (flownet.bin/flownet.param).
