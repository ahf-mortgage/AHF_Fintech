

    let input_fieldKeyPressed = true;
    const btn_save = document.getElementById("btn-save")
    const loan_break_point = document.getElementById("loan_break_point")
    const max_gci = document.getElementById("max_gci")
    const inputs_fields = document.querySelectorAll("input");
    //querySelectorAll(".inputs_fields"); // Select elements

    if (max_gci || loan_break_point) {
        input_fieldKeyPressed = true

    }
        if (input_fieldKeyPressed) {


        inputs_fields.forEach(element => {
            element.addEventListener("keydown", function () {
                btn_save.classList.remove("disabled")
                btn_save.classList.remove("bg-gray-500")
                btn_save.classList.add("bg-blue-500")
                btn_save.classList.add("text-white")

            });
        });

    }

