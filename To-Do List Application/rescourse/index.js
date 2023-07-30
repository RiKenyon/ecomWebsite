// script.js
const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");
const taskList = document.getElementById("taskList");

addButton.addEventListener("click", addTask);
taskList.addEventListener("click", deleteTask);

function addTask(event) {
  event.preventDefault();
  const taskText = taskInput.value;
  if (taskText.trim() === "") return;

  const taskItem = document.createElement("li");
  taskItem.innerHTML = `
    <span>${taskText}</span>
    <span class="delete-button">X</span>
  `;
  taskList.appendChild(taskItem);
  taskInput.value = "";
}

function deleteTask(event) {
  if (event.target.classList.contains("delete-button")) {
    const taskItem = event.target.parentElement;
    taskItem.remove();
  }
}
