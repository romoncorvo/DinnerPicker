const addStepsDiv = document.querySelector("#addSteps");
const addIngredientsDiv = document.querySelector("#addIngredients");

const addLineStepsBtn = document.querySelector("#addLineSteps");
const addLineIngredientsBtn = document.querySelector("#addLineIngredients");

const removeLineStepsBtn = document.querySelector("#removeLineSteps");
const removeLineIngredientsBtn = document.querySelector(
  "#removeLineIngredients"
);

let stepNum = 4;
let ingredientsNum = 4;

addLineStepsBtn.addEventListener("click", () => {
  stepNum++;

  const newDiv = document.createElement("div");
  newDiv.setAttribute("class", "form-floating");

  const newText = document.createElement("textarea");
  newText.setAttribute("class", "form-control mb-1");
  newText.setAttribute("placeholder", `Step ${stepNum}`);
  newText.setAttribute("id", `step${stepNum}`);
  newText.setAttribute("name", `step${stepNum}`);

  const newLabel = document.createElement("label");
  newLabel.setAttribute("for", "floatingTextarea");

  const newB = document.createElement("b");
  newB.textContent = `${stepNum}.`;

  newDiv.appendChild(newText);
  newLabel.appendChild(newB);
  newDiv.appendChild(newLabel);
  addStepsDiv.appendChild(newDiv);
});

addLineIngredientsBtn.addEventListener("click", () => {
  ingredientsNum++;

  const newDiv = document.createElement("div");
  newDiv.setAttribute("class", "input-group mb-1");

  const newInput = document.createElement("input");
  newInput.setAttribute("id", `ingredient${ingredientsNum}`);
  newInput.setAttribute("name", `ingredient${ingredientsNum}`);
  newInput.setAttribute("type", "text");
  newInput.setAttribute("class", "form-control");
  newInput.setAttribute("aria-label", "Ingredients");
  newInput.setAttribute("aria-describedby", "basic-addon1");

  newDiv.appendChild(newInput);
  addIngredientsDiv.appendChild(newDiv);
});

removeLineStepsBtn.addEventListener("click", () => {
  addStepsDiv.lastElementChild.remove();
  if (stepNum > 0) {
    stepNum--;
  }
});

removeLineIngredientsBtn.addEventListener("click", () => {
  addIngredientsDiv.lastElementChild.remove();
  if (ingredientsNum > 0) {
    ingredientsNum--;
  }
});
