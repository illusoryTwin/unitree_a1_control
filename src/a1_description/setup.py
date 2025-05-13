from setuptools import find_packages, setup
import os 
from glob import glob 

package_name = 'a1_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # (os.path.join('share', package_name, 'launch'), glob('launch/*.rviz')),
        # Install URDF/Xacro files
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'xacro'), glob('xacro/*.xacro')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.dae')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.png')),
        # Install Gazebo world files
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ekaterina',
    maintainer_email='mozhegova04@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
