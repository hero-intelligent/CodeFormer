FROM scratch as temp
COPY ./requirements.txt /cf/requirements.txt
COPY ./downloader.py /cf/downloader.py
COPY ./app.py /cf/app.py
COPY ./README.md /cf/README.md


FROM pytorch/pytorch:latest as base

RUN apt update && apt install -y git ffmpeg libgl1 libglib2.0-dev libsm6 libxext6

COPY --from=temp /cf /cf

WORKDIR /cf

RUN git clone https://github.com/sczhou/CodeFormer.git
RUN pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
RUN pip install gradio && python -m pip install markupsafe==2.0.1
RUN python -c "from downloader import download_images; download_images()"

# VOLUME [ "/cf/CodeFormer/weights" ]

EXPOSE 7860

CMD [ "python", "app.py" ]



FROM base

RUN python downloader.py

# VOLUME [ "/cf/CodeFormer/weights" ]

EXPOSE 7860

CMD [ "python", "app.py" ]
