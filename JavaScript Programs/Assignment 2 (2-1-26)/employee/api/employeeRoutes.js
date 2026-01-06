const express = require('express');
const router = express.Router();
const controller = require('./employeeController');

router.get('/employees', controller.getAllEmployees);
router.get('/employees/:id', controller.getEmployee);
router.post('/employees', controller.createEmployee);
router.put('/employees/:id', controller.updateEmployee);
router.delete('/employees/:id', controller.deleteEmployee);

module.exports = router;
