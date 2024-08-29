import re
from copy import deepcopy
import math

def parsed_workflows(workflows_raw):
    workflows = {}

    for line in workflows_raw.split("\n"):
        name, rest = line.split("{")
        workflows[name] = []
        for raw_rule in rest[:-1].split(","):
            s = raw_rule.split(":")
            rule = {"destination": s[-1]}
            if len(s) == 2:
                match = re.match(r"(\w)(>|<)(\d+)", s[0])
                rule["category"] = match[1]
                rule["operator"] = match[2]
                rule["value"] = int(match[3])
                pass
            elif len(s) == 1:
                pass
            else:
                print(f"unknown rule {raw_rule}")
                exit()
            workflows[name].append(rule)

    return workflows


def parsed(data):
    workflows_raw, parts_raw = data.split("\n\n")

    parts = []
    for line in parts_raw.split("\n"):
        part = {}
        for rating in line.split(","):
            rating = rating.replace("{", "")
            rating = rating.replace("}", "")
            category, value = rating.split("=")
            part[category] = int(value)
        parts.append(part)

    return parsed_workflows(workflows_raw), parts


def destination(part, rule):
    a = part[rule["category"]]
    o = rule["operator"]
    b = rule["value"]
    d = rule["destination"]

    if o == "<":
        return d if a < b else None
    elif o == ">":
        return d if a > b else None
    else:
        print(f"unknown operator {o}")
        exit()


def run_sorting_process(parts, workflows):
    results = {"A": [], "R": []}

    for part in parts:
        workflow = workflows["in"]

        while workflow:
            for rule in workflow:
                if "operator" in rule:
                    d = destination(part, rule)
                else:
                    d = rule["destination"]

                if d is not None:
                    if d in results:
                        results[d].append(part)
                        workflow = None
                        break  # stop processing rules
                    elif d in workflows:
                        workflow = workflows[d]
                        break
                    else:
                        print(f"unknown destination {d}")
                        exit()
    return results


def default_filter():
    return {
        "x": {"min": 1, "max": 4000},
        "m": {"min": 1, "max": 4000},
        "a": {"min": 1, "max": 4000},
        "s": {"min": 1, "max": 4000},
    }


def accept_rule(reject_rule):
    new_rule = deepcopy(reject_rule)
    new_rule["destination"]
    if reject_rule["operator"] == "<":
        new_rule["operator"] = ">"
        new_rule["value"] = reject_rule["value"] - 1
    else:
        new_rule["operator"] = "<"
        new_rule["value"] = reject_rule["value"] + 1

    return new_rule


def is_split(rule):
    return "operator" in rule


def matching_filter(filter, rule, workflows=[]):
    new_filter = deepcopy(filter)
    category = rule["category"]

    if rule["destination"] == "A" or rule["destination"] in workflows:
        if rule["operator"] == "<":
            new_filter[category]["max"] = min(
                new_filter[category]["max"], rule["value"] - 1
            )
        elif rule["operator"] == ">":
            new_filter[category]["min"] = max(
                new_filter[category]["min"], rule["value"] + 1
            )

    return new_filter


def non_matching_filter(filter, rule, workflows=[]):
    new_filter = deepcopy(filter)

    category = rule["category"]

    if rule["destination"] == "A" or rule["destination"] in workflows:
        if rule["operator"] == "<":
            new_filter[category]["min"] = max(
                new_filter[category]["min"], rule["value"]
            )
        elif rule["operator"] == ">":
            new_filter[category]["max"] = min(
                new_filter[category]["max"], rule["value"]
            )
    if rule["destination"] == "R":
        if rule["operator"] == "<":
            new_filter[category]["min"] = max(
                new_filter[category]["min"], rule["value"]
            )
        elif rule["operator"] == ">":
            new_filter[category]["max"] = min(
                new_filter[category]["max"], rule["value"]
            )
        pass

    return new_filter


def find_all_filters(workflows):
    all_filters = []

    def search(rules, filter):
        if not rules:
            return

        rule, *remaining_rules = rules

        if is_split(rule):
            if rule["destination"] == "A":
                # if it is accepted, end of the search!
                all_filters.append(matching_filter(filter, rule))
                # non-matching values can keep evaluating rules. recurse.
                search(remaining_rules, non_matching_filter(filter, rule))
            elif rule["destination"] == "R":
                # ignore the rejected matching values
                # recurse with the non-matching values:
                search(remaining_rules, non_matching_filter(filter, rule))
            elif rule["destination"] in workflows:
                search(
                    workflows[rule["destination"]],
                    matching_filter(filter, rule, workflows),
                )
                search(remaining_rules, non_matching_filter(filter, rule, workflows))
            else:
                print("unknown destination")
                exit()
        else:
            if rule["destination"] == "A":
                all_filters.append(filter)
            elif rule["destination"] in workflows:
                new_rules = workflows[rule["destination"]]
                search(new_rules, filter)

    search(workflows["in"], default_filter())

    return all_filters


def part_one(data):
    workflows, parts = parsed(data)
    results = run_sorting_process(parts, workflows)
    total = sum([sum(accepted.values()) for accepted in results["A"]])
    print(total)


def part_two(data):
    workflows, _ = parsed(data)

    total = 0
    for filter in find_all_filters(workflows):
        xx = 1
        for category in filter:
            x = filter[category]['max'] - filter[category]['min'] + 1
            xx *= x
        total += xx
    print(total)

if __name__ == "__main__":
    with open("day_19_input.txt", "r") as file:
        data = file.read()
    part_two(data)
