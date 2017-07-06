import sys
import clr

# This variable points to where the FAtiMA Libraries are located in your
# machine
fatima_lib_path = r"C:\GIT\furhat-client-fatima\fatima"
sys.path.append(fatima_lib_path)
clr.AddReference("IntegratedAuthoringTool")

from IntegratedAuthoringTool import IntegratedAuthoringToolAsset

iat = IntegratedAuthoringToolAsset.LoadFromFile("C:/Tests/test1.iat")

print(iat.ScenarioName)
