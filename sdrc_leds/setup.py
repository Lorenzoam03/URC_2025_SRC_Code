from setuptools import setup
from glob import glob

package_name = 'sdrc_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=['sdrc_navigation'],  # Matches sdrc_navigation/sdrc_navigation/
    package_dir={'sdrc_navigation': 'sdrc_navigation'},  # Maps to the nested directory
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lorenzoam',
    maintainer_email='lamart66@asu.edu',
    description='Navigation package for the URC 2025 rover project',
    license='TODO: License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mock_gnss_publisher = sdrc_navigation.mock_gnss_publisher:main',  # Updated path
        ],
    },
)