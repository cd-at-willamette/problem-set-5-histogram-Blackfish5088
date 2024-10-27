from pgl import *
from pgl import GWindow, GRect

# Part 1a: Create the histogram array
def create_histogram_array(data: list[int]) -> list[int]:
    histogram = [0] * (max(data) + 1)
    for number in data:
        histogram[number] += 1
    return histogram

# Part 1b: Print the histogram in text form
def print_histogram(hist: list[int]) -> None:
    for index, count in enumerate(hist):
        print(f"{index}: {'*' * count}")

# Part 1c: Graph the histogram in a PGL window
def graph_histogram(hist: list[int], width: int, height: int):
    gw = GWindow(width, height)
    bar_width = width / len(hist)
    max_count = max(hist)
    height_scale = height / max_count

    for i, count in enumerate(hist):
        bar_height = count * height_scale
        rect = GRect(i * bar_width, height - bar_height, bar_width, bar_height)
        rect.setFilled(True)
        rect.setColor("red")
        gw.add(rect)

# Example usage
if __name__ == "__main__":
    PI_DIGITS = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 5, 8, 9, 7, 9]
    
    # Generate the histogram array
    histogram = create_histogram_array(PI_DIGITS)
    
    # Print the histogram in text form
    print("Text-based Histogram:")
    print_histogram(histogram)
    
    # Display the histogram graphically in a PGL window
    print("Graphical Histogram:")
    graph_histogram(histogram, 400, 400)
