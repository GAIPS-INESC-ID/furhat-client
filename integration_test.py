import sys
import clr

# This variable points to where the FAtiMA Libraries are located in your
# machine
fatima_lib_path = r"C:\GIT\furhat-client-fatima\fatima"
sys.path.append(fatima_lib_path)
clr.AddReference("IntegratedAuthoringTool")

from IntegratedAuthoringTool import IntegratedAuthoringToolAsset
from IntegratedAuthoringTool import IATConsts
from IntegratedAuthoringTool.DTOs import CharacterSourceDTO
from RolePlayCharacter import RolePlayCharacterAsset

# Load the Scenario Configuration
iat = IntegratedAuthoringToolAsset.LoadFromFile("C:/Tests/test1.iat")
print('- Scenario Information -')
print('Name: ', iat.ScenarioName)
print('Description: ', iat.ScenarioDescription)
print('\n')


# Load All The Character Sources
sources = []
for s in iat.GetAllCharacterSources():
    sources.append(s.Source)

# Loading the First Character From the Scenario
rpc = RolePlayCharacterAsset.LoadFromFile(sources[0])
rpc.LoadAssociatedAssets()
iat.BindToRegistry(rpc.DynamicPropertiesRegistry)

print('- Character Information -')
print('Name: ', rpc.CharacterName)
print('Mood: ', rpc.Mood)
print('\n')

curState = IATConsts.INITIAL_DIALOGUE_STATE
while(curState != IATConsts.TERMINAL_DIALOGUE_STATE):
    playerDialogs = iat.GetDialogueActionsByState(IATConsts.PLAYER, curState)
    print('- Available Dialogue Options -')
    dialogues = []
    for d in playerDialogs:
        dialogues.append(d)
        print(d.Utterance)
    i = -1
    while(i < 0 or i >= len(dialogues)):
        i = int(input('Select option: '))
    pAct = iat.BuildSpeakActionName(IATConsts.PLAYER, dialogues[i].Id)
    speakEvt = EventHelper.ActionEnd(IATConsts.PLAYER, pAct, rpc.CharacterName)


# var actionName = iat.BuildSpeakActionName(playerStr, chosenDialog.Id)
# var speakEvt = EventHelper.ActionEnd(playerStr, actionName.ToString(), rpc.CharacterName.ToString())
