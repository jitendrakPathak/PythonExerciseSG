"""
Python Code to Summarise Market quote count using a text file.
"""
import sys

import datetime


class MarketQuoteSummary:
    """
    Read the text file.
    Filter based on date.
    Generate count summary.
    """

    def __init__(self, data_file, date_filter, delim=None):
        self.data_file = data_file
        self.date_filter = date_filter
        self.delim = delim if delim else ";"

    @staticmethod
    def _format_data(unformatted_data):
        """
        Formatting for printing purpose only
        :return:
        """
        formatted_data = ""
        for quote, ct in unformatted_data.items():
            temp_str = f"{quote}:{ct}\n"
            formatted_data += temp_str

        return formatted_data

    def parse_data(self):
        """

        :return:
        """
        return_data = dict()
        with open(self.data_file, mode="r") as opened_file:
            for line in opened_file:
                line_split = line.strip().split(self.delim)
                instrument = line_split[0].strip()
                instrument_date = line_split[1]

                if instrument_date > self.date_filter:  # Excluding the given date
                    if instrument not in return_data:
                        return_data[instrument] = 1
                    else:
                        return_data[instrument] += 1

        formatted_data = self._format_data(return_data)

        return formatted_data


if __name__ == "__main__":
    input_file = sys.argv[1]
    try:
        input_date = sys.argv[2]
    except IndexError:
        input_date = str(datetime.datetime.now())

    summary_data = MarketQuoteSummary(data_file=input_file, date_filter=input_date).parse_data()

    print(f"Number of quotes after {input_date}:\n\n\n", summary_data)
