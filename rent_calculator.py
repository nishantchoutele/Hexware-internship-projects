def rent_calculator():
    total_rent = float(input("Enter the total number of the monthly rent amount:"))
    utilities = float(input("Enter the total number of monthly utility cost:"))
    num_roommates = int(input("Enter the number of roommates(Including your self)"))

    total_cost = total_rent + utilities
    per_person_share = total_cost / num_roommates

    print("\n--- Rent calculation Summery ---")
    print(f"Total monthly Rent: {total_rent:.2f}")
    print(f"Total number of Utility Cost: {utilities:.2f}")
    print(f"Number of Roommates: {num_roommates}")
    print(f"Total Monthly Cost: {total_cost:.2f} ")
    print(f"Each Person share: {per_person_share:.2f}")

    return per_person_share

rent_calculator()
