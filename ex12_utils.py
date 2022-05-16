import boggle_board_randomizer

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1),
              (1, 1)]


def create_word_dict(file):
    """

    :param file: the file that we want to turn into a dictionary
    :return: a dictionary of words. the value of each word will be 0 if the
    word wasn't used by the user and 1 otherwise.
    """
    with open(file, "r") as words_file:
        words_dict = {}
        for line in words_file:
            words_dict[line.split()[0]] = 0
    return words_dict

# def binary_search_word(word,dict, low, high):
#     if high <= low:
#         return -1
#     mid = (high + low ) //2
#     if dict[mid] == word:
#         return





def is_ind_on_board(ind, board):
    """

    :param ind: a Tuple with the location we want to check.
    :param board:
    :return: True if the location is legal. False otherwise.
    """
    row, col = ind[0], ind[1]
    if row >= len(board) or row < 0:
        return False
    if col >= len(board[0]) or col < 0:
        return False
    return True


def possible_moves(board, row, col):
    """ This function returns a dictionary with all the possible moves of
    of the user and the current location that the user is in."""
    list_of_moves = []
    # checks that the current location is on the board:
    if is_ind_on_board((row, col), board):
        list_of_moves.append((row, col))
    else:
        return list_of_moves

    for direction in DIRECTIONS:
        d_row, d_col = direction[0], direction[1]
        if is_ind_on_board((row + d_row, col + d_col), board):
            list_of_moves.append((row + d_row, col + d_col))
    return list_of_moves



def check_path_moves_legal(board, path):
    """This function checks that the path given is a legal path on the
    board."""
    word_in_board = ""
    # make sure that the user didn't step on the same location more than once
    # or the path is empty:
    set_of_path = set(path)
    if not path or len(set_of_path) != len(path):
        return

    # Create a dictionary of all possible moves:
    possible_moves_lst = possible_moves(board, path[0][0], path[0][1])

    for ind in range(len(path)):
        row, col = path[ind][0], path[ind][1]
        # Check that the current location is in the possible moves:
        if (row, col) in possible_moves_lst:
            word_in_board += board[row][col]
        else:
            return
        possible_moves_lst = possible_moves(board, path[ind][0], path[ind][1])
    return word_in_board


def is_valid_path(board, path, words):
    """

    :param board:
    :param path:
    :param words:
    :return: None - if the path isn't valid or the word isn't in the dictionary
             The word otherwise.
    """
    word_in_board = check_path_moves_legal(board, path)
    if word_in_board in words:
        return word_in_board


def find_length_n_paths(n, board, words):
    """This function returns a list of all paths on the board that create a
    word from the words collection."""
    all_path = find_general_length_n_paths(n, board)
    all_good_path = []
    # words_lst = []
    for path in all_path:
        word = is_valid_path(board, path, words)
        if word:
            all_good_path.append(path)
            # words_lst += [word]
    return all_good_path


def find_general_length_n_paths(n, board):
    """This function will return all the paths with the length of n on
    the board."""
    result = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            start_point = (row, col)
            result += find_point_length_n_paths(n, board, [],
                                                1, [start_point], False)
    return result


def find_point_length_n_paths(n, board, list_of_legal, counter,
                              path, flag):
    """
    :param n: number of paths
    :param board: the board of the game
    :param list_of_legal:
    :param counter: length of path/ word
    :param path: current path
    :param flag: True if we are returning paths according to length of words.
                 False if we are returning paths with length n.
    :return: a list of legal paths from a specific point
    """
    if counter > n:
        return
    if counter == n:
        list_of_legal.append(path[:])
        return list_of_legal
    possible_m = possible_moves(board, path[-1][0], path[-1][1])
    for point in possible_m:
        if point not in path:
            path.append(point)
            if flag:
                find_point_length_n_paths(n, board,
                                          list_of_legal,
                                          counter + len(board[point[0]][point[1]]), path, flag)
            else:
                find_point_length_n_paths(n, board,
                                          list_of_legal,
                                          counter + 1, path, flag)
            path.pop()
    return list_of_legal


def find_length_n_words(n, board, words):
    """This function will return all the paths on the board that create words
    from the words collection with the length of n."""
    all_path = find_all_words_n_paths(n, board, words)
    all_good_path = []
    for path in all_path:
        word = is_valid_path(board, path, words)
        if word:
            all_good_path.append(path)
    return all_good_path


def find_all_words_n_paths(n, board, words):
    result = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            start_point = (row, col)
            temp = find_point_length_n_paths(n, board, [],
                                                len(board[row][col]), [start_point], True)
            if temp:
                result += temp
    return result


def max_score_words_dict(n, board, words):
    all_path = find_general_length_n_paths(n, board)
    all_good_path = dict()
    for path in all_path:
        word = is_valid_path(board, path, words)
        if word:
            all_good_path[word] = path
    return all_good_path

def max_score_paths(board, words):
    max_score_dict = {}
    max_word_length = len((max(words, key=len)))
    min_word_length = len((min(words, key=len)))
    for n in range(max_word_length, min_word_length - 1, -1):
        temp = max_score_words_dict(n, board, words)
        for word in temp:
            if word not in max_score_dict:
                max_score_dict[word] = temp[word]
            elif len(temp[word]) > len(max_score_dict[word]):
                max_score_dict[word] = temp[word]
    return list(max_score_dict.values())



# def max_score_paths(board, words):
#     max_score_dict = {}
#     max_word_length = len((max(words.keys(), key=len)))
#     min_word_length = len((min(words.keys(), key=len)))
#     for n in range(max_word_length, min_word_length - 1, -1):
#         temp = max_score_words_dict(n, board, words)
#         for word in temp:
#             if word not in max_score_dict:
#                 max_score_dict[word] = temp[word]
#             elif len(temp[word]) > len(max_score_dict[word]):
#                 max_score_dict[word] = temp[word]
#     return list(max_score_dict.values())


# if __name__ == '__main__':
#     # board = [['G', 'SE', 'I', 'R'],
#     #          ['JS', 'AL', 'S', 'E'],
#     #          ['EA', 'L', 'I', 'V'],
#     #          ['S', 'U', 'S', 'T']]
#     #
#     # from pprint import pprint
#     # pprint(board)
#     # words_dict = create_word_dict("boggle_dict.txt")
#     # print(find_length_n_paths(3, board, words_dict))
#     # print(_find_all_length_n_words_helper(4, board, words_dict, [], 1,
#     #                             [(0,0)], board[0][0]))
#     # paths = _find_all_length_n_paths_helper(4, board, words_dict, [], 1,
#     #                             [(0,0)])
#     # print(find_length_n_paths(4, board, words_dict))
#     # print(find_length_n_words(7, board, words_dict))
#     # print(find_length_n_paths(7, board, words_dict))
#     # print(max_score_paths(board, {"RISE": 0}))
#     print(max_score_paths(
#         [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'G', 'K', 'L'],
#          ['M', 'N', 'O', 'P']], ('ABC', 'CDE', 'ABCD')))

    #Todo - check what heppens when n is more than 8.

    # lst_of_words = []
    # for path in paths:
    #     word = ""
    #     for point in path:
    #         word += board[point[0]][point[1]]
    #     lst_of_words.append(word)
    # print(lst_of_words)
    # print(len(lst_of_words))
    #




