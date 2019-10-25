ARG REGISTRY
ARG TAG
FROM ${REGISTRY}/base-pytorch-1-3-cuda-10-1:${TAG}

############### copy code ###############
ARG MODULE_PATH

# Copy the code over from the base (CUDA 9 / pytorch 0.3.1) implementation.
# Docker copy does not follow symlinks, so specifying the paths by hand here.
COPY $MODULE_PATH/../unet_v2/src /workdir/src
COPY $MODULE_PATH/../unet_v2/predefined_run_configs.json /workdir/
COPY $MODULE_PATH/../unet_v2/README.md /workdir/

# Plugin info and version are different
COPY $MODULE_PATH/plugin_info.json /workdir/
COPY $MODULE_PATH/VERSION /workdir/

COPY supervisely_lib /workdir/supervisely_lib

ENV PYTHONPATH /workdir:/workdir/src:/workdir/supervisely_lib/worker_proto:$PYTHONPATH
WORKDIR /workdir/src