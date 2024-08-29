import re


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


def part_one(data):
    workflows, parts = parsed(data)
    results = run_sorting_process(parts, workflows)
    total = sum([sum(accepted.values()) for accepted in results["A"]])
    print(total)


if __name__ == "__main__":
    with open("day_19_input.txt", "r") as file:
        data = file.read()
    part_one(data)
