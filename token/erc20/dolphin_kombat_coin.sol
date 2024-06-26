pragma solidity ^0.8.0;

contract ERC20_Dolphin_Coin is ERC20, ERC20Burnable {
    construct() ERC20("ERC20 Dolphin kombat coin", "Dolkom") {
        _mint(msg.sender, 100_000_000_000 * 10**18 );
    }
}
