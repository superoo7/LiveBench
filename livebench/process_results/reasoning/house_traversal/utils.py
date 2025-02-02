
import re


def house_traversal_process_results(ground_truth: str, llm_answer: str) -> int:

    # pull out words in bold
    bold_words = re.findall(r'(\*{2,})(.*?)\1', llm_answer.lower())
    if not len(bold_words):
        return 0

    last_bold = bold_words[-1][1]
    ground_truth_names = ground_truth.lower().split(" ")

    # check if all the ground truth names are in the last bolded part
    if all([name in last_bold for name in ground_truth_names]):
        return 1

    # check if all the ground truth names are in the last few bolded words, in order
    if len(bold_words) >= len(ground_truth_names):
        if all([name in last_bold[-1 - i] for i,name in enumerate(ground_truth_names[::-1])]):
            return 1

    return 0
