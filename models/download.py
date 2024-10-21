# import kagglehub

# # Download latest version
# path = kagglehub.model_download("google/movenet/tensorFlow2/singlepose-lightning")

# print("Path to model files:", path)

# import tensorflow as tf

# # Load the model
# model_path = r"D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models"
# model = tf.saved_model.load(model_path)
# # Assuming 'model' is your loaded model
# model.summary()


import tensorflow as tf

# Load the MoveNet model
model_path = r"D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models"
model = tf.saved_model.load(model_path)

# Get the signature and output names
concrete_func = model.signatures["serving_default"]
print(concrete_func.outputs)





# # Get the serving_default signature
# signature = model.signatures['serving_default']

# # Print out the input and output layer details
# print("Input details:")
# for input_tensor in signature.inputs:
#     print(f"Name: {input_tensor.name}, Shape: {input_tensor.shape}, Type: {input_tensor.dtype}")

# print("\nOutput details:")
# for output_tensor in signature.outputs:
#     print(f"Name: {output_tensor.name}, Shape: {output_tensor.shape}, Type: {output_tensor.dtype}")
