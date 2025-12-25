import express from "express";
import { calculatePayroll } from "../utils/payrollCalculator.js";
const router = express.Router();

router.post("/", (req, res) => {
  const { basic, allowances, deductions } = req.body;
  const result = calculatePayroll(basic, allowances, deductions);
  res.json({ message: "Payroll calculated", result });
});

export default router;
