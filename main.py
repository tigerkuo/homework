from math_op import basic_op, advanced_op

def main():
    while True:
        print("\n選擇運算類型:")
        print("1. 加法")
        print("2. 減法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 平均值")
        print("6. 冪次")
        print("7. 平方根")
        print("8. 對數")
        print("9. 結束")
        
        choice = input("請輸入選項 (1-9): ")
        
        if choice == '9':
            print("程式結束！")
            break
        
        try:
            if choice in ['1', '2', '3', '4']:
                a = float(input("輸入第一個數: "))
                b = float(input("輸入第二個數: "))
                if choice == '1':
                    print("結果:", basic_op.add(a, b))
                elif choice == '2':
                    print("結果:", basic_op.substract(a, b))
                elif choice == '3':
                    print("結果:", basic_op.multiply(a, b))
                elif choice == '4':
                    print("結果:", basic_op.divide(a, b))
            elif choice == '5':
                nums = list(map(float, input("輸入數字 (以空格分開): ").split()))
                print("結果:", advanced_op.average(nums))
            elif choice == '6':
                base = float(input("輸入底數: "))
                exponent = float(input("輸入指數: "))
                print("結果:", advanced_op.power(base, exponent))
            elif choice == '7':
                num = float(input("輸入數字: "))
                print("結果:", advanced_op.sqrt(num))
            elif choice == '8':
                num = float(input("輸入數字: "))
                base = float(input("輸入底數 (預設為10，直接按Enter可跳過): ") or 10)
                print("結果:", advanced_op.log(num, base))
            else:
                print("無效選擇，請重新輸入。")
        except Exception as e:
            print("錯誤:", e)

if __name__ == "__main__":
    main()
