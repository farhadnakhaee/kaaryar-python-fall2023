class SampleClass:
    def __init__(self, name:str,*args, **kwargs) -> None:
        self.name = name
        self.args=args
        [
            setattr(self, key, value)
            for key, value in 
            kwargs.items()
        ]

    def __repr__(self) -> str:
        return f"""
                { {key:getattr(self,key) for key in dir(self) if not key.startswith("_")} }
                """


if __name__=="__main__":

    my_class = SampleClass("First","Hello",25, payment=100, deposit=50.0, last_name="Roshandel")

    print(my_class)

    my_dict = {
        (1, "Hossein"):15,
        "name":"Tehran",
        (9, "Farhad"):lambda x: x*x
    }
    my_dict["vjgjh"]="test"

    print(my_dict)

    my_set = {
        "Hossein",
        "Farhad"
    }
    my_set.add("Hossein")
    print(my_set)
