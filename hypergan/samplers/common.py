def plot(config, image, file):
    """ Plot an image."""
    image = np.squeeze(image)
    print(file, image.shape)
    imsave(file, image)
