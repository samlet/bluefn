pragma solidity^0.6.0;

contract Foo {

    string public bar;
    event barred(string _bar);

    constructor() public {
        bar = "hello world";
    }

    function setBar(string memory _bar) public {
        bar = _bar;
        emit barred(_bar);
    }
}
