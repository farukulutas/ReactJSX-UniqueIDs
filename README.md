# ReactJSX-UniqueIDs

A Python script to automatically add unique IDs to all JSX components in a React project to avoid the "No duplicate props allowed" error. The script searches through all .js and .jsx files in the specified directory, generates a unique string, and adds it as an ID to any component that doesn't already have one. The modified files are then overwritten with the updated content.

## Installation

1. Clone this repository or download the script directly.
2. Make sure you have Python installed on your machine.
3. No additional dependencies are required for this script.

## Usage

1. Open the `unique_ids.py` file in your preferred editor.
2. Set the `path` variable to the directory path of your React project.
3. Run the script.
4. Check your React project files to see that unique IDs have been added to all JSX components that didn't previously have one.

Note: If any components already have an ID, they will not be modified. However, as a result of the automatic ID assignment, there may be syntax errors that need to be fixed. It is recommended to use a linter such as the ESlint VSCode extension to help identify and fix any syntax errors that may occur due to the automatic addition of IDs.

## Contributing

Contributions to this project are always welcome! If you find any bugs or have ideas for new features, please open an issue on this repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute this script as needed.
