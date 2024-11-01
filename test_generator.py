# test_generator.py
import ast
import inspect
import main  # main.pyをインポート


def generate_tests_from_module(module):
    functions = [
        f for f in dir(module) if callable(getattr(module, f)) and not f.startswith("_")
    ]
    test_cases = []

    for func in functions:
        func_obj = getattr(module, func)
        params = inspect.signature(func_obj).parameters

        test_case = f"    def test_{func}(self):\n"
        param_values = ", ".join(
            [f"0" for _ in params]
        )  # ここでは単純に0を渡しています
        test_case += (
            f"        self.assertEqual({func}({param_values}), ...)  # 期待値を設定"
        )
        test_cases.append(test_case)

    return "\n".join(test_cases)


# テストケースを生成して表示
if __name__ == "__main__":
    generated_tests = generate_tests_from_module(main)
    print(
        "import unittest\n\nclass TestMain(unittest.TestCase):\n"
        + generated_tests
        + "\n\nif __name__ == '__main__':\n    unittest.main()"
    )
