from deep_translator import GoogleTranslator
import xml.etree.ElementTree as ET
import re

# C:\Users\tuan.thaiminh\Desktop\evt_th\evt_th\skill.xml
# <skill id="1502691" modelName="" name="" icon="" mpostionType="" distancePath="" actionid="" skillEffect="" fullScreen="" attackEffct="" attackEffctPosition="" hitEffct="" showDamageAction="" skipAble="" isFix="" effectOder="Oc0D0sA" meffectType="1" mattackNumberType="1" des="[กายภาพ]: สร้างความเสียหายให้กับยูนิตของศัตรู" functionWay="1" class="Add Status" magicCost="0" range="19" windAttack="" windAtkRatio="-10000" thdAttack="" thdAtkRatio="-10000" wtrAttack="" wtrAtkRatio="-10000" fireAttack="" fireAtkRatio="-10000" skillWeight="" isComplexSkill="" skillRangeImg="1.png" Ragetype="" skillTip="Enhance equipment will not improve the skill effect" hitTipEffect="" underHitEffect=""  rokishikiUp=""/>

to_translate = 'I want to translate this text'
translated = GoogleTranslator(source='auto', target='th').translate(to_translate)
print(translated)

# TODO update attribute ------------------
# file_path = r'C:\Users\tuan.thaiminh\Desktop\evt_th\evt_th\skill.xml'
# tree = ET.parse(file_path)
# root = tree.getroot()
#
# skills = root.findall('skill')
#
# for skill in skills:
#     skill_id = skill.get('skillTip')
#     skill.set("skillTip","hihi")
#     print(f'Skill ID: {skill_id}')
#
# # Lưu lại file XML với các giá trị id đã được cập nhật
# updated_file_path = r'C:\Users\tuan.thaiminh\Desktop\evt_th\evt_th\updated_skill.xml'
# tree.write(updated_file_path, encoding='utf-8', xml_declaration=True)

# TODO ---------

text_to_translate = "[Physical]: Use the flying ring attack,Damage to the enemy unit,Probability &lt;font color='#ff8000'&gt;vertigo target 1 Round&lt;/font&gt;"


# Hàm để dịch các phần văn bản và giữ lại các ký tự đặc biệt
def translate_preserve_special_chars(text, source_lang='auto', target_lang='th'):
    # Định dạng regex để tìm các thẻ HTML
    pattern = re.compile(r'(<.*?>)')
    parts = pattern.split(text)

    # Tạo đối tượng GoogleTranslator
    translator = GoogleTranslator(source=source_lang, target=target_lang)

    # Dịch từng phần và giữ nguyên các thẻ HTML
    translated_parts = [
        part if pattern.match(part) else translator.translate(part)
        for part in parts
    ]

    return ''.join(translated_parts)


# Dịch chuỗi và giữ lại các ký tự đặc biệt
translated_text = translate_preserve_special_chars(text_to_translate)

# In kết quả
print(translated_text)

text_to_translate = "&quot;Dùng để chọn 1 trong: thời trang Thủy Đội (Điềm Quyển,Vụ Khí,Vinh Ảo Quang,Câu Ngọc,Hồng Liên Hỏa,Hàn Võ Kỉ), thời trang thịnh hạ e tộc(Hương Tuyết Cầu,Hồng Nham Mộc,Nguyệt Kiến Thảo,Hồng Mê Hương,Phong Linh Thảo,Mễ Lan Nhân), thời trang Xuân Nhật(Tân Lục Sắc,Xuân Quang Khắc,Noãn Lưu Tú,Lụa Hồng Hà,Thanh Phong Tình,Thái La Y)&quot;"

# Dịch chuỗi và giữ nguyên các dấu ngoặc kép
translated_text = GoogleTranslator(source='auto', target='th').translate(text_to_translate)
print(translated_text)