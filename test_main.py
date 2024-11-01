# test_generator.py
import ast
import inspect
import unittest
import main  # main.pyをインポート


class TestMain(unittest.TestCase):
    @classmethod  # クラスメソッドとして定義
    def generate_tests_from_module(cls, module):
        functions = [
            f
            for f in dir(module)
            if callable(getattr(module, f)) and not f.startswith("_")
        ]

        for func in functions:
            func_obj = getattr(module, func)
            params = inspect.signature(func_obj).parameters

            # テストメソッドを動的に生成
            def test_func(self, func=func, param_values=[0] * len(params)):
                self.assertEqual(func(param_values), ...)  # 期待値を設定

            # メソッド名を設定
            test_func.__name__ = f"test_{func}"
            setattr(cls, test_func.__name__, test_func)

        # 生成されたテストケースを表示
        print(
            "Generated test methods:", [f"test_{f}" for f in functions]
        )  # ここで生成されたテストケースを確認


if __name__ == "__main__":
    TestMain.generate_tests_from_module(main)
    unittest.main()
