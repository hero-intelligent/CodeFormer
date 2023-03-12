---
title: CodeFormer
emoji: 🐼
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 3.4
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# Information

imported from: https://huggingface.co/spaces/sczhou/CodeFormer
source code: https://github.com/sczhou/CodeFormer

# Usage

first clone this repository and navigate into the directory.

If you don't want to download pretrained models at building stage, Run `docker build --target=base -t codeformer .` to build the image and then run `docker run -v $(pwd)/CodeFormer/weights:/cf/CodeFormer/weights -p 7860:7860 --name codeformer codeformer`

If you want to build a self-contained image, run `docker build -t codeformer .` to build the image and then run `docker run -p 7860:7860 --name codeformer codeformer`

if you have a gpu, please add the argument `--gpus=all`
