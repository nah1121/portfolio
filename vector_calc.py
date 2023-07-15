from tkinter import Frame, Entry, LEFT, Button, Tk, Label, Toplevel, messagebox
from math import sqrt, acos, degrees

root = Tk()
root.title("Vector Calculator")

vector_entries = []


def add_vector():
    frame = Frame(root)
    frame.grid(row=len(vector_entries), columnspan=3)
    entry = Entry(frame)
    entry.pack(side=LEFT)
    Label(frame, text=f"Vector {len(vector_entries) + 1} (comma separated components)", font=("Helvetica", 12)).pack(side=LEFT)
    vector_entries.append(entry)

    # Update row numbers for Add Vector, Remove Vector, and Calculate buttons
    add_button.grid(row=len(vector_entries) + 1, column=0)
    remove_button.grid(row=len(vector_entries) + 1, column=1)
    calc_button.grid(row=len(vector_entries) + 2, column=0, columnspan=3)

def remove_vector():
    if vector_entries:
        vector_entries[-1].master.destroy()
        vector_entries.pop()

        # Update row numbers for Add Vector, Remove Vector, and Calculate buttons
        add_button.grid(row=len(vector_entries) + 1, column=0)
        remove_button.grid(row=len(vector_entries) + 1, column=1)
        calc_button.grid(row=len(vector_entries) + 2, column=0, columnspan=3)


def calculate():
    try:
        vectors = [list(map(float, entry.get().split(','))) for entry in vector_entries]
        if not all(len(vector) == len(vectors[0]) for vector in vectors):
            raise ValueError("All vectors must have the same number of components.")

        resultant = [sum(vector[i] for vector in vectors) for i in range(len(vectors[0]))]
        magnitude = sqrt(sum(x ** 2 for x in resultant))

        # Create a new window to display the results
        result_window = Toplevel(root)
        result_window.title("Results")

        # Display the resultant and magnitude
        Label(result_window, text="Resultant:", font=("Helvetica", 13)).grid(row=0, column=0)
        Label(result_window, text=str(resultant), font=("Helvetica", 13)).grid(row=0, column=1)
        Label(result_window, text="Magnitude of the resultant:", font=("Helvetica", 13)).grid(row=1, column=0)
        Label(result_window, text=str(magnitude), font=("Helvetica", 13)).grid(row=1, column=1)

        # Calculate and display the dot product
        dot_product = sum(a * b for a, b in zip(vectors[0], vectors[1]))
        Label(result_window, text="Dot Product of first two vectors:", font=("Helvetica", 13)).grid(row=2, column=0)
        Label(result_window, text=str(dot_product), font=("Helvetica", 13)).grid(row=2, column=1)

        # Calculate and display the cross product (only for 3D vectors)
        if len(vectors[0]) == 3:
            cross_product = [
                vectors[0][1] * vectors[1][2] - vectors[0][2] * vectors[1][1],
                vectors[0][2] * vectors[1][0] - vectors[0][0] * vectors[1][2],
                vectors[0][0] * vectors[1][1] - vectors[0][1] * vectors[1][0],
            ]
            Label(result_window, text="Cross Product of first two vectors:", font=("Helvetica", 13)).grid(row=3, column=0)
            Label(result_window, text=str(cross_product), font=("Helvetica", 13)).grid(row=3, column=1)
        else:
            Label(result_window, text="Cross Product of first two vectors:", font=("Helvetica", 13)).grid(row=3, column=0)
            Label(result_window, text="Only for 3D vectors", font=("Helvetica", 13)).grid(row=3, column=1)

        # Calculate and display the angle between the first two vectors
        magnitude_v1 = sqrt(sum(x ** 2 for x in vectors[0]))
        magnitude_v2 = sqrt(sum(x ** 2 for x in vectors[1]))
        angle_rad = acos(dot_product / (magnitude_v1 * magnitude_v2))
        angle_deg = degrees(angle_rad)
        Label(result_window, text="Angle formed by the first two vectors (degrees):", font=("Helvetica", 13)).grid(row=4, column=0)
        Label(result_window, text=str(angle_deg), font=("Helvetica", 13)).grid(row=4, column=1)

    except Exception as e:
        messagebox.showerror("Error", str(e))


add_button = Button(root, text="Add Vector", command=add_vector, font=("Helvetica", 13))
add_button.grid(row=0, column=0)

remove_button = Button(root, text="Remove Vector", command=remove_vector, font=("Helvetica", 13))
remove_button.grid(row=0, column=1)

calc_button = Button(root, text="Calculate", command=calculate, font=("Helvetica", 13))
calc_button.grid(row=1, column=0, columnspan=3)

root.mainloop()
