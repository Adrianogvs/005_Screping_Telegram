from setuptools import setup, find_packages

setup(
    name='telegram_scraper',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'telethon',
        'tqdm',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'telegram_scraper=src.main:main',
        ],
    },
)
