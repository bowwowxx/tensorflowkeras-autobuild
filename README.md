# tensorflowkeras-autobuild
ubuntu16-cuda8-jupyter-tensorflow-keras

## Run Keras Container

```
docker run -d -it --name=ktf -p 8888:8888 -e KERAS_BACKEND=tensorflow -v $PWD/deep-models:/deep-models bowwow/keras-tensorflow-autobuild
```

## Accessing the jupyter
Just browse [localhost:8888](localhost:8888)