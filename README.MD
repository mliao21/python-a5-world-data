## 📚 Learning Outcomes
* Manipulate and analyze data using Pandas DataFrame objects
* Read Excel data into a DataFrame
* Use hierarchical indexing to sort and slice data
* Process data according to specifications
* Find missing values in a dataset
* Operate on data in Pandas

## 💻 Program Specifications
The United Nations and other international organizations collect data on various demographics worldwide.
You are being asked to design a terminal-based application for computing and printing statistics based on a provided UN sub-region name.
Your application must meet the following design specifications:
* Your final output should match the given examples (see attached screenshots)
* Stage 1: DataFrame Creation
  1. Import the provided data into a Pandas DataFrame. 
  2. You may not change or sort the Excel file.
  3. You may not hard-code/copy-paste any information into your program except for the Excel column names.
  4. Index the data in the following order: UN Region -> UN Sub-Region -> Country
  5. All of the below specifications must show the data in the correctly sorted order.
  6. You may not use global variables. You must import the data within your main function.
* Stage 2: User Entry
  1. Prompt the user to enter a sub-region name. 
  2. If the name does not exist within the given data, raise a ValueError to print “You must enter a valid UN sub-region name.” 
  3. Again, you must not hard-code the names (the UN could decide to change the sub-region names at any time!).
* Stage 3: Find Missing Data
  1. It is not always possible to collect complete data from all countries. Some countries do not have sq km area measurements. Write a function called `find_null()` to determine whether any area data is missing for the chosen sub-region.
  2. Your function may take in any arguments or return any values of your choosing.
  3. If all sq km data is available for the sub-region, print the message "There are no missing sq km values for this sub-region."
  4. If any data is missing, print the UN Region/UN Sub-Region/Country information and the NaN sq km value.
* Stage 4: Sub-Region Calculations
  1. Add two new columns to the sub-region data: a) the change in population from 2000 to 2020 and b) the current population density (num of people per sq km).
  2. Print all columns for each country in the sub-region.
  3. Conservationists are concerned about the number of threatened plant, bird, fish, and mammal species in each country. Print the number of threatened species in each category for each country in the sub-region.
  4. To better estimate possible rehabilitation and sanctuary space, calculate and print the sq km area per the total number of threatened species for each country in the sub-region.
  5. Put a clear header before each printed dataset for better readability.
* Your code should include and use at least one multi-index Pandas DataFrame, at least one IndexSlice object, a user-defined function called `find_null`, at least one masking operation, and at least one built-in Pandas or NumPy computational method.
* Your code must follow the conventions discussed so far in the course (names_with_underscores, ClassNames, four spaces for indentations, spaces between variables/operators, comments throughout, etc.)
* All classes, methods, and functions must contain docstring documentation.
    1. For each class, include a functionality summary and describe any class and/or instance variables (do not include a separate docstring for \_\_init\_\_)
    2. For each method/function, include a functionality summary and describe parameters and return values (or specify if there are none)
    3. Main functions do not need a docstring but should be well-commented