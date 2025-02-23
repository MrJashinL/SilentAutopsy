# SilentAutopsy

## Overview

This tool is designed for forensic and post-mortem analysis of system incidents. It collects system logs and information, analyzes the data using Haskell and GPT-2, and generates a comprehensive report in HTML format using Ada. The tool is designed to be stealthy and removes all traces after execution.

## Features

- Collects system logs and information.
- Analyzes logs using Haskell.
- Integrates with GPT-2 for automated AI analysis.
- Generates HTML reports using Ada.
- Stealth mode to avoid detection and remove traces.

## Prerequisites

- Python 3.x
- Haskell
- Ada
- [Transformers library](https://github.com/huggingface/transformers) for GPT-2

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/username/silentautopsy.git
    cd silentautopsy
    ```

2. Install Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Install Haskell and Ada compilers.

## Usage

1. Collect and analyze data:

    ```sh
    python forensic_tool.py
    ```

2. Analyze logs with Haskell:

    ```sh
    runhaskell ForensicAnalysis.hs
    ```

3. Generate HTML report with Ada:

    ```sh
    gnatmake Forensic_Report.adb
    ./forensic_report
    ```

## Credits

Developed by Jashin L.

## License

This project is licensed under the MIT License.