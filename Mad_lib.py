def mad_libs():
    """Generates a Mad Libs story based on user input."""

    story_template = """
    The {adjective} {noun} {verb} over the {adjective} {noun}.
    It {adverb} {verb} a {adjective} {noun} and then {verb} away.
    The {noun} was very {adjective} and made a loud {noun} sound.
    """

    words = {}

    word_types = ["adjective", "noun", "verb", "adverb"]

    for word_type in word_types:
        while True:  # Loop until at least one word of each type is entered
            user_input = input(f"Enter an {word_type}: ")
            if user_input:  # Check if the input is not empty
                if word_type not in words:
                    words[word_type] = []
                words[word_type].append(user_input)
                break
            else:
                print("Please enter a word.")


    # Replace placeholders in the template with user input. Cycle through inputs if there are multiple for a single word type.
    story = story_template
    for word_type, word_list in words.items():
        word_index = 0
        while f"{{{word_type}}}" in story:
            story = story.replace(f"{{{word_type}}}", word_list[word_index % len(word_list)], 1) #replace only the first occurence.
            word_index +=1

    print("\nHere's your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()