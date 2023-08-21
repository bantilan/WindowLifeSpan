# WindowLifeSpan

WindowLifeSpan is a Python-based program that monitors Windows applications, tracking the number of seconds they are open, and calculating the total time upon closure. This tool provides valuable insights into application usage and can be utilized for system analysis, productivity tracking, benchmarking, or other use cases.

## Features

- **Real-Time Monitoring**: Tracks all currently open Windows applications.
- **Time Calculation**: Records the exact time each window was open and calculates the total duration upon closure.
- **Excludes Blank Titles**: Omits windows with blank titles to ensure relevant tracking.

## Use Cases

- **Benchmarking**: You can use this tool to benchmark SSD, RAM Memory, CPU like tracking the duration of copy and paste task which gives you exact seconds of the operation.
- **Simple Tracking**: Track the apps you opened and the duration of your usage.

## Screenshots

![sample-screenshot](https://github.com/bantilan/WindowLifeSpan/assets/1697297/d465dc5e-25ff-4e97-94bb-2b265ee6d42f)

## Installation

### Requirements

- Python 3.x
- pygetwindow

### Steps

1. Clone the repository:

       git clone https://github.com/bantilan/WindowLifeSpan.git


2. Navigate to the directory:

       cd WindowLifeSpan

3. Install the required libraries:

       pip install -r requirements.txt

## Usage

Run the script using the following command:

       python your_script.py

The program will start monitoring all open windows and print the duration they were open once closed.

## Create Windows Executable Files

Install pyinstaller first

       pip install pyinstaller

Create the executable

       cd WindowLifeSpan
       pyinstaller WindowLifeSpan.spec

## Contact

For any questions, feel free to reach out at contact@gamingph.com or erwinbantilan@gmail.com
