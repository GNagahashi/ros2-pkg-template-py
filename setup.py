from setuptools import setup

package_name = 'ros2_pkg_template_py'


setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires = ['setuptools'],
    maintainer = 'Maintainer name',
    maintainer_email = 'email@example.com',
    description = 'Package description',
    license = 'License declaration',
    entry_points = {
        'console_scripts': [
            'talker = ros2_pkg_template_py.publisher:main',
        ],
    },
)
