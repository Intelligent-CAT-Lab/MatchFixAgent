
/// SKEL HEAD BEGIN
function user_check_type(obj, _type) {
    if (typeof obj === 'object' && !Array.isArray(obj) && obj !== null && obj.hasOwnProperty("_class_name")) {
        if (String(_type).includes('function')) {
            for (let i of obj["_class_name"].split(";")) {
                if (i === String(_type).split(" ")[1].split("(")[0]) {
                    return true;
                }
            }
            return false;
        } else if (typeof _type === 'string') {
            for (let i of obj["_class_name"].split(";")) {
                if (i === _type) {
                    return true;
                }
            }
            return false;
        }
        else{
            return false;
        }
    } else {
        if (typeof _type === 'symbol') {
            if (_type.description === 'str' || _type.description === 'string') {
                return typeof obj === 'string';
            }
            if (_type.description === 'list' || _type.description === 'array') {
                return Array.isArray(obj);
            }
            if (_type.description === 'dict') {
                return obj.constructor === Object;
            }
            if (_type.description === 'int' || _type.description === 'number') {
                return Number.isSafeInteger(obj)  && obj !== 1e6;;
            }
            if (_type.description === 'float') {
                return typeof obj === 'number';
            }
            if (_type.description === 'bool' || _type.description === 'boolean') {
                return typeof obj === 'boolean';
            }
            if (_type.description === 'datetime') {
                return obj instanceof Date;
            }
            if (_type.description === 'time') {
                return obj instanceof Date && obj.getFullYear() === 1970 && obj.getMonth() === 0 && obj.getDate() === 1;
            }
            if (_type.description === 'date') {
                return obj instanceof Date && obj.getHours() === 0 && obj.getMinutes() === 0 && obj.getSeconds() === 0;
            }
            return false;
        }

        if (typeof _type === 'string') {
            if (_type === 'str' || _type === 'string') {
                return typeof obj === 'string';
            }
            if (_type === 'list' || _type === 'array') {
                return Array.isArray(obj);
            }
            if (_type === 'dict') {
                return obj.constructor === Object;
            }
            if (_type === 'int' || _type === 'number') {
                return Number.isSafeInteger(obj) && obj !== 1e6;
            }
            if (_type === 'float') {
                return typeof obj === 'number';
            }
            if (_type === 'bool' || _type === 'boolean') {
                return typeof obj === 'boolean';
            }
            if (_type === 'datetime') {
                return obj instanceof Date;
            }
            if (_type === 'time') {
                return obj instanceof Date && obj.getFullYear() === 1970 && obj.getMonth() === 0 && obj.getDate() === 1;
            }
            if (_type === 'date') {
                return obj instanceof Date && obj.getHours() === 0 && obj.getMinutes() === 0 && obj.getSeconds() === 0;
            }
            return false;
        }
        else return obj instanceof _type;
    }
}


function SkelClass(name) {
    let _class_var = {};
    _class_var._class_name = name;
    return _class_var;
}

/// SKEL HEAD END

function rgb_to_yiq(r, g, b){
    /// --- BLOCK BEGIN 1
var y = 0.30*r + 0.59*g + 0.11*b;
    var i = 0.74*(r-y) - 0.27*(b-y);
    var q = 0.48*(r-y) + 0.41*(b-y);
    return [y, i, q];
    /// --- BLOCK END 1

}

function yiq_to_rgb(y, i, q){
    /// --- BLOCK BEGIN 2
var r = y + 0.9468822170900693 * i + 0.6235565819861433 * q;
    var g = y - 0.27478764629897834 * i - 0.6356910791873801 * q;
    var b = y - 1.1085450346420322 * i + 1.7090069284064666 * q;
    if (r < 0.0) {
        r = 0.0;
    }
    if (g < 0.0) {
        g = 0.0;
    }
    if (b < 0.0) {
        b = 0.0;
    }
    if (r > 1.0) {
        r = 1.0;
    }
    if (g > 1.0) {
        g = 1.0;
    }
    if (b > 1.0) {
        b = 1.0;
    }
    return [r, g, b];

    /// --- BLOCK END 2

}

function rgb_to_hls(r, g, b){
    /// --- BLOCK BEGIN 3
var maxc = Math.max(r, g, b);
    var minc = Math.min(r, g, b);
    var sumc = (maxc + minc);
    var rangec = (maxc - minc);
    var l = sumc / 2.0;
    if (minc == maxc) {
        return [0.0, l, 0.0];
    }
    var s;
    if (l <= 0.5) {
        s = rangec / sumc;
    } else {
        s = rangec / (2.0 - sumc);
    }
    var rc = (maxc - r) / rangec;
    var gc = (maxc - g) / rangec;
    var bc = (maxc - b) / rangec;
    var h;
    if (r == maxc) {
        h = bc - gc;
    } else if (g == maxc) {
        h = 2.0 + rc - bc;
    } else {
        h = 4.0 + gc - rc;
    }
    h = (h / 6.0) % 1.0;
    if (h < 0) {
        h += 1.0;
    }
    return [h, l, s];
    /// --- BLOCK END 3

}

