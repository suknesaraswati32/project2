const express=require("express")
const app=express()
const path=require("path")
const methodOverride = require('method-override')
const { v4 : uuidv4 }=require("uuid")
let tasks = [
  {
    id: uuidv4(),
    title: "Complete DBMS Assignment",
    description: "Finish normalization and SQL queries",
    status: "pending",
    priority: "high",
    deadline: "2026-05-15",
    subject: "DBMS"
  },
  {
    id: uuidv4(),
    title: "Practice REST API",
    description: "Build CRUD APIs using Express",
    status: "completed",
    priority: "medium",
    deadline: "2026-05-12",
    subject: "Web Development"
  },
  {
    id: uuidv4(),
    title: "Learn Authentication",
    description: "Study JWT authentication",
    status: "pending",
    priority: "high",
    deadline: "2026-05-18",
    subject: "Backend"
  },
  {
    id: uuidv4(),
    title: "DSA Practice",
    description: "Solve 5 array problems",
    status: "pending",
    priority: "low",
    deadline: "2026-05-11",
    subject: "DSA"
  },
  {
    id: uuidv4(),
    title: "Mini Project UI",
    description: "Design frontend pages",
    status: "completed",
    priority: "medium",
    deadline: "2026-05-20",
    subject: "Frontend"
  },
  {
    id: uuidv4(),
    title: "MongoDB Practice",
    description: "Learn CRUD operations",
    status: "pending",
    priority: "high",
    deadline: "2026-05-17",
    subject: "Database"
  },

];
app.set("view engine","ejs");
app.use(express.static(path.join(__dirname, "public")));
app.set("views", path.join(__dirname, "views"));
app.use(express.urlencoded({extended:true}))
app.use(methodOverride("_method"))

app.get("/task",(req,res)=>{
  res.render("task.ejs",{tasks});
})
app.get("/task/new",(req,res)=>{
  res.render("new.ejs")
})
app.post("/task",(req,res)=>{
   const {title, description, status, priority, deadline, subject } = req.body;
   const id= uuidv4()
   tasks.push({ id,title, description, status, priority, deadline, subject })
   res.redirect("/task")
})
app.get("/task/:id/edit",(req,res)=>{
  let {id}=req.params
  let task=tasks.find(p=> p.id===id)
  res.render("edit.ejs",{task})
})

app.put("/task/:id",(req,res)=>{

  let {id}=req.params;

  let task = tasks.find(p => p.id === id);

  const {title,description,status,priority,deadline,subject} = req.body;

  task.title = title;
  task.description = description;
  task.status = status;
  task.priority = priority;
  task.deadline = deadline;
  task.subject = subject;

  res.redirect("/task");
})

app.delete("/task/:id",(req,res)=>{
let {id}=req.params
  tasks = tasks.filter(p => p.id !== id);
  res.redirect("/task")
})
app.listen(8080,(req,res)=>{
  console.log("server is running on port 8080")
})