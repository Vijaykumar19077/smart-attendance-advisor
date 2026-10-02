import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

attendance = ctrl.Antecedent(np.arange(0, 101, 1), "attendance")
exam_days = ctrl.Antecedent(np.arange(0, 61, 1), "exam_days")
assignments = ctrl.Antecedent(np.arange(0, 9, 1), "assignments")

risk = ctrl.Consequent(np.arange(0, 101, 1), "risk")

attendance["low"] = fuzz.trapmf(attendance.universe, [0, 0, 50, 65])
attendance["medium"] = fuzz.trimf(attendance.universe, [50, 70, 85])
attendance["high"] = fuzz.trapmf(attendance.universe, [75, 90, 100, 100])

exam_days["soon"] = fuzz.trapmf(exam_days.universe, [0, 0, 3, 10])
exam_days["near"] = fuzz.trimf(exam_days.universe, [5, 15, 25])
exam_days["far"] = fuzz.trapmf(exam_days.universe, [20, 35, 60, 60])

assignments["low"] = fuzz.trapmf(assignments.universe, [0, 0, 1, 2])
assignments["medium"] = fuzz.trimf(assignments.universe, [1, 3, 5])
assignments["high"] = fuzz.trapmf(assignments.universe, [4, 6, 8, 8])

risk["low"] = fuzz.trimf(risk.universe, [0, 0, 35])
risk["medium"] = fuzz.trimf(risk.universe, [25, 50, 70])
risk["high"] = fuzz.trimf(risk.universe, [60, 75, 90])
risk["critical"] = fuzz.trapmf(risk.universe, [80, 90, 100, 100])

rule1 = ctrl.Rule(attendance["low"] & exam_days["soon"], risk["critical"])
rule2 = ctrl.Rule(attendance["low"] & exam_days["near"], risk["high"])
rule3 = ctrl.Rule(attendance["medium"] & exam_days["soon"], risk["high"])
rule4 = ctrl.Rule(attendance["high"] & exam_days["far"], risk["low"])
rule5 = ctrl.Rule(attendance["medium"] & exam_days["far"], risk["medium"])
rule6 = ctrl.Rule(attendance["high"] & assignments["high"], risk["medium"])
rule7 = ctrl.Rule(attendance["low"] & assignments["high"], risk["critical"])
rule8 = ctrl.Rule(attendance["high"] & exam_days["soon"] & assignments["low"], risk["medium"])

risk_control = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4,
    rule5, rule6, rule7, rule8
])

def calculate_risk(attendance_value, exam_days_value, assignments_value):
    simulation = ctrl.ControlSystemSimulation(risk_control)
    simulation.input["attendance"] = attendance_value
    simulation.input["exam_days"] = exam_days_value
    simulation.input["assignments"] = assignments_value
    simulation.compute()
    if "risk" not in simulation.output:
        return 50.0, "Medium"

    risk_score = simulation.output["risk"]

    if risk_score < 35:
        category = "Low"
    elif risk_score < 60:
        category = "Medium"
    elif risk_score < 80:
        category = "High"
    else:
        category = "Critical"

    return round(risk_score, 2), category
