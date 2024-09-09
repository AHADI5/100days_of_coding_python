def love_calculator(name1, name2):
    # Combine the names and convert to uppercase
    name = (name1 + name2).upper()

    # Initialize counters for TRUE and LOVE
    true_occurences = 0
    love_occurences = 0

    # Count occurrences of letters in TRUE
    true_count = sum(name.count(letter) for letter in 'TRUE')

    # Count occurrences of letters in LOVE
    love_count = sum(name.count(letter) for letter in 'LOVE')

    # Calculate the love score
    love_score = (true_count % 10) * 10 + (love_count % 10)

    # Print results
    print(f"TRUE count: {true_count}")
    print(f"LOVE count: {love_count}")
    print(f"Love score: {love_score}")


# Example usage
love_calculator("Angela Yu", "Jack Bauer")
