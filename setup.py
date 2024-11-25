from setuptools import setup, find_packages

setup(
    name='tesmartctl',
    version='1.0.0',
    author='Pablo Saavedra',
    author_email='saavedra.pablo@gmail.com',
    description='A Python script to control the TESmart HKS801-E23-EUBK KVM switch over LAN.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/psaavedra/tesmartctl',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'tesmartctl=tesmartctl:main',
        ],
    },
)

