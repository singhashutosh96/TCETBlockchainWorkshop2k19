pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Owned {
    
    address owner;
    
    constructor() public {
        owner = msg.sender;
    }
    
    modifier onlyOwner {
        require (msg.sender == owner);
        _;
    }
}

contract EmpAttendance is Owned {
    
    struct employee {
        string empName;
        string empDepartment;
        string [] empAttendance;
    }
    
    mapping (address => employee) db_empAttendanceRecord;
    address [] db_empAccounts;
    
    function signUp(string memory _empName , string memory _empDeparment) public {
        
        employee memory newEmployee = employee(_empName,_empDeparment,new string[](0));
     
        db_empAttendanceRecord[msg.sender] = newEmployee;
        db_empAccounts.push(msg.sender);
    }
    
    function markAttendance(string memory _date) public {
        db_empAttendanceRecord[msg.sender].empAttendance.push(_date);
    }
    
    function viewAttendance() public returns (string [] memory) {
        return db_empAttendanceRecord[msg.sender].empAttendance;
    }
    
    function viewEmpAttendance(address _empaddress) onlyOwner public returns (string [] memory)
    {
        return db_empAttendanceRecord[_empaddress].empAttendance;
    }
    
    function viewEmpName(address _empaddress) onlyOwner public returns (string memory)
    {
        return db_empAttendanceRecord[_empaddress].empName;
    }
    
    function viewEmpAccounts() onlyOwner public returns (address [] memory)
    {
        return db_empAccounts;
    }
}
