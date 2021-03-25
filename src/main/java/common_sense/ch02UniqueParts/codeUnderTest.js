function isEquivalent(a,b) {
    // arrays of property names
    var aProps = Object.getOwnPropertyNames(a);
    var bProps = Object.getOwnPropertyNames(b);

    // If their property lengths are different, they're different objects
    if (aProps.length != bProps.length){
        return false;
    }

    for (var i=0;i<aProps.length;i++){
        var propname = aProps[i];

        // If the values of the property are different, not equal
        if (a[propname]!=b[propname]){
            return false;
        }
    }

    // If everything matched, correct
    return true;
}

module.exports = { isEquivalent };
