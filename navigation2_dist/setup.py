from setuptools import setup

package_name = 'navigation2_dist'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='konrad',
    maintainer_email='konrad@todo.todo',
    description='Package to measure path length of planers',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'path_len = navigation2_dist.path_len:main'
        ],
    },
)
