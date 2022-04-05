# Juce RSA Python
This is a juce RSA algorithm implementation without compiling C++ source code

# Install 
```shell
pip3 install juce-rsa-python
```

# Usage

```python
from juce_rsa_python import JuceRSA

public_key = '11,76e78a6f1f8158f8bbc85d7737218096953fedfa823a4ed45e884c3b7e7d3d0fe99cfdeae8fc5abdc1451fce4894fac9b19ae0b30973041b531753153f6f29ab'
private_key = '5aed4bbe6362e9af262fcf00cfce5345f9a95ba172a50f1adee0b2c4156ed4566ad34d099ef3157a74cd8b43b1b3072e44aeb65db623a66976435b59edbe0069,76e78a6f1f8158f8bbc85d7737218096953fedfa823a4ed45e884c3b7e7d3d0fe99cfdeae8fc5abdc1451fce4894fac9b19ae0b30973041b531753153f6f29ab'

text = 'Hello World!'

# encrypt
public_juce_rsa = JuceRSA(public_key)
encrypted = public_juce_rsa.encrypt(text)

# print(encrypted) 
# e72a9ff9b0b36bf96e5fa6a6820a9f86f11b2a82594185731368c01e466ccb24fd2c29a87ac9cd025a4f45e6b1cacf39cc2c5906d139f21f09cbcaa0f7277fb

# decrypt
private_juce_rsa = JuceRSA(private_key)
decrypted = private_juce_rsa.decrypt(encrypted)

# print(decrypted)
# Hello World!

```