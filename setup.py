import shutil
from setuptools import setup, find_packages
from pathlib import Path
import os

# পুরানো dist, build, egg-info ফোল্ডার ডিলিট করা
for folder in ["dist", "build", "tamilmv_bot.egg-info"]:
    path = Path(__file__).parent / folder
    if path.exists() and path.is_dir():
        shutil.rmtree(path)
        print(f"Deleted old folder: {folder}")

# README ফাইল পড়ার জন্য
readme_path = Path(__file__).parent / "README.md"
try:
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Telegram bot for downloading from 1Tamilmv Torrent"

# requirements.txt ফাইল পড়ার জন্য
req_path = Path(__file__).parent / "requirements.txt"
try:
    with open(req_path, "r", encoding="utf-8") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = []
    print("Warning: requirements.txt file not found!")

# মূল setup
setup(
    name="tamilmv-bot",
    version="0.2.1",
    description="Telegram bot for downloading from 1Tamilmv Torrent magnet link",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="SudoR2spr",
    author_email="wdzoneleech@gmail.com",
    url="https://github.com/SudoR2spr/1tamilmv_v2_Bot",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Internet",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities",
        "Framework :: Flask",
        "Natural Language :: English",
    ],
    python_requires='>=3.7',
    keywords="telegram bot 1tamilmv movies torrent magnet link downloader",
    project_urls={
        "Bug Reports": "https://github.com/SudoR2spr/1tamilmv_v2_Bot/issues",
        "Source": "https://github.com/SudoR2spr/1tamilmv_v2_Bot",
    },
    license="MIT",
    platforms=["any"],
)
