// SPDX-License-Identifier: STG-SOVEREIGN-GALAXY-1.0
// 🏛️ STG GOVERNMENT GALAXY LICENSE v1.0
// ARCHITECT: ANDI MUHAMMAD HARPIANTO

pragma solidity ^0.8.20;

contract TitanPsycheMono {
    string public constant name = "TITAN PSYCHE MONO";
    string public constant symbol = "TPM";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 17845000000 * 10**18;
    string public constant valuation = "114 Absolute Infinite";
    string public constant backing = "16 Psyche Metallic Equity ($10 Quintillion)";

    mapping(address => uint256) public balanceOf;
    address public immutable architect;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() {
        architect = msg.sender;
        balanceOf[msg.sender] = totalSupply;
    }

    function secureTransfer(address _to, uint256 _value) public returns (bool) {
        require(msg.sender == architect, "JANGAN AJARI IKAN BERENANG!");
        require(balanceOf[msg.sender] >= _value, "SALDO TIPIS!");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }
}
