import logging


def day_1():
    logging.info("day 1: started")
    data = open("data")
    total = 0
    totals = []
    for line in data:
        logging.debug("line: " + line)
        if line != "\n":
            total = total + int(line)

        elif line == "\n":
            logging.debug("end of the line")
            logging.debug("current total: " + str(total))
            totals.append(total)   # add this total to a dictionary or list of totals
            total = 0

    logging.info(totals)
    logging.info("the fattest reindeer is carrying " + str(max(totals)) + " calories")

    top3_total = 0
    for i in range(3):
        current = max(totals)
        top3_total = top3_total + current
        logging.debug(current)
        totals.remove(current)

    logging.info("top3_total: " + str(top3_total))
    logging.info("day 2: ended!")


logging.basicConfig(handlers=[logging.StreamHandler()],
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')  # initialize logger to log to file, and console!


if __name__ == "__main__":
    day_1()
