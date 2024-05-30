# Face-Landmarks-SPADE-Low-bandwidth-Video-Chat

## Overview

This repository implements the approach described in the paper [Low Bandwidth Video-Chat Compression using Deep Generative Models](https://arxiv.org/abs/2012.00328) Our goal is to enable high-quality video chat at extremely low bandwidths by leveraging deep generative models and advanced facial landmark techniques.

## Key Features

- **Facial Landmark Extraction**: Extracts facial landmarks on the sender's device, significantly reducing the amount of data that needs to be transmitted.
- **SPADE Integration**: Utilizes Spatially-Adaptive Denormalization (SPADE) blocks to enhance the visual quality of critical facial regions such as eyes and lips.
- **Generative Model**: Based on the First Order Motion Model for image animation, enabling realistic facial reconstructions on the receiver's device.
- **Real-Time Performance**: Optimized to run efficiently on mobile devices, ensuring smooth and real-time video chat even on low-end hardware.
- **Low Bandwidth Usage**: Achieves video calling at a few kilobits per second, making it accessible for users with limited internet connectivity.
