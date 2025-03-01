import cv2
import numpy as np

def embed_message(image_path,output_path="data/restored_grey_image.png",message="Ugur Mali"):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        bit_matrix = np.vectorize(lambda x: format(x, '08b'))(image)
        binary_message = ''.join(format(ord(c), '08b') for c in message)
        binary_message_chars = [char for char in binary_message]
        end_binary_message = ''.join(format(ord(c), '08b') for c in "#")
        end_binary_message_chars = [char for char in end_binary_message]
        
        for row_index,row in enumerate(bit_matrix):
            for column_index,column in enumerate(bit_matrix[row_index]):
                temporary = [char for char in bit_matrix[row_index][column_index]]
                if len(binary_message_chars) != 0:
                    temporary.pop()
                    temporary.append(binary_message_chars[0])
                    tempString = "".join(temporary)
                    bit_matrix[row_index][column_index] = int(tempString)
                    temporary.clear()
                    binary_message_chars.pop(0)
                elif len(end_binary_message_chars) != 0:
                    temporary.pop()
                    temporary.append(end_binary_message_chars[0])
                    tempString = "".join(temporary)
                    bit_matrix[row_index][column_index] = int(tempString)
                    temporary.clear()
                    end_binary_message_chars.pop(0)
                else:
                    break
                    
        image_array = np.array([[int(pixel, 2) for pixel in row] for row in bit_matrix], dtype=np.uint8)
        cv2.imwrite(output_path, image_array)
        print(f"Successfully hid the message... The output photo path is {output_path}")
    except Exception as e:
        print(f"Error message: {e}")

def read_embed_message(image_path="data/restored_grey_image.png"):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        bit_matrix = np.vectorize(lambda x: format(x, '08b'))(image)
        message = []
        for row_index,row in enumerate(bit_matrix):
            for column_index,column in enumerate(bit_matrix[row_index]):
                temporary = [char for char in bit_matrix[row_index][column_index]]
                message.append(temporary[-1])
                temporary.clear()
        msgString = "".join(message)
        eight_bit_chunks = [msgString[i:i+8] for i in range(0, len(msgString), 8)]
        mainMessage = []
        for chunk in eight_bit_chunks:
            if len(chunk) == 8:
                char = chr(int(chunk,2))
                if char == "#":
                    break
                mainMessage.append(char)
        mainMessageString = "".join(mainMessage)
        return mainMessageString
    except Exception as e:
        print(f"Error message: {e}")