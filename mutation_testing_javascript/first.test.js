const { whatPartOfDay } = require("./app/day-or-night-utility");

describe("When is it daylight?", () => {
  test("Expect to get 'Daylight' for hours between 7 am and 6 pm (18 hours)", () => {
    let expectedValue = "Daylight";
    let daylightHour = 8;
    let actualValue = whatPartOfDay(daylightHour);
    expect(actualValue).toBe(expectedValue);
  });
});

describe("When is it nighttime?", () => {
  test("Expect to get 'Nighttime' for hours between 6 pm and 7 am", () => {
    let expectedValue = "Nighttime";
    let nighttimeHour = 20;
    let actualValue = whatPartOfDay(nighttimeHour);
    expect(actualValue).toBe(expectedValue);
  });
});
