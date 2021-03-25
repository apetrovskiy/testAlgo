const codeUnderTest = require('../../../main/java/common_sense/ch02UniqueParts/codeUnderTest');

test('Equality case',()=>{
    result = codeUnderTest.isEquivalent({'hi':12},{'hi':12});
    expect(result).toEqual(true);
})

test('Inequality case',()=>{
    result = codeUnderTest.isEquivalent({'hi':12},{'hi':14});
    expect(result).toEqual(false);
})
