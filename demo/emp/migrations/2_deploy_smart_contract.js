var EmpAttendance = artifacts.require("EmpAttendance");

module.exports = function(deployer) {
  deployer.deploy(EmpAttendance);
};