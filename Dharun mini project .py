import pandas as pd

alumni_data = {
    "Name": [
        "Steve Rogers", "Tony Stark", "Bruce Banner", "Natasha Romanoff", "Clint Barton", "Wanda Maximoff", "Peter Parker", "Sam Wilson", 
        "Bucky Barnes", "Thor", "Loki", "Nick Fury", "T'Challa", "Stephen Strange", "Carol Danvers", "Peggy Carter", "Lionel Messi", "Mike Tyson", "LeBron James", "Serena Williams", "Tom Brady", "Oprah Winfrey", "Michael Jordan", "Ariana Grande", "Taylor Swift"
    ],
    "Graduation Year": [
        2010, 2012, 2015, 2018, 2016, 2014, 2013, 2011, 
        2017, 2019, 2020, 2015, 2018, 2014, 2019, 2011, 2013, 2015, 2017, 2018, 2020, 2021, 2014, 2019, 2021
    ],
    "Major": [
        "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Computer Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Mechanical Engineering", 
        "Computer Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Computer Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Computer Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Computer Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Computer Engineering"
    ],
    "Current Occupation": [
        "Design Engineer", "Structural Engineer", "Power Systems Engineer", "Software Engineer", "Automotive Engineer", "Construction Manager", "Control Systems Engineer", "Robotics Engineer", 
        "Embedded Systems Engineer", "Aerospace Engineer", "Geotechnical Engineer", "Energy Analyst", "Network Engineer", "Manufacturing Engineer", "Transportation Engineer", "Signal Processing Engineer", "Data Engineer", "Industrial Engineer", "Urban Planner", "Renewable Energy Consultant", "Automation Specialist", "HVAC Engineer", "Water Resources Engineer", "Electronics Engineer", "Cloud Architect"
    ],
    "Location": [
        "New York", "San Francisco", "Chicago", "Boston", "Los Angeles", "Houston", "Seattle", "New York", 
        "San Francisco", "Chicago", "Boston", "Los Angeles", "Houston", "Seattle", "New York", "San Francisco", "Chicago", "Boston", "Los Angeles", "Houston", "Seattle", "New York", "San Francisco", "Chicago", "Boston"
    ]
}

alumni_df = pd.DataFrame(alumni_data)

def filter_alumni():
    while True:
        show_full_list = input("\nDo you want to see the full alumni list? (yes/no): ").strip().lower()
        if show_full_list == 'yes':
            print("\nFull Alumni List:")
            print(alumni_df)
        print("\n")

        filter_option = input("Would you like to filter by 'Major', 'Location', 'Graduation Year', or 'Current Occupation'? Enter your choice: ").strip().lower()
        print("\n")

        if filter_option == "major":
            available_majors = alumni_df["Major"].unique()
            print(f"Available Majors: {', '.join(available_majors)}\n")
            while True:
                selected_major = input("Enter the major you want to filter by: ").strip().lower()
                if selected_major in [major.lower() for major in available_majors]:
                    filtered_data = alumni_df[alumni_df["Major"].str.lower() == selected_major]
                    print(f"\nAlumni with Major '{selected_major.title()}':")
                    print(filtered_data["Name"].to_list())
                    print(f"\nNumber of Alumni in '{selected_major.title()}':", len(filtered_data))
                    print("\n")
                    break
                else:
                    print(f"Invalid Major '{selected_major}'. Please choose a valid major from the list.\n")

        elif filter_option == "location":
            available_locations = alumni_df["Location"].unique()
            print(f"Available Locations: {', '.join(available_locations)}\n")
            while True:
                selected_location = input("Enter the location you want to filter by: ").strip().lower()
                if selected_location in [location.lower() for location in available_locations]:
                    filtered_data = alumni_df[alumni_df["Location"].str.lower() == selected_location]
                    print(f"\nAlumni in Location '{selected_location.title()}':")
                    print(filtered_data["Name"].to_list())
                    print(f"\nNumber of Alumni in '{selected_location.title()}':", len(filtered_data))
                    print("\n")
                    break
                else:
                    print(f"Invalid Location '{selected_location}'. Please choose a valid location from the list.\n")

        elif filter_option == "graduation year":
            try:
                selected_year = int(input("Enter the graduation year to filter by: ").strip())
                filtered_data = alumni_df[alumni_df["Graduation Year"] == selected_year]
                if not filtered_data.empty:
                    print(f"\nAlumni who graduated in '{selected_year}':")
                    print(filtered_data["Name"].to_list())
                    print("\n")
                else:
                    print(f"No alumni found who graduated in '{selected_year}'.\n")
            except ValueError:
                print("Invalid input. Please enter a valid year.\n")

        elif filter_option == "current occupation":
            available_occupations = alumni_df["Current Occupation"].unique()
            print(f"Available Occupations: {', '.join(available_occupations)}\n")
            while True:
                selected_occupation = input("Enter the occupation you want to filter by: ").strip().lower()
                if selected_occupation in [occupation.lower() for occupation in available_occupations]:
                    filtered_data = alumni_df[alumni_df["Current Occupation"].str.lower() == selected_occupation]
                    print(f"\nAlumni with Occupation '{selected_occupation.title()}':")
                    print(filtered_data["Name"].to_list())
                    print(f"\nNumber of Alumni with '{selected_occupation.title()}':", len(filtered_data))
                    print("\n")
                    break
                else:
                    print(f"Invalid Occupation '{selected_occupation}'. Please choose a valid occupation from the list.\n")

        else:
            print("Invalid filter option. Please choose 'Major', 'Location', 'Graduation Year', or 'Current Occupation'.\n")

        show_counts = input("\nDo you want to see the number of alumni in each Major and Location? (yes/no): ").strip().lower()
        if show_counts == 'yes':
            print("\nNumber of Alumni in each Major:")
            print(alumni_df["Major"].value_counts())
            print("\n")

            print("Number of Alumni in each Location:")
            print(alumni_df["Location"].value_counts())
            print("\n")

        continue_choice = input("\nDo you want to continue checking alumni data? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Goodbye!\n")
            break

filter_alumni()
