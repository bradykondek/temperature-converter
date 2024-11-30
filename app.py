# Notes:
# ----------------------------------------------------------------------------------------------------------------------
# When dealing with a StringVar variable, to get the str value for it, use [VAR].get(), not str(VAR).
#
# Using a lambda function in a button command allows the program to wait until the button is pressed for the function to execute.
# Otherwise, without it, it will run and assign the result to command as soon as the line is run by the program, without you even clicking it first.
#
# StringVar variables are passed into functions by reference, not by value like a "normal" variable.

# Include libraries
import tkinter as tk

# Convert temperature
def convert(inputValue, startUnit, resultUnit):
    
    # Convert input value from start unit to result unit, return empty string if nothing is entered for input value
    try:  # attempt to do

        # Convert depending on input unit and result unit
        if((startUnit.get())[1] == "C"):  # if input unit is °C

            if((resultUnit.get())[1] == "F"):  # if result unit is °F
                
                # Return converted value using conversion formula
                return (float(inputValue.get()) * (9/5) + 32)
        
        if((startUnit.get())[1] =="F"):  # if input unit is °F

            if((resultUnit.get())[1] == "C"):  # if result unit is °C

                # Return converted value using conversion formula
                return ((float(inputValue.get()) - 32) * (5/9))
            
        if(((startUnit.get())[1]) == ((resultUnit.get())[1])):  # if starting unit matches result unit

            # Return the same input value, as it doesn't need to be converted to another unit
            return float(inputValue.get())
    
    except ValueError:  # except if ValueError exception arises, most likely due to no value haven been entered into the input field

        # Return empty string
        return ""

# Initialize application
def application(root):
    
    # Set application title
    root.title("Brady's Temperature Converter")

    # Set application size
    root.geometry("365x165")

    # Initialize entry and result field
    # Entry field
    entryValue = tk.StringVar(root)  # variable to keep track of user-inputted value within entry field
    entry_field = tk.Entry(root, textvariable = entryValue, width=8)
    entry_field.grid(row=1, column=1, padx=30, pady=20)

    # Arrow image to be in between the two entry and result fields
    arrow_image = tk.PhotoImage(file="assets/arrow.png").subsample(70, 70)  # assign the image to variable, and divide the width by 70, and the height by 70
    arrow_image_display = tk.Label(root, image=arrow_image)  # display the image
    arrow_image_display.grid(row=1, column=2, padx=10)

    # Result field
    resultValue = tk.StringVar(root)  # variable to keep track of converted value
    result_field = tk.Entry(root, textvariable=resultValue, state="readonly", width=8)
    result_field.grid(row=1, column=3, padx=30, pady=20)

    # Conversion menus
    # List of options
    units = ["°F", "°C"]

    # Dropdown select menu for starting unit
    starting_unit_selected_option = tk.StringVar()  # keeps track of the currently selected option within starting unit
    starting_unit_selected_option.set(units[0])  # set option to first element in units list by default
    starting_unit_dropdown = tk.OptionMenu(root, starting_unit_selected_option, *units)  # create dropdown menu, and list options
    starting_unit_dropdown.grid(row=2, column=1, pady=8)
    
    # Dropdown select menu for result unit
    result_unit_selected_option = tk.StringVar()  # keeps track of the currently selected option within resulting unit
    result_unit_selected_option.set(units[1])  # set option to second element in units list by default
    result_unit_dropdown = tk.OptionMenu(root, result_unit_selected_option, *units)
    result_unit_dropdown.grid(row=2, column=3, pady=8)

    # Update result value
    def update_result_value(newResultValue):
        
        # Update result value to input
        resultValue.set(newResultValue)

    # Swap selected units
    def swap_units(startUnit, resultUnit):

        # Unpack variables to store since input StringVar variables are passed in by reference
        startUnit = startUnit.get()
        resultUnit = resultUnit.get()
        
        # Change starting unit option to result option
        starting_unit_selected_option.set(resultUnit)

        # Change result unit option to starting option
        result_unit_selected_option.set(startUnit)
    
    # Convert button
    convert_button = tk.Button(root, text="Convert", command=lambda: update_result_value(convert(entryValue, starting_unit_selected_option, result_unit_selected_option)))
    convert_button.grid(row=2, column=2, pady=8)

    # Swap units button
    swap_units_button = tk.Button(root, text="Swap Units", command=lambda: swap_units(starting_unit_selected_option, result_unit_selected_option))
    swap_units_button.grid(row=3, column=2, pady=5)

    # Execute app
    root.mainloop()

# Main function
def main():

    # Create application window
    root = tk.Tk()
    
    # Run application
    application(root)

# Execute program
if __name__ == "__main__":

    # Run main function
    main()