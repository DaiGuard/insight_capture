import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'insight_capture'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),        
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='DaiGuard',
    maintainer_email='DaiGuard@todo.todo',
    description='insight capture package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'insight_capture = insight_capture.insight_capture_node:main'
        ],
    },
)