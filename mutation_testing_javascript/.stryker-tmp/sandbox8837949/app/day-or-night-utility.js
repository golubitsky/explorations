function stryNS_9fa48() {
  var g = new Function("return this")();
  var ns = g.__stryker__ || (g.__stryker__ = {});
  if (ns.activeMutant === undefined && g.process && g.process.env && g.process.env.__STRYKER_ACTIVE_MUTANT__) {
    ns.activeMutant = g.process.env.__STRYKER_ACTIVE_MUTANT__;
  }
  function retrieveNS() {
    return ns;
  }
  stryNS_9fa48 = retrieveNS;
  return retrieveNS();
}
stryNS_9fa48();
function stryCov_9fa48() {
  var ns = stryNS_9fa48();
  var cov = ns.mutantCoverage || (ns.mutantCoverage = {
    static: {},
    perTest: {}
  });
  function cover() {
    var c = cov.static;
    if (ns.currentTestId) {
      c = cov.perTest[ns.currentTestId] = cov.perTest[ns.currentTestId] || {};
    }
    var a = arguments;
    for (var i = 0; i < a.length; i++) {
      c[a[i]] = (c[a[i]] || 0) + 1;
    }
  }
  stryCov_9fa48 = cover;
  cover.apply(null, arguments);
}
function stryMutAct_9fa48(id) {
  var ns = stryNS_9fa48();
  function isActive(id) {
    if (ns.activeMutant === id) {
      if (ns.hitCount !== void 0 && ++ns.hitCount > ns.hitLimit) {
        throw new Error('Stryker: Hit count limit reached (' + ns.hitCount + ')');
      }
      return true;
    }
    return false;
  }
  stryMutAct_9fa48 = isActive;
  return isActive(id);
}
function whatPartOfDay(hour) {
  if (stryMutAct_9fa48("0")) {
    {}
  } else {
    stryCov_9fa48("0");
    if (stryMutAct_9fa48("3") ? hour >= 7 || hour < 18 : stryMutAct_9fa48("2") ? false : stryMutAct_9fa48("1") ? true : (stryCov_9fa48("1", "2", "3"), (stryMutAct_9fa48("6") ? hour < 7 : stryMutAct_9fa48("5") ? hour > 7 : stryMutAct_9fa48("4") ? true : (stryCov_9fa48("4", "5", "6"), hour >= 7)) && (stryMutAct_9fa48("9") ? hour >= 18 : stryMutAct_9fa48("8") ? hour <= 18 : stryMutAct_9fa48("7") ? true : (stryCov_9fa48("7", "8", "9"), hour < 18)))) {
      if (stryMutAct_9fa48("10")) {
        {}
      } else {
        stryCov_9fa48("10");
        return stryMutAct_9fa48("11") ? "" : (stryCov_9fa48("11"), "Daylight");
      }
    }
    return stryMutAct_9fa48("12") ? "" : (stryCov_9fa48("12"), "Nighttime");
  }
}
module.exports = stryMutAct_9fa48("13") ? {} : (stryCov_9fa48("13"), {
  whatPartOfDay
});
module.exports = stryMutAct_9fa48("14") ? {} : (stryCov_9fa48("14"), {
  whatPartOfDay
});