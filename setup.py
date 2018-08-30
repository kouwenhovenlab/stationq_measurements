from setuptools import setup, find_packages

setup(
    name='stationq_measurements',
    version='0.0.1',
    description='Shared code for measurements and experiments within '
                'Microsoft collaboration',
    packages=find_packages(),
    url='https://github.com/kouwenhovenlab/stationq_measurements',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Licence :: MIT Licence',
        'Topic :: Scientific/Engineering'
    ],
    license='MIT',
    install_requires=[
            'qcodes>=0.1.11',
        ],
    test_suite='stationq_measurements.tests',
    python_requires='>=3',
    use_2to3=False,
)