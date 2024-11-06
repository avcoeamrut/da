// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract SimpleBank{
    address public owner;
    uint256 public balance;
    event Deposit(address indexed from,uint256 amount);
    event Withdraw(address indexed to,uint256 amount);
    constructor() {
        owner=msg.sender;
        balance=0;
    }
    function deposit(uint256 amount) public {
        require(msg.sender == owner,"only the owner can deposite money");
        balance += amount;
        emit Deposit(msg.sender, amount);
    }
    function withdraw(uint256 amount) public {
        require(msg.sender == owner,"only the owner can deposite money");
        require(amount <= balance,"insufficient balance");
        balance -= amount;
        emit Withdraw(msg.sender,amount);
    }
    function getBalance() public view returns (uint256){
        return balance;
    }


}