function hls_to_rgb(h, l, s){
    /// --- BLOCK BEGIN 4
    if (s === 0.0) {
        return [l, l, l];
    }
    var m2;
    if (l <= 0.5) {
        m2 = l * (1.0 + s);
    } else {
        m2 = l + s - (l * s);
    }
    var m1 = 2.0 * l - m2;
    var tmp_1 = _v(m1, m2, h + ONE_THIRD);
    var tmp_2 = _v(m1, m2, h);
    var tmp_3 = _v(m1, m2, h - ONE_THIRD);
    return [tmp_1, tmp_2, tmp_3];
    /// --- BLOCK END 4

}

function _v(m1, m2, hue){
    /// --- BLOCK BEGIN 5
    hue = hue % 1.0;
    if (hue < 0) hue += 1.0;
    if (hue < ONE_SIXTH) {
        return m1 + (m2 - m1) * hue * 6.0;
    }
    if (hue < 0.5) {
        return m2;
    }
    if (hue < TWO_THIRD) {
        return m1 + (m2 - m1) * (TWO_THIRD - hue) * 6.0;
    }
    return m1;

    /// --- BLOCK END 5

}

function rgb_to_hsv(r, g, b){
    /// --- BLOCK BEGIN 6
var maxc = Math.max(r, g, b);
    var minc = Math.min(r, g, b);
    var rangec = maxc - minc;
    var v = maxc;
    if (minc == maxc) {
        return [0.0, 0.0, v];
    }
    var s = rangec / maxc;
    var rc = (maxc - r) / rangec;
    var gc = (maxc - g) / rangec;
    var bc = (maxc - b) / rangec;
    var h;
    if (r == maxc) {
        h = bc - gc;
    } else if (g == maxc) {
        h = 2.0 + rc - bc;
    } else {
        h = 4.0 + gc - rc;
    }
    h = (h / 6.0) % 1.0;
    if (h < 0) {
        h += 1.0;
    }
    return [h, s, v];

    /// --- BLOCK END 6

}

function hsv_to_rgb(h, s, v){
    /// --- BLOCK BEGIN 7
if (s === 0.0) {
        return [v, v, v];
    }
    var i = parseInt(h * 6.0);
    var f = (h * 6.0) - i;
    var p = v * (1.0 - s);
    var q = v * (1.0 - s * f);
    var t = v * (1.0 - s * (1.0 - f));
    i = i % 6;
    if (i === 0) {
        return [v, t, p];
    }
    if (i === 1) {
        return [q, v, p];
    }
    if (i === 2) {
        return [p, v, t];
    }
    if (i === 3) {
        return [p, q, v];
    }
    if (i === 4) {
        return [t, p, v];
    }
    if (i === 5) {
        return [v, p, q];
    }
    // Cannot get here
    /// --- BLOCK END 7

}

function user_assert_almost_equal(a, b){
    /// --- BLOCK BEGIN 8
if (!(Math.abs(a - b) <= 0.0001)) {
    throw new Error('Assertion failed');
}
return true;
    /// --- BLOCK END 8

}

function assert_iter_almost_equal(iter1, iter2){
    /// --- BLOCK BEGIN 9
    for (var index = 0; index < iter1.length && index < iter2.length; index++) {
        var a = iter1[index];
        var b = iter2[index];
        user_assert_almost_equal(a, b);
    }
    return true;

    /// --- BLOCK END 9

}

