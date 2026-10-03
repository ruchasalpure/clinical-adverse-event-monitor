from crewai import Agent

clinical_adverse_event_monitor = Agent(
    role="Clinical Adverse Event Monitor",
    goal="Deliver high-precision autonomous Clinical Adverse Event Monitor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
