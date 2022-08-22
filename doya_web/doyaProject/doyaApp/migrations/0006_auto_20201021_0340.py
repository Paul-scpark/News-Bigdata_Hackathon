# Generated by Django 3.1.2 on 2020-10-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doyaApp', '0005_delete_news_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_major',
            field=models.CharField(choices=[('major_1', '간호'), ('major_2', '건축'), ('major_3', '경영'), ('major_4', '공예'), ('major_5', '관광'), ('major_6', '광고'), ('major_7', '교육'), ('major_8', '교통 및 운송'), ('major_9', '기계 및 금속'), ('major_10', '농림 및 수산'), ('major_11', '도시 및 토목'), ('major_12', '디자인'), ('major_13', '미술'), ('major_14', '법'), ('major_15', '뷰티아트'), ('major_16', '사진 및 만화'), ('major_17', '사회과학'), ('major_18', '산업공학'), ('major_19', '생명과학'), ('major_20', '서비스'), ('major_21', '소재 및 재료'), ('major_22', '수의학'), ('major_23', '식품'), ('major_24', '약학'), ('major_25', '언론'), ('major_26', '언어 및 문학'), ('major_27', '에너지'), ('major_28', '연극 및 영화'), ('major_29', '영상 및 예술'), ('major_30', '유아교육'), ('major_31', '음악'), ('major_32', '응용소프트웨어'), ('major_33', '의류'), ('major_34', '인문과학'), ('major_35', '자연과학'), ('major_36', '전기 및 전자'), ('major_37', '전산학 및 컴퓨터공학'), ('major_38', '정보 및 통신'), ('major_39', '조선'), ('major_40', '체육'), ('major_41', '초등교육'), ('major_42', '치료 및 보건'), ('major_43', '특수교육'), ('major_44', '화공')], max_length=20, null=True),
        ),
    ]