function test_assertions(){
    /// --- BLOCK BEGIN 10
    console.log("--- rgb_to_yiq ---");
    var tmp = rgb_to_yiq(0.5, 0.5, 0.5);
    var _const_var = [0.49999999999999994, 2.6090241078691177e-17, 4.940492459581946e-17];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_yiq(0, 0.5, 1);
    var _const_var = [0.40499999999999997, -0.46035, 0.04954999999999998];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_yiq(1, 0, 0);
    var _const_var = [0.3, 0.599, 0.21299999999999997];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_yiq(0, 0, 0);
    var _const_var = [0.0, 0.0, 0.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_yiq(1, 0.1, 0.3);
    var _const_var = [0.392, 0.47476, 0.25411999999999996];
    assert_iter_almost_equal(tmp, _const_var);
    console.log("--- yiq_to_rgb ---");
    tmp = yiq_to_rgb(1.0, 0.5957, 0.0);
    var _const_var = [1.0, 0.8363089990996986, 0.33963972286374133];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = yiq_to_rgb(0.0, -0.5957, -0.5226);
    var _const_var = [0.0, 0.49590315888362624, 0.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = yiq_to_rgb(0.8, 0.1, 0.2);
    var _const_var = [1.0, 0.6453830195326262, 1.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = yiq_to_rgb(0.0, 0.0, 0.0);
    var _const_var = [0.0, 0.0, 0.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = yiq_to_rgb(1.0, 0.0, 0.0);
    var _const_var = [1.0, 1.0, 1.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = yiq_to_rgb(0.5, 0.0, 0.0);
    var _const_var = [0.5, 0.5, 0.5];
    assert_iter_almost_equal(tmp, _const_var);
    console.log("--- rgb_to_hls ---");
    tmp = rgb_to_hls(0.5, 0.5, 0.5);
    var _const_var = [0.0, 0.5, 0.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hls(0, 0.5, 1);
    var _const_var = [0.5833333333333334, 0.5, 1.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hls(1, 0, 0);
    var _const_var = [0.0, 0.5, 1.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hls(0, 0, 0);
    var _const_var = [0.0, 0.0, 0.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hls(1, 0.1, 0.3);
    var _const_var = [0.9629629629629629, 0.55, 1.0000000000000002];
    assert_iter_almost_equal(tmp, _const_var);
    console.log("--- hls_to_rgb ---");
    tmp = hls_to_rgb(0.5, 0.5, 0.5);
    var _const_var = [0.25, 0.7499999999999999, 0.75];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hls_to_rgb(0, 0.5, 1);
    var _const_var = [1.0, 0.0, 0.0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hls_to_rgb(1, 0, 0);
    var _const_var = [0, 0, 0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hls_to_rgb(0, 0, 0);
    var _const_var = [0, 0, 0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hls_to_rgb(1, 0.1, 0.3);
    var _const_var = [0.13, 0.07, 0.07];
    assert_iter_almost_equal(tmp, _const_var);
    console.log("--- rgb_to_hsv ---");
    tmp = rgb_to_hsv(0.5, 0.5, 0.5);
    var _const_var = [0.0, 0.0, 0.5];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hsv(0, 0.5, 1);
    var _const_var = [0.5833333333333334, 1.0, 1];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hsv(1, 0, 0);
    var _const_var = [0.0, 1.0, 1];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hsv(0, 0, 0);
    var _const_var = [0.0, 0.0, 0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = rgb_to_hsv(1, 0.1, 0.3);
    var _const_var = [0.9629629629629629, 0.9, 1];
    assert_iter_almost_equal(tmp, _const_var);
    console.log("--- hsv_to_rgb ---");
    tmp = hsv_to_rgb(0.5, 0.5, 0.5);
    var _const_var = [0.25, 0.5, 0.5];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hsv_to_rgb(0, 0.5, 1);
    var _const_var = [1, 0.5, 0.5];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hsv_to_rgb(1, 0, 0);
    var _const_var = [0, 0, 0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hsv_to_rgb(0, 0, 0);
    var _const_var = [0, 0, 0];
    assert_iter_almost_equal(tmp, _const_var);
    tmp = hsv_to_rgb(1, 0.1, 0.3);
    var _const_var = [0.3, 0.27, 0.27];
    assert_iter_almost_equal(tmp, _const_var);

    /// --- BLOCK END 10

}

function test(){
    /// --- BLOCK BEGIN 11
test_assertions();
additional_tests();

    /// --- BLOCK END 11

}

function additional_tests(){
    /// --- BLOCK BEGIN 12
    _tmp = yiq_to_rgb(0.0, 1.0, 0.3)
    _const = [1.0, 0.0, 0.0]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = yiq_to_rgb(2.0, 0.0, 0.0)
    _const = [1.0, 1.0, 1.0]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = rgb_to_hls(0.5, 1.5, 0.2)
    _const = [0.2948717948717949, 0.85, 4.333333333333333]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = hls_to_rgb(0.5, 0.6, 0.2)
    _const = [0.5199999999999999, 0.68, 0.68]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = rgb_to_hsv(0.5, 1.5, 0.2)
    _const = [0.2948717948717949, 0.8666666666666666, 1.5]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = hsv_to_rgb(0.2, 0.6, 0.2)
    _const = [0.176, 0.2, 0.08]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = hsv_to_rgb(0.4, 0.6, 0.2)
    _const = [0.08, 0.2, 0.128]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = hsv_to_rgb(0.7, 0.6, 0.2)
    _const = [0.10399999999999993, 0.08000000000000002, 0.2]
    assert_iter_almost_equal(_tmp, _const)
    _tmp = hsv_to_rgb(0.9, 0.6, 0.2)
    _const = [0.2, 0.08000000000000002, 0.15199999999999997]
    assert_iter_almost_equal(_tmp, _const)

    /// --- BLOCK END 12

}

/// --- BLOCK BEGIN 0
var ONE_THIRD = 1.0 / 3.0;

var ONE_SIXTH = 1.0 / 6.0;

var TWO_THIRD = 2.0 / 3.0;

test();
/// --- BLOCK END 0
