# Python ইমেজ ব্যবহার করুন
FROM python:3.9-slim

# সিস্টেম প্যাকেজ ইনস্টল করুন (libmagic সহ)
RUN apt-get update && apt-get install -y \
    libmagic1 \
    libmagic-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# কাজের ডিরেক্টরি তৈরি করুন
WORKDIR /app

# প্রয়োজনীয় ফাইলগুলো কপি করুন
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# মূল কোড কপি করুন
COPY . .

# 3000 পোর্ট প্রকাশ করুন
EXPOSE 3000

# অ্যাপ রান করুন
CMD ["python", "-m", "tamilmvbot.angel"]
