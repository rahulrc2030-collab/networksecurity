from setuptools import find_packages,setup
from typing import List

# this func will return a lsit of string which will be our requirements


def get_req()->List[str]:
    req_list:List[str]=[]


    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines :
                requirement=line.strip()
                if requirement and requirement !="-e .":
                    req_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return req_list





setup(

    name="networksecurity",
    version="0.0.1",
    author="rhaul chalkapur",
    packages=find_packages(),
    install_requires=get_req(),
    author_email="rahulrc2030@gmail.com"

)












