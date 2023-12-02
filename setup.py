from setuptools import setup, find_namespace_packages

setup(
    name='bot_helper_dm',
    version='0.1.0',
    description='Useful bot',
    author='Bulavina Mariia',
    author_email='legomerelin@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['tabulate', 'prompt_toolkit'],
    entry_points={'console_scripts': ['bot_dm = bot_helper_dm.bot:main']}
)