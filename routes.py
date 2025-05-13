from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ContentType
from aiogram import Router
from aiogram import F
import random
import json
import asyncio

r = Router()

#@r.message(F.text[0:1].lower() == '.')
#async def add_phse(ms: Message):
    #await ms.delete()
    #await ms.answer(ms.text[1:])
 
@r.message(F.text[0] == '.')
async def add_phse(ms: Message):
    await ms.answer(ms.text[1:])
    print(f"ЕБать секретни: {ms.from_user.full_name}\ntext: {ms.text}")
    await ms.delete()

@r.message(F.text.lower().contains("чичивап"))
async def add_phrase(ms: Message):
    await ms.reply(ms.text)
    
@r.message(F.text.lower() == 'узнать фразы')
async def add_phrase(ms: Message):
    print(ms.chat.id)
    with open("data.json") as dataFile:
        dataInfo = json.load(dataFile)
        for i in dataInfo['info']:
            flag = False
            if(int(i['id']) == ms.chat.id):
                random_phrases = i['phrases']
                flag = True
                break
        if(flag == False):
            await ms.reply('фраз нет кароче')
            dataInfo['info'].append({
                "id":ms.chat.id,
                "phrases":[]
            })
            with open('data.json', 'w') as dataW:
                json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
            return 0
    if len(random_phrases) == 0:
        await ms.reply('фраз нет кароче')
        return 0
    answer = 'вот те фразы\n'
    for i in range(len(random_phrases)):
        answer += f'{i+1}: {random_phrases[i]}\n'
    await ms.reply(answer)
    
@r.message(F.text == 'получить рандом фразу')
async def add_phrase(ms: Message):
    with open("data.json") as dataFile:
        dataInfo = json.load(dataFile)
        for i in dataInfo['info']:
            flag = False
            if(int(i['id']) == ms.chat.id):
                if (i['phrases'] == []):
                    await ms.reply('фраз нет кароче')
                    return 0
                await ms.reply(i['phrases'][random.randint(0,(len(i['phrases'])-1))])
                flag = True
                break
        if(flag == False):
            await ms.reply('фраз нет кароче')
            dataInfo['info'].append({
                "id":ms.chat.id,
                "phrases":[]
            })
            with open('data.json', 'w') as dataW:
                json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
            return 0
    
@r.message(F.text[0:14].lower() == 'добавить фразу')
async def add_phrase(ms: Message):
    with open("data.json") as dataFile:
        dataInfo = json.load(dataFile)
        for i in dataInfo['info']:
            flag = False
            if ms.text[15:].strip() == "":
                await ms.reply("пустато")
            if(int(i['id']) == ms.chat.id):
                if ms.text[15:] in i['phrases']:
                    await ms.reply('есть такая фраза пупсик')
                    return 0
                i['phrases'].append(ms.text[15:])
                flag = True
                with open('data.json', 'w') as dataW:
                    json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
                break
        if(flag == False):
            await ms.reply('фраз нет кароче')
            dataInfo['info'].append({
                "id":ms.chat.id,
                "phrases":[]
            })
            with open('data.json', 'w') as dataW:
                json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
            return 0
    await ms.reply('добавель')
    
@r.message(F.text[0:13].lower() == 'удалить фразу')
async def delete_phrase(ms: Message):
    with open("data.json") as dataFile:
        dataInfo = json.load(dataFile)
        for i in dataInfo['info']:
            flag = False
            if(int(i['id']) == ms.chat.id):
                if len(ms.text.split(' ')) < 3:
                    await ms.reply('эээ, а че удалять')
                    return 0
                id = int(ms.text[13:]) - 1
                if id in i['phrases']:
                    await ms.reply('ти шо ебобо, нет такой фразу')
                    return 0
                # elif int(id) < 1:
                #     await ms.reply('ти шо ебобо, како меньше отнаго')
                #     return 0
                i['phrases'].pop(id)
                await ms.reply('удалил, проверяй😈')
                flag = True
                with open('data.json', 'w') as dataW:
                    json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
                break
        if(flag == False):
            await ms.reply('фраз нет кароче')
            dataInfo['info'].append({
                "id":ms.chat.id,
                "phrases":[]
            })
            with open('data.json', 'w') as dataW:
                json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
            return 0

@r.message()
async def on_photo(ms: Message):
    if ms.from_user.id == 6124318812:
        return 0
    if ms.content_type != ContentType.VIDEO and ms.content_type != ContentType.PHOTO and ms.content_type != ContentType.ANIMATION and ms.content_type != ContentType.STICKER:
        return 0
    if ms.from_user.id == 1:
        return 0
    with open("data.json") as dataFile:
        dataInfo = json.load(dataFile)
        for i in dataInfo['info']:
            flag = False
            if(int(i['id']) == ms.chat.id):
                if (i['phrases'] == []):
                    await ms.reply('фраз нет кароче')
                    return 0
                await ms.reply(i['phrases'][random.randint(0,(len(i['phrases'])-1))])
                flag = True
                break
        if(flag == False):
            await ms.reply('фраз нет кароче')
            dataInfo['info'].append({
                "id":ms.chat.id,
                "phrases":[]
            })
            with open('data.json', 'w') as dataW:
                json.dump(dataInfo, dataW, indent=4,ensure_ascii=False)
            return 0
@r.message()
async def add_phse(ms: Message):
    #if ms.chat.id != -1002631703522:
        #return 0
    print(ms.from_user.id)
    print(ms.from_user.full_name)
    print(ms.text)