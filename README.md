## Getting Started

To get started, install the proper dependencies executing the following command. 

`pip install -r requirements.txt`

## Running commands

The following commands will allow you to run the application 

1. `python3 main.py  --Image_function` This command will take the `.PNG` provided in the `files` folder of this repo and calculate the (X,Y) centre points and radiuses from the holes detected.
    It will create a copy of the provided image as the output annotated with the information calculated.
2. `python3 main.py  --Model_function` This command will take the `.STL` provided in the `files` folder of this repo and calculate the (X,Y,Z) centre points and radiuses from the holes detected.
    It will print on the terminal the center and radius of each hole founded in the file.
3. python3 main.py  --Image_function --Model_function` This command will give you the results of preivous two items and calculate the translational and rotational components of the `.STL` file.
