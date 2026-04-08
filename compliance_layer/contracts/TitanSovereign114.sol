// SPDX-License-Identifier: Sovereign-1.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./PsycheCompliance.sol";

contract TitanSovereign114 is ERC20 {
    PsycheCompliance public compliance;
    uint256 public constant TOTAL_GENESIS = 114;

    constructor(address _complianceAddress) ERC20("TITAN PSYCHE SOVEREIGN", "114-TPS") {
        compliance = PsycheCompliance(_complianceAddress);
        // Minting 114 unit ke alamat deployer (Kedaulatan Negara)
        _mint(msg.sender, TOTAL_GENESIS * 10**decimals());
    }

    // Override fungsi transfer untuk mengecek aturan legal
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(compliance.canTransfer(msg.sender, to), "Gagal: Pelanggaran Kepatuhan/Data Riset Belum Valid");
        return super.transfer(to, amount);
    }
}
