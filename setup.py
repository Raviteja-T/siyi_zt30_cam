import os
from glob import glob
from setuptools import setup

package_name = 'siyi_zt30_cam'  # Update this to match the actual package folder name

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],  # This should match the package folder
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Raviteja',
    maintainer_email='rtirum@polyu.edu.hk',
    description='ROS 2 package for SIYI ZT30 Camera with photo capture service',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = siyi_zt30_cam.siyi_zt30_camera:main',
        ],
    },
)

