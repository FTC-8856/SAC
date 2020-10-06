from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='sac',
      version='0.1',
      description='A Soft-Actor-Critic implementation in Python',
      long_description=readme(),
      url='https://github.com/FTC-8856/SAC',
      author='Caden Haustein',
      author_email='cadenhaustein@gmail.com',
      license='MIT',
      packages=['sac'],
      install_requires=[
          'numpy', 'torch'
      ],
      zip_safe=False)
