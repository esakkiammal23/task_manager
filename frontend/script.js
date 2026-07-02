console.log("Script Loaded");
const API_URL =
"https://task-manager-checklist.onrender.com/api";
loadTasks();

async function loadTasks(){
    const response = await fetch(`${API_URL}/tasks/`)
    const tasks =await response.json();
    let html = ""; tasks.forEach(task => {

        html += `
        <li>

            <span>${task.title} - ${task.task_status ? "Completed" : "Pending"}
            </span>
            <div>
           <button onclick="updateTask(${task.id})"
              ${task.task_status ? "disabled" : ""}>
              ${task.task_status ? "Completed" : "Mark Complete"} </button>

            <button onclick="deleteTask(${task.id})">
                Delete</button>
            </div>
        </li>
        `;
    });

    document.getElementById("taskList").innerHTML = html;
}

async function addTask(){

    const title =document.getElementById( "taskInput" ).value;

    await fetch(`${API_URL}/tasks/add`,
        {
            method:"POST",

            headers:{"Content-Type":"application/json"
            },
            body:JSON.stringify({ title:title})
        }
    );

    document.getElementById("taskInput").value="";
    loadTasks();
}

async function updateTask(id){

    await fetch(`${API_URL}/tasks/update/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({task_status: true})
    });

    loadTasks();
}

async function deleteTask(id){

    await fetch( `${API_URL}/tasks/delete/${id}`,
        {
            method:"DELETE"
        }
    );

    loadTasks();
}