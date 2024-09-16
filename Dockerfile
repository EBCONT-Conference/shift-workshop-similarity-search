FROM continuumio/miniconda3:latest
WORKDIR /app
COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH /opt/conda/envs/myenv/bin:$PATH

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]
