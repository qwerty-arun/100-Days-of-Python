# Local and Non-local

chai_type = "Ginger"
def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type # use global to change the global chai_type
        print("Before Update: ", chai_type)
        chai_type = "Kesar"

    kitchen()
    print("After kitchen update: ", chai_type)

update_order()