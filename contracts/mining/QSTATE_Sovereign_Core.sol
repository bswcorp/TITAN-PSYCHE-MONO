// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title QSTATE Sovereign Core
 * @dev Asset-Backed by 16 Psyche Metal Reserves (STG-HKI-2026)
 * Architect: Andi Muhammad Harpianto
 * Unit: 1 QSTATE = 10^18 AKSA
 */

contract QSTATE {
    string public name = "Quorum State";
    string public symbol = "QSTATE";
    uint8 public decimals = 18; 
    uint256 public totalSupply = 114000000 * 10**18; // 114 JUTA (ANGKA KERAMAT)

    mapping(address => uint256) public balanceOf;
    
    // SKEMA VETO ARCHITECT (ANTI-DUMP)
    address public architect;
    
    constructor() {
        architect = msg.sender;
        balanceOf[architect] = totalSupply;
    }
}
