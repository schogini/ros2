from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sree',
    maintainer_email='sree@example.com',
    description='My ROS2 Python package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'hello_node = my_py_pkg.hello_node:main',
        ],
    },
)