include('inc/testing.js')

test.name = "boolean operations test"

f = false
t = true

assert.areEqual(f, false, 'f should equal false')
assert.areEqual(t, true , 't should equal true')

assert.areEqual(f == false, true , 'f equals false should be true')
assert.areEqual(f == true , false, 'f equals true should be false')

assert.areEqual(t == false, false, 't equals false should be false')
assert.areEqual(t == true , true , 't equals true should be true')

// do some more stuff here with relative comparisons etc
