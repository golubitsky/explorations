This is an attempt to utilize the GPU on my System76 laptop via Tensorflow in Docker.

OS:

```sh
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Pop
Description:	Pop!_OS 20.04 LTS
Release:	20.04
Codename:	focal
```

Docker:

```sh
$ docker -v
Docker version 20.10.3, build 48d30b5
```

I pulled the [tf image](https://docs.nvidia.com/deeplearning/frameworks/tensorflow-release-notes/running.html).

```sh
$ docker pull nvcr.io/nvidia/tensorflow:20.12-tf2-py3
```

I installed the [docker-container-toolkit](https://docs.nvidia.com/deeplearning/frameworks/user-guide/index.html#runcont).

```sh
$ sudo apt-get install -y docker nvidia-container-toolkit
```

I restarted the machine.

It is [not trival to use docker-compose](https://docs.docker.com/compose/gpu-support/). Therefore going to work with `docker run` commands.

```sh
golubitsky@ml ~/source/explorations/docker_gpu (master %=)                                                                                                                                                                                   
$ docker run --gpus all -it --rm nvcr.io/nvidia/tensorflow:20.12-tf2-py3 echo hi
                                                                                                                                                
================
== TensorFlow ==
================

NVIDIA Release 20.12-tf2 (build 18110405)
TensorFlow Version 2.3.1

Container image Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
Copyright 2017-2020 The TensorFlow Authors.  All rights reserved.

Various files include modifications (c) NVIDIA CORPORATION.  All rights reserved.
NVIDIA modifications are covered by the license terms that apply to the underlying project or file.

NOTE: MOFED driver for multi-node communication was not detected.
      Multi-node communication performance may be reduced.

NOTE: The SHMEM allocation limit is set to the default of 64MB.  This may be
   insufficient for TensorFlow.  NVIDIA recommends the use of the following flags:
   nvidia-docker run --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 ...

hi
```

This appears to succeed.

Need to devise a test to confirm that GPU is actually used (start [here](https://www.tensorflow.org/tutorials/quickstart/beginner)?).
