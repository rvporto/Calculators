class MyClass:

    def registry(self) -> None:
        print("Start registry")
        self.__verify()
        self.__verify_registry()
        self.__insert_data()

    def __verify(self) -> None:
        print("Verify Data")

    def __verify_registry(self) -> None:
        print("Verify Registry")

    def __insert_data(self) -> None:
        print("Insert DB")
        
obj = MyClass()
obj.registry()


        