import unittest


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super(CustomTestResult, self).__init__(stream, descriptions, verbosity)

    def startTest(self, test):
        super(CustomTestResult, self).startTest(test)

    def addSuccess(self, test):
        super(CustomTestResult, self).addSuccess(test)
        self.print_result(test, "PASS")

    def addFailure(self, test, err):
        super(CustomTestResult, self).addFailure(test, err)
        self.print_result(test, "FAIL")

    def addSkip(self, test, reason):
        super(CustomTestResult, self).addSkip(test, reason)
        self.print_result(test, "SKIP")

    def addError(self, test, err):
        super(CustomTestResult, self).addError(test, err)
        self.print_result(test, "ERROR")

    def print_result(self, test, result):
        test_id = test.id()
        result_id = test_id.replace("__main__.", "")
        name_summary = test.shortDescription() or str(test)
        output = f'"{name_summary}", "{result}", "{result_id}"'

        import os

        file_name = "test_results.txt"
        current_path = os.path.dirname(os.path.realpath(__file__))
        file_path = current_path + "/" + file_name

        with open(file_path, "a") as file:
            file.write(output + "\n")


class CustomTestRunner(unittest.TextTestRunner):
    """
    A basic test runner implementation which prints results
    """

    def __init__(self, stream=None, descriptions=None, verbosity=1):
        super(CustomTestRunner, self).__init__(stream, descriptions, verbosity)

    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        result = super(CustomTestRunner, self).run(test)
        return result


if __name__ == "__main__":
    pass
