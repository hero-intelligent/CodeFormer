FROM pytorch/pytorch:latest as base

RUN apt update && apt install -y git ffmpeg libgl1 libglib2.0-dev libsm6 libxext6

COPY ./requirements.txt /cf/requirements.txt
COPY ./downloader.py /cf/downloader.py

WORKDIR /cf

RUN pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
RUN pip install gradio && python -m pip install markupsafe==2.0.1
RUN python -c "from downloader import download_images; download_images()"

COPY . /cf

VOLUME [ "/cf/CodeFormer/weights" ]

EXPOSE 7860

CMD [ "python", "app.py" ]



FROM base

RUN python downloader.py

VOLUME [ "/cf/CodeFormer/weights" ]

EXPOSE 7860

CMD [ "python", "app.py" ]
