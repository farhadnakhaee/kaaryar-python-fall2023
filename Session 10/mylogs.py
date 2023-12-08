# DEBUG   Detailed information, typically of interest only when diagnosing problems.
# INFO  Confirmation that things are working as expected.
# WARNING  An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR   Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL   A serious error, indicating that the program itself may be unable to continue running.

# https://betterstack.com/community/guides/logging/how-to-start-logging-with-python/


import logging

# logging.basicConfig(level=logging.DEBUG)
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.DEBUG,format=FORMAT, filename="logs.txt")
logger = logging.getLogger(__name__)
logger2 = logging.getLogger("file_logs")


def some_function():
    logger.info("Executing some function...")

    # a loop with if-else statements
    for i in range(5):
        if i % 2 == 0:
            logger.debug(f"Step {i}: Performing even iteration.")
        else:
            logger.debug(f"Step {i}: Performing odd iteration.")

    # a conditional statement
    user_input = input("Enter 'yes' or 'no': ")
    if user_input.lower() == 'yes':
        logger.info("User entered 'yes', proceeding with the next steps.")
    elif user_input.lower() == 'no':
        logger.info("User entered 'no', skipping some steps.")
    else:
        logger.error("Invalid input. Defaulting to the next steps.")

    logger.info("Print statement at the end.")

if __name__ == "__main__":
    logger.info("Starting the program...")
    some_function()
    logger.info("Program finished.")
