from webpage.web_module import *
from webpage.web_music_data import *


# 예측 함수
def predict(predict_sentence):

    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok,vocab, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=0)
    
    model.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length= valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids)


        test_eval=[]
        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()

            if np.argmax(logits) == 0:
                test_eval.append("기쁨이")
            elif np.argmax(logits) == 1:
                test_eval.append("슬픔이")
            elif np.argmax(logits) == 2:
                test_eval.append("당황이")
            elif np.argmax(logits) == 3:
                test_eval.append("공포가")
            elif np.argmax(logits) == 4:
                test_eval.append("불안이")
            elif np.argmax(logits) == 5:
                test_eval.append("분노가")
            elif np.argmax(logits) == 6:
                test_eval.append("차분이")

        result_emotion = ">> 오늘의 일기에서 " + test_eval[0] + " 느껴집니다.\n\n\n\n\n\n"
        # return result_emotion
        
        
        # print(">> 입력하신 내용에서 " + test_eval[0] + " 느껴집니다.")

        music_eval=[]
        for m in out:
            logits=m
            logits = logits.detach().cpu().numpy()

            if np.argmax(logits) == 0:
                music_eval.append(final_music5.sample(1))
                
            elif np.argmax(logits) == 1:
                music_eval.append(final_music4.sample(1))
                
            elif np.argmax(logits) == 2:
                music_eval.append(final_music2.sample(1))
                
            elif np.argmax(logits) == 3:
                music_eval.append(final_music1.sample(1))
                
            elif np.argmax(logits) == 4:
                music_eval.append(final_music7.sample(1))
                
            elif np.argmax(logits) == 5:
                music_eval.append(final_music3.sample(1))
                
            elif np.argmax(logits) == 6:
                music_eval.append(final_music6.sample(1))
                
        result_music = ">> 오늘의 하루와 어울리는 노래는 " + "["+music_eval[0].iloc[0].at['제목']+"-"+ music_eval[0].iloc[0].at['가수']+ "]" + " 입니다."

        result = result_emotion+result_music
        return result