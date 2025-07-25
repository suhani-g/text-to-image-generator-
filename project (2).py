# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gPahy9yO124JoNsgVtY323JKfl0t5btK
"""

import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import login
from PIL import Image
from IPython.display import display

login()

import torch
from diffusers import StableDiffusionPipeline

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

pipe.enable_attention_slicing()

prompt = "A dreamy forest landscape with glowing magical lights and soft mist"

result = pipe(prompt)
image = result.images[0]

# Show the result
display(image)

# Save it if you like
image.save("stable_diffusion_image.png")

