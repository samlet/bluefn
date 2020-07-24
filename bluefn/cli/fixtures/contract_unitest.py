test_js_template='''// test/${name}.test.js

// Load dependencies
const { accounts, contract } = require('@openzeppelin/test-environment');
const { expect } = require('chai');

// Load compiled artifacts
const ${name} = contract.fromArtifact('${name}');

// Start test block
describe('${name}', function () {
    const [ owner ] = accounts;

    beforeEach(async function () {
        // Deploy a new ${name} contract for each test
        this.contract = await ${name}.new({ from: owner });
    });

    // Test case
    it('retrieve .. stored', async function () {        
        // await this.contract.store(42, { from: owner });
        // console.log('... result is '+(await this.contract.retrieve()).toString());
        // expect((await this.contract.retrieve()).toString()).to.equal('42');
    });
});'''

