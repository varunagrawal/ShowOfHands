# Main
import pygame
import pygame.camera

pygame.init()

def save_image(img_name):

    camera_error = 5

    pygame.camera.init()
    cam = None
    
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0], (640,480), "RGB")
    
    cam.start()

    cam.set_controls(False, False, 30)

    for i in range(camera_error):
        # get and discard error images due to camera boot time
        cam.get_image()

    image = cam.get_image()
    pygame.image.save(image, img_name)

    print cam.get_controls()
    cam.stop()

if __name__ == "__main__":
    save_image("image.jpg")
