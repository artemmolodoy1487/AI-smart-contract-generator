# Solidity Code Generation System

## Overview

This system is designed to generate smart contracts in the Solidity language based on user requests. It leverages a large language model to represent concepts and their relationships and provides a graphical interface for easy user interaction.

## Features

- Generation of Solidity smart contract code
- Visualization of concepts and their interrelations
- Support for natural language input for requests

## Key Concepts

### Solidity Language Concepts

- **Variable**: Stores data within a smart contract.
- **Function**: Performs actions and can modify the contract state.
- **Access Modifiers**: Define who can call contract functions (e.g., `public`, `private`).
- **Library**: A set of reusable functions for other contracts.

### Ethereum-Related Concepts

- **Voting**: Processes related to decision-making in smart contracts.
- **Transaction**: Transfer of data or funds between addresses in the Ethereum network.
- **Gas**: Unit of measurement for computational costs in the Ethereum network.

### Natural Language Elements

- **Date**: Refers to a specific day.
- **Time**: Refers to a specific moment.
- **Amount**: Defines the quantity of tokens or funds.
- **Send**: Action of transferring funds or data.
- **Receive**: Action of receiving funds or data.

## Graphical Interface

The interface allows users to:
- Input the description of the desired contract in natural language.
- View the generated code and its visualization.
- Explore relationships between various Solidity and Ethereum concepts.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/artemmolodoy1487/AI-smart-contract-generator.git
   cd AI-smart-contract-generator
   python -m venv venv
   venv\Scripts\activate // Windows
   source venv/bin/activate // macOS/Linux
   pip install -r requirements.txt
   ```
   Create a .env file in the project root and add your API key:
   ```
   MISTRAL_API_KEY=your_api_key_here
```
```uvicorn main\:app --reload
```




### MIT License

Copyright (c) 2023 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


