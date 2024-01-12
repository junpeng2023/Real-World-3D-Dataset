import cv2
import torch
import torchvision.transforms as T
from midas.midas_net import MidasNet

# Load the MiDaS model
model_path = "path/to/midas_model.pt"
model = MidasNet(model_path)
model.eval()

def frame_to_depth_map(model, frame):
    transform = T.Compose(
        [
            T.ToTensor(),
            T.Resize((384, 384)),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    input_tensor = transform(frame).unsqueeze(0)

    with torch.no_grad():
        depth_map = model(input_tensor)

    depth_map = depth_map.squeeze().numpy()

    # Normalize the depth map to [0, 255]
    depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())
    depth_map = (depth_map * 255).astype("uint8")

    return depth_map