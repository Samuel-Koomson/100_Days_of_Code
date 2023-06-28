# bookshop = [
#     [
#         "Fiction",
#         [
#             ["Mystery", [
#                 ["The Hound of the Baskervilles", "Arthur Conan Doyle", 9.99],
#                 ["The Maltese Falcon", "Dashiell Hammett", 12.99]
#             ]]]]]
# book_price = [book[2] for category, subcategories in bookshop for subcategory, books in category for book in books]
# average = sum(book_price) / len(book_price)
# print(average)

# This is a list about a BookShop
# Use list comprehension to find the average price of all the books in the bookshop.
bookshop = [
    [
        "Fiction",
        [
            ["Mystery", [
                ["The Hound of the Baskervilles", "Arthur Conan Doyle", 9.99],
                ["The Maltese Falcon", "Dashiell Hammett", 12.99]
            ]],
            ["Science Fiction", [
                ["Dune", "Frank Herbert", 15.99],
                ["Neuromancer", "William Gibson", 13.99]
            ]],
            ["Fantasy", [
                ["The Hobbit", "J.R.R. Tolkien", 14.99],
                ["A Game of Thrones", "George R.R. Martin", 18.99]
            ]]
        ]
    ],
    [
        "Non-fiction",
        [
            ["Biography", [
                ["Steve Jobs", "Walter Isaacson", 16.99],
                ["The Autobiography of Benjamin Franklin", "Benjamin Franklin", 9.99]
            ]],
            ["History", [
                ["Guns, Germs, and Steel", "Jared Diamond", 12.99],
                ["A People's History of the United States", "Howard Zinn", 19.99]
            ]],
            ["Science", [
                ["A Brief History of Time", "Stephen Hawking", 11.99],
                ["The Selfish Gene", "Richard Dawkins", 14.99]
            ]]
        ]
    ]
]

book_price = [book[2] for category in bookshop for subcategory in category for book_list in subcategory for book in book_list]
average_price = sum(book_price) / len(book_price)

print(average_price)

# book_price = [book[2] for category, subcategories in bookshop for subcategory, books in subcategories for book in books]
# average_price = sum(book_price) / len(book_price)
#
# print(average_price)

