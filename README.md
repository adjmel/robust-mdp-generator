# Password Generator

This Python script generates a strong, random password that is highly resistant to brute-force attacks. The password combines letters, digits, and punctuation to create a complex and secure string, ideal for protecting sensitive information and accounts.

## Features

- **Recommended Length**: Generates a password of 16 characters, which is considered highly secure. Passwords of this length provide a robust defense against brute-force attacks due to the large number of possible combinations.

## Libraries Used

- **`string`**: Provides common string constants such as letters, digits, and punctuation.
- **`random`**: Used to generate random selections from the character set.

## Prerequisites

- **Python 3.x**: Ensure that Python 3.x is installed on your system.

## Usage

1. **Save the script** to a file, e.g., `generate_password.py`.

2. **Run the script** from the command line by executing:

   ```bash
   python3 generate_password.py
   ```

   The script will generate a 16-character random password and print it to the console.

3. **Customize the Password Length**: If you need a password of a different length, you can modify the `generer_mot_de_passe` function call in the script. For instance, to generate a 12-character password:

   ```python
   mot_de_passe = generer_mot_de_passe(14)
   ```

## Example Usage

To use the script, open your terminal and run:

```bash
python3 generate_password.py
```
