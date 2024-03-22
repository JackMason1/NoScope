from setuptools import setup, find_packages

setup(
    name='nosc0pe',
    version='0.1.0',  # Adjust as per your versioning scheme
    author='Jack Mason',
    author_email='jack@jackmason.com',  # Replace with your email
    description='A tool for IP resolution, expansion, and analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JackMason1/noSc0pe',  # Replace with the actual URL
    packages=find_packages(),
    install_requires=[
        'netaddr',
        'colorama',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'nosc0pe=nosc0pe:main',  # Adjust if necessary
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust according to your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust based on your requirements
)
