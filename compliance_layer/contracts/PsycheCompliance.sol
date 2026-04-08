// SPDX-License-Identifier: Sovereign-1.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";

contract PsycheCompliance is Ownable {
    mapping(address => bool) public isVerified;
    
    // Status data riset NASA sebagai syarat aktivasi jaminan
    bool public nasaDataValidated;

    constructor() Ownable(msg.sender) {}

    function verifyIdentity(address _user) external onlyOwner {
        isVerified[_user] = true;
    }

    function setNasaValidation(bool _status) external onlyOwner {
        nasaDataValidated = _status;
    }

    function canTransfer(address _from, address _to) external view returns (bool) {
        // Hanya bisa transfer jika kedua pihak terverifikasi (KYC Negara)
        // dan Data Riset NASA telah divalidasi sebagai jaminan
        return isVerified[_from] && isVerified[_to] && nasaDataValidated;
    }
}
