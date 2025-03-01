from steganography.steganography import embed_message, read_embed_message

if __name__ == "__main__":
    try:
        processType = input("What do you want to do: \nEnter '1' for hide a message into a photo,\nEnter '2' for see the hidden message...\n")
        if processType == "1":
            messageInput = str(input("Enter your message to hide: "))
            inputPath = str(input("Enter the path of your photo: "))
            outputPath = str(input("Enter the output path of your photo: "))

            embed_message(inputPath,outputPath,messageInput)
        elif processType == "2":
            imagePath = str(input("Enter the path of your photo: "))
            hiddenMessage = read_embed_message(imagePath)
            print(f"Hidden message has been decrypted. The message is: {hiddenMessage}")
        else:
            print("Please enter an existing option... Exiting the program...")
    except Exception as e:
        print(f"Error message: {e}")
    except KeyboardInterrupt:
        print("\nExiting the program...")