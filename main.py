import json


with open('changes.json', 'r') as openfile:
    # Reading from json file
    changes = json.load(openfile)
with open('mixtape.json', 'r') as openfile:
    # Reading from json file
    mixtape = json.load(openfile)
    
with open('mixtape.json', 'r') as openfile:
    # Reading from json file
    output = json.load(openfile)



def add_song_to_playlist(song_id,playlist_id):
   
    for m in mixtape['playlists']:
        
        if m['id'] == playlist_id:
            m['song_ids'].append(str(song_id))
    
def add_playlist(user_id,song_ids):
    newplaylist = {
      "id": len(mixtape['playlists'])+1,
      "owner_id": user_id,
      "song_ids": song_ids
    }
    
    mixtape['playlists'].append(newplaylist)
def remove_playlist(playlist_id):
    
    for i in mixtape['playlists']:
        
        if i['id'] == playlist_id:
            mixtape['playlists'].remove(i)
    

for i in changes:
    if(i['type'] == 'add_song_to_playlist'):
        add_song_to_playlist(i['song_id'],i['playlist_id'])
    
    if(i['type'] == 'add_playlist'):
      
        add_playlist(i['user_id'],i['song_ids'])
    
    if(i['type'] == 'remove_playlist'):
        remove_playlist(i['playlist_id'])
        
        
output = mixtape    
#print(output)
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
    
    
#print(output)