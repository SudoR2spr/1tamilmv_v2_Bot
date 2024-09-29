# Python ইমেজ ব্যবহার করুন
FROM python:3.9-slim

# কাজের ডিরেক্টরি তৈরি করুন
WORKDIR /app

# প্রয়োজনীয় ফাইলগুলো কপি করুন
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# মূল কোড কপি করুন
COPY . .

# 3000 পোর্ট প্রকাশ করুন (যদি আপনার অ্যাপ্লিকেশনটি 3000 পোর্টে রান করে)
EXPOSE 3000

# অ্যাপ্লিকেশন রান করার জন্য গুনিকর্ন কমান্ড
CMD ["python", "angel.py"]
