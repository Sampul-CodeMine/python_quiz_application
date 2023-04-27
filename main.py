#!/usr/bin/python3


def clear_screen():
    """Function that clears the screen"""
    from sys import platform as p
    from os import system as s
    os_platform = p
    if os_platform == "win32":
        s("cls")
    elif os_platform == "linux":
        s("clear")
    return

def accept_int(prompt: str) -> int | None:
    """This is function that accepts integer input from a user.

    Args:
        prompt (str): Prompt to specify the datatype to input.

    Return:
        int | None: if input is of type int, return int else None.

    Raises:
        TypeError: if the data is not of type `int`
        ValueError: if no data is provided
        Exception: if data is empty
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    while True:
        try:
            data = input(f"Enter {prompt}: ")
            if data == '':
                raise Exception("Data is required")
            if data.isdigit():
                data = int(data)
                if type(data) == int:
                    return data
                else:
                    raise ValueError("Numeric data is required.")
            else:
                raise TypeError("Numeric data is required.")
        except ValueError as err:
            print(err)
        except (Exception, TypeError) as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted.")
            exit()

def accept_str(prompt: str) -> str | None:
    """This is function that accepts String input from a user.

    Args:
        prompt (str): Prompt to specify the datatype to input.

    Return:
        str | None: string type else None.

    Raises:
        ValueError: if there is no data provided or string is empty
        TypeError: if the data procided is all digits
        Exception: if data is empty
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    while True:
        try:
            data = input(f"Enter {prompt}: ")
            if data == '':
                raise ValueError("Data is required.")
            if data.isdigit():
                raise TypeError("Data must not be numeric.")
            return data
        except (ValueError, TypeError, Exception) as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted.")
            exit()

def accept_any_input(prompt: str) -> str | None:
    """This is function that accepts any input from a user.

    Args:
        prompt (str): Prompt to specify the datatype to input.

    Return:
        str | int | None: string or int type else None.

    Raises:
        ValueError: if there is no data provided or string is empty
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    while True:
        try:
            data = input(f"Enter {prompt}: ")
            if data == '':
                raise ValueError("Data is required.")
            return data
        except ValueError as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted.")
            exit()

def main_screen():
    prompt = """
             Welcome to Sampul-CodeMine Quiz Application
    =========                                           ========

        1. Tutor
        2. Scholar
        3. Exit
    """
    print(prompt)

def read_from_json_file(fn) -> list | None:
    """This is a function that reads data from a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        ValueError: if filename is empty
        TypeError: if the data procided is all digits
        FileNotFoundError: if specified file is not found
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    from os import path
    try:
        if fn == "":
            raise ValueError("Filename is required")
        if path.getsize(fn) == 0:
            return []
        with open(fn, mode="r") as f:
            data = json.load(f)
            return data
    except ValueError as err:
        print(err)
    except FileNotFoundError as err:
        print(f"The file '{fn}' was not found.")
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted.")
        exit()

