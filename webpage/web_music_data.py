import pandas as pd
music_data = pd.read_excel('data/노래 라벨링 감정 7개.xlsx')

music_data_list = []
for w, musiclabel in zip(music_data['제목'], music_data['가수'])  :
    musicdata = []
    musicdata.append(w)
    musicdata.append(str(musiclabel))

    music_data_list.append(musicdata)

music_line1 = music_data['감정'].str.contains('공포')
music_line2 = music_data['감정'].str.contains('당황')
music_line3 = music_data['감정'].str.contains('분노')
music_line4 = music_data['감정'].str.contains('슬픔')
music_line5 = music_data['감정'].str.contains('기쁨')
music_line6 = music_data['감정'].str.contains('차분')
music_line7 = music_data['감정'].str.contains('불안')

save_music_line1 = music_data[music_line1]
save_music_line2 = music_data[music_line2]
save_music_line3 = music_data[music_line3]
save_music_line4 = music_data[music_line4]
save_music_line5 = music_data[music_line5]
save_music_line6 = music_data[music_line6]
save_music_line7 = music_data[music_line7]

# 제목-가수 출력
# final_music1 = save_music_line1[['제목','가수']]
# final_music2 = save_music_line2[['제목','가수']]
# final_music3 = save_music_line3[['제목','가수']]
# final_music4 = save_music_line4[['제목','가수']]
# final_music5 = save_music_line5[['제목','가수']]
# final_music6 = save_music_line6[['제목','가수']]
# final_music7 = save_music_line7[['제목','가수']]

# 제목-가수-youtube 링크 출력
final_music1 = save_music_line1[['제목','가수','Youtube']]
final_music2 = save_music_line2[['제목','가수','Youtube']]
final_music3 = save_music_line3[['제목','가수','Youtube']]
final_music4 = save_music_line4[['제목','가수','Youtube']]
final_music5 = save_music_line5[['제목','가수','Youtube']]
final_music6 = save_music_line6[['제목','가수','Youtube']]
final_music7 = save_music_line7[['제목','가수','Youtube']]