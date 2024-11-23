from PIL import Image

def split_image(image_path, output_dir):
    try:
        # Open the image
        img = Image.open(image_path)
        width, height = img.size
        
        # Validate dimensions are divisible by 3
        if width % 3 != 0 or height % 3 != 0:
            print("Image dimensions should be divisible by 3.")
            return

        # Calculate size of each grid cell
        grid_width = width // 3
        grid_height = height // 3
        
        # Loop through each grid cell
        for row in range(3):
            for col in range(3):
                left = col * grid_width
                upper = row * grid_height
                right = left + grid_width
                lower = upper + grid_height

                # Crop and save each part
                cropped_img = img.crop((left, upper, right, lower))
                output_path = f"{output_dir}/section_{row}_{col}.png"
                cropped_img.save(output_path)
                print(f"Saved: {output_path}")
        
        print("Image split and saved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user input for the image file and output directory
    input_image = input("Enter the path to the image: ").strip()
    output_directory = input("Enter the output directory path: ").strip()

    # Run the split image function
    split_image(input_image, output_directory)