def write_to_json_file(data: list, fn: str) -> bool | None:
    """This is a function that writes `data` to a JSON file `fn`.

    Args:
        data (list): the data (list of dictionaries) to be written to the
    JSON file
        fn (str): the file to write JSON object to

    Returns:
        bool | None: If successful, returns True else return None.

    Raises:
        TypeError - if `data` is not of type list
        Exception - if specified file is not found
        (KeyboardInterrupt, EOFError) - if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    try:
        if type(data) is not list:
            raise TypeError("Invalid data cannot be added.")
        if fn == "" or fn is None:
            raise Exception("Filename is required.")
        with open(fn, mode="w", encoding="utf-8") as f:
            json.dump(data, f, sort_keys=True)
            return True
    except TypeError as err:
        print(err)
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()

def admin_login(fn: str) -> bool | None:
    clear_screen()
    prompt = """
        ====     L O G I N   P A G E     ====

    """
    print(prompt)
    data = read_from_json_file(fn)
    if len(data) == 0:
        print("No user available.")
        return
    
    result = data['privi']
    username = accept_str("Username")
    password = accept_str("Password")
    for user in result:
        uname, pwd = user
        if username == user[uname] and password == user[pwd]:
            return True
    return

def input_question() -> dict | None:
    data = {}
    options = []
    try:
        data["question"] = accept_any_input("Question")
        for i in range(4):
            opt = accept_any_input(f"Option {chr(97 + i)}")
            options.append((chr(97 + i), opt))
        data["options"] = options
        data["answer"] = accept_any_input("Answer")
        return data
    except (KeyboardInterrupt, EOFError):
        print("\nProgram halted")
        exit()

def add_question(dbf: str) -> bool | None:
    clear_screen()
    prompt = """
        ====  A D D   Q U E S T I O N  ====

    """
    try:
        try:
            raw_data = read_from_json_file(dbf)
        except Exception:
            raw_data = []
    
        print(prompt)
        data = input_question()
        if data is not None:
            raw_data.append(data)
            write_to_json_file(raw_data, dbf)
            return True
        else:
            raise Exception("We could not add data at this time. Please try\
                            again")
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()

def view_data_from_db(dbf: str) -> list | None:
    """This is a function that views the data in a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        ValueError: if filename is empty
        TypeError: if the data procided is all digits
        FileNotFoundError: if specified file is not found
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    prompt = """
        ====  V I E W   A L L   Q U E S T I O N S  ====

    """
    try:
        if dbf == "" or dbf is None:
            raise Exception("Filename is required.")
        data = read_from_json_file(dbf)
        if len(data) == 0:
            raise Exception("There are no questions available. Add Question")
        count = 1
        clear_screen()
        print(prompt)
        for item in data:
            print(f"Question #{count}")
            print(f"\tQuestion:\t{item['question']}")
            print("\tOptions:\t", end="")
            for i in item['options']:
                print(f"({i[0]}): {i[1]}", end="  ")
            print(f"\n\tAnswer:\t\t{item['answer']}")
            print("")
            count += 1
        return data
    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()   

