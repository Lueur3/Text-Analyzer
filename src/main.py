import sys
import utils as ut
import processor as ps


def show_results(stats: dict):
    k_top_words = 0
    try:
        k_top_words = input(
            "\nEnter a number for the most frequently occurring words\n(or leave this field blank to use the default value - 3)\n"
        )

        k_top_words = int(k_top_words.strip()) if k_top_words else 3

    except ValueError:
        k_top_words = 3

    top_words = ps.get_top_words(stats["word_frequencies"], k_top_words)

    print("\n\nAnalysis results for your text:")
    print(f"Total count words: {stats['total_count']}")
    print(f"The longest word: {stats['longest_word']}")
    print(f"Top {k_top_words} most common words:")
    for word in top_words:
        print(f"'{word[0]}' - {word[1]}")

    keys = ("statistic_type", "total_count", "longest_word")
    to_save = {k: v for k, v in stats.items() if k in keys}
    ut.save_stats(to_save)


def check_line(lines_generator, stats):
    for line in lines_generator:
        clean_line = ut.preprocess_line(line)
        ps.update_stats(clean_line, stats)


print(
    "Welcome to the Text Analyzer!\n\
      Select the text you want to analyze:\n\
      1) Text from a file\n\
      2) Your text"
)

user_choice = 0

try:
    user_choice = int(input())
except ValueError:
    print("Enter a number to make your selection!")
    sys.exit()

match user_choice:
    case 1:
        filename = input("Enter the file path\n")
        file_path = ""

        try:
            file_path = ut.validate_file_path(filename)

            stats = ps.init_stats(user_choice, file_path)

            lines_generator = ut.get_file_lines(file_path)

            check_line(lines_generator, stats)

            show_results(stats)

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except PermissionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

    case 2:
        print("Type your text.\n(To finish, press Enter, then Ctrl+D.)")
        user_text = sys.stdin.read().rstrip()

        try:
            ut.raw_text(user_text)

            stats = ps.init_stats(user_choice)
            lines_generator = ut.get_text_lines(user_text)
            check_line(lines_generator, stats)

            show_results(stats)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")
