import express from "express";
const router = express.Router();

let employees = [];

router.post("/", (req, res) => {
  const employee = req.body;
  employee.id = employees.length + 1;
  employees.push(employee);
  res.json({ message: "Employee added", employee });
});

router.get("/", (req, res) => res.json(employees));

router.put("/:id", (req, res) => {
  const id = parseInt(req.params.id);
  employees[id - 1] = { ...employees[id - 1], ...req.body };
  res.json({ message: "Employee updated", employee: employees[id - 1] });
});

router.delete("/:id", (req, res) => {
  const id = parseInt(req.params.id);
  employees = employees.filter(e => e.id !== id);
  res.json({ message: "Employee removed" });
});

export default router;
