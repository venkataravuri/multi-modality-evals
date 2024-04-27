from multi_modality_evals.logging_config import logger
import argparse
import sys
from eval import eval

def create_parser():
    parser = argparse.ArgumentParser(description='An multi-modality ML model evaluation & benchmarking engine.')

    parser.add_argument(
        "-m",
        "--model",
        type=str,
        choices=['phi'],
        default=None,
        help="Specify ML model name. e.g., phi"
    )
    
    parser.add_argument(
        "-t",
        "--tasks",
        type=str,
        choices=['phi'],
        default=None,
        metavar="task1,task2",
        help="List of tasks to be executed.")

    args = parser.parse_args()

    return args

def evaluate(args):

    if args.tasks is None:
        logger.error("Tasks are not specified.")
        sys.exit()

    task_list = args.tasks.split(",")


def main():
    args = create_parser()
    logger.info(f"Arguments: {args}")

if __name__ == '__main__':
    main()