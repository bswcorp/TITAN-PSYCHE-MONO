// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title QSTATE Sovereign Core
 * @dev Digital Currency backed by ASSET-ARK Credit
 */
contract QSTATE {
    string public name = "Quorum State";
    string public symbol = "QSTATE";
    uint8 public decimals = 18; 
    uint256 public totalSupply = 141000000 * 10**18; // 141 Juta QSTATE (Mastering Frequency)

    mapping(address => uint256) public balanceOf;
    address public architect;
    
    constructor() {
        architect = msg.sender;
        balanceOf[architect] = totalSupply;
    }
}
