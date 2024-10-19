# HeliosIA

HeliosIA is an AI-powered tool designed to analyze nighttime road usage by cars and pedestrians using drone-captured videos. By processing high-altitude, downward-looking footage, HeliosIA maps traffic patterns, visualizes pedestrian movement, and provides valuable insights into road utilization under low-light conditions.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Processing Raw Videos](#processing-raw-videos)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Traffic Analysis**: Detects and tracks vehicles and pedestrians in nighttime drone footage.
- **Visualization**: Maps and visualizes traffic patterns and pedestrian movements.
- **Insights**: Provides data-driven insights on road utilization during low-light conditions.
- **AI-Powered**: Utilizes advanced AI algorithms for object detection and tracking.

## Prerequisites

- Python 3.7 or higher
- Required Python packages (see `requirements.txt`)
- Processed video data (see [Processing Raw Videos](#processing-raw-videos))

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Septimus4/HeliosIA.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd HeliosIA
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Processed Videos**

   Ensure your drone-captured videos are processed using [HeliosPostProcessing](https://github.com/Septimus4/HeliosPostProcessing) before analysis.

2. **Run the Analysis**

   ```bash
   python analyze.py --input path_to_processed_videos --output results/
   ```

3. **View Results**

   Analysis results will be saved in the specified output directory. Use provided visualization tools to interpret the data.

## Processing Raw Videos

To process raw drone videos for use with HeliosIA, utilize the [HeliosPostProcessing](https://github.com/Septimus4/HeliosPostProcessing) tool. This pre-processing step includes stabilizing footage, enhancing low-light visibility, and formatting data for analysis.

**Steps:**

1. **Clone HeliosPostProcessing**

   ```bash
   git clone https://github.com/Septimus4/HeliosPostProcessing.git
   ```

2. **Process Videos**

   Follow the instructions in the HeliosPostProcessing repository to prepare your videos.

3. **Output**

   Use the processed videos as input for HeliosIA.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