def edit_question(dbf: str) -> bool | None:
    """This is a function that edits and updates data in a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        Exception: if `fn` is empty or data read from the JSON file is None
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    try:
        if view_data_from_db(dbf) is not None:
            
            data = view_data_from_db(dbf)
            data_len = len(data)
            edit_opt = accept_int("Edit Question #")
            if edit_opt < 0 or edit_opt > data_len:
                raise Exception(f"\nQuestion #{edit_opt} not found.\n")
            new_data = []
            q_dict = {}
            options = []
            count = 0
            for item in data:
                if count == (edit_opt - 1):
                    print(f"Current Question:\t{item['question']}")
                    q_dict["question"] = accept_any_input("New Question")
                    print("\nCurrent Options:", end="  ")
                    for i in item['options']:
                        print(f"({i[0]}): {i[1]}", end="  ")
                    print("\n\nNew Options")
                    for i in range(4):
                        opt = accept_any_input(f"New Option {chr(97 + i)}")
                        options.append((chr(97 + i), opt))
                    q_dict["options"] = options
                    print(f"\nCurrent Answer:\t{item['answer']}")
                    q_dict["answer"] = accept_any_input("New Answer")
                    new_data.append(q_dict)
                    count += 1
                else:
                    new_data.append(item)
                    count += 1
            write_to_json_file(new_data, dbf)
            return True
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()
    return

def admin_main(fn: str) -> None:
    clear_screen()
    if admin_login(fn) is None:
        clear_screen()
        print("Username/Password incorrect.")
        return
    clear_screen()
    print("Login was successful.\n")
    prompt = """
     ========== A D M I N I S T R A T I V E   P A G E ==========

     1. Add a Question
     2. Edit a Question
     3. View Questions
     4. Logout
    """
    db_file = "database.json"
    while True:
        try:
            print(prompt)
            choice = accept_int("Choice")
            if choice == 1:
                if add_question(db_file) is True:
                    clear_screen()
                    print("Question added successfully.\n")
                
            elif choice == 2:
                clear_screen()
                if edit_question(db_file) is True:
                    print("Question was successfully updated.\n")
                else:
                    print("We could not update the question at this time.\n")
            elif choice == 3:
                clear_screen()
                if view_data_from_db(db_file) is not None:
                    ...
                else:
                    print("No Questions to view.\n")
            elif choice == 4:
                clear_screen()
                print("===== LOGGING OUT =====")
                return
            else:
                clear_screen()
                print("\nInvalid option. Please choose from the right options\n")
        except Exception:
            print("fddf")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram Interrupted.\n")
            exit()
    return

def start_quiz(data: list, mark: int) -> None:
    import random
    count = 0
    score = 0
    correct_mark = 0
    incorrect_mark = 0
    result = {}
    random.shuffle(data)
    for question in data:
        clear_screen()
        count += 1
        print(f"Question #{count}\t\t\tScore: {score}\n")
        print(f"\tQuestion:\t{question['question']}\n")
        print("\tOptions:")
        a, b, c, d = question['options']
        print(f"\t\t(a). {a[1]}")
        print(f"\t\t(b). {b[1]}")
        print(f"\t\t(c). {c[1]}")
        print(f"\t\t(d). {d[1]}")
        answer = accept_any_input("Answer:  ").lower()
        if (answer == a[0] or answer == b[0] or answer == c[0] or answer == d[0])\
            and answer == question["answer"]:
            score += mark
            correct_mark += 1
        else:
            incorrect_mark += 1
            score = score
        
    result["count"] = count
    result["score"] = score
    result["failed"] = incorrect_mark
    result["passed"] = correct_mark
    return result

def user_main(fn: str) -> None:
    marks = 5
    prompt = """
             Welcome to Sampul-CodeMine Quiz Application
    =========                                           ========

    All Questions carry equal marks ({:d} marks each)

    ============================================================

    """.format(marks)
    print(prompt)
    while True:
        try:
            if fn == "" or fn is None:
                raise Exception("Filename is required.")
            data = read_from_json_file(fn)
            if len(data) == 0:
                raise Exception("There are no questions available. " +\
                                "Contact your Tutor.")
            count = 1
            # print(prompt)
            print("Do you wish to proceed? (y/n) ")
            response = input("Response: ")
            if response in "yY":
                clear_screen()
                result = start_quiz(data, marks)
                clear_screen()
                result_data = """
                Thank you for attempting the quiz.
                Quiz Summary
                ==============
                
                Your score was {}.
                You passed {} question(s).
                You failed {} question(s).
                Total Questions: {}.
                """.format(result["score"], result["passed"],\
                           result["failed"], result["count"])
                print(result_data)
                print("\n\n")
            elif response in "nN":
                clear_screen()
                return
            else:
                clear_screen()
                print("Invalid response. Try again")


        except TypeError as err:
            clear_screen()
            print(err)
        except ValueError as err:
            clear_screen()
            print(err)
        except Exception as err:
            clear_screen()
            print(err)
            return
        except (KeyboardInterrupt, EOFError):
            clear_screen()
            print("\nProgram was halted.")
            exit() 


if __name__ == "__main__":
    import json
    clear_screen()
    while True:
        try:
            main_screen()
            choice = accept_int("Choice")
            if choice == 1:
                filename = "users.json"
                clear_screen()
                admin_main(filename)
            elif choice == 2:
                filename = "database.json"
                clear_screen()
                user_main(filename)
            elif choice == 3:
                clear_screen()
                print("==== E X I T I N G    A P P L I C A T I O N ====\n")
                print("Thank you for dropping by. Do have a lovely day.")
                exit(1)
            else:
                clear_screen()
                print("\nInvalid option. Please choose from the right options\n")
        except ValueError as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram Interrupted\n")
            exit(1)
