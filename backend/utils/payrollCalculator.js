export function calculatePayroll(basic, allowances = 0, deductions = 0) {
  const gross = basic + allowances;
  const paye = gross * 0.05;     // Sample PAYE % for now
  const nhif = 500;
  const nssf = 200;
  const net = gross - (paye + nhif + nssf + deductions);
  return { gross, paye, nhif, nssf, net };
}
