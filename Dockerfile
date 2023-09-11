FROM python:3.11.5-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip wheel && \
  pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec streamlit run frontend.py
