const selectElement = document.getElementById("select-floor");
    const option1Content = document.getElementById("ground-floor");
    const option2Content = document.getElementById("first-floor");
    const option3Content = document.getElementById("second-floor");
    const option4Content = document.getElementById("third-floor");
    const option5Content = document.getElementById("fourth-floor");
    const option6Content = document.getElementById("fifth-floor");

    selectElement.addEventListener("change", function() {
      switch (this.value) {
        case "option-floor_ground":
          option1Content.style.display = "flex";
          option2Content.style.display = "none";
          option3Content.style.display = "none";
          option4Content.style.display = "none";
          option5Content.style.display = "none";
          option6Content.style.display = "none";
          break;
        case "option-floor_1":
          option1Content.style.display = "none";
          option2Content.style.display = "flex";
          option3Content.style.display = "none";
          option4Content.style.display = "none";
          option5Content.style.display = "none";
          option6Content.style.display = "none";
          break;
        case "option-floor_2":
          option1Content.style.display = "none";
          option2Content.style.display = "none";
          option3Content.style.display = "flex";
          option4Content.style.display = "none";
          option5Content.style.display = "none";
          option6Content.style.display = "none";
          break;
        case "option-floor_3":
          option1Content.style.display = "none";
          option2Content.style.display = "none";
          option3Content.style.display = "none";
          option4Content.style.display = "flex";
          option5Content.style.display = "none";
          option6Content.style.display = "none";
          break;
        case "option-floor_4":
          option1Content.style.display = "none";
          option2Content.style.display = "none";
          option3Content.style.display = "none";
          option4Content.style.display = "none";
          option5Content.style.display = "flex";
          option6Content.style.display = "none";
          break;
        case "option-floor_5":
          option1Content.style.display = "none";
          option2Content.style.display = "none";
          option3Content.style.display = "none";
          option4Content.style.display = "none";
          option5Content.style.display = "none";
          option6Content.style.display = "flex";
          break;
        default:
          option1Content.style.display = "none";
          option2Content.style.display = "none";
          option3Content.style.display = "none";
          option4Content.style.display = "none";
          option5Content.style.display = "none";
          option6Content.style.display = "none";
      }
    });