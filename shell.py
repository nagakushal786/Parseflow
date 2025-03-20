import parseflow
import sys

while True:
    text = input('parseflow > ')
    if text.strip() == "":
        continue
    elif text.strip().lower() == "exit":
        sys.exit()

    result, error = parseflow.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))

    # Notify user about intermediate code generation
    print("Intermediate code saved to 'intermediate_code.txt'.")