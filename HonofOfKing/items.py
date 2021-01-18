# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeroItem(scrapy.Item):
    # 英雄名称
    name = scrapy.Field()
    # 位置
    position = scrapy.Field()
    # 最大生命
    health = scrapy.Field()
    # 最大法力
    mana = scrapy.Field()
    # 物理攻击
    attack_damage = scrapy.Field()
    # 法术攻击
    ability_power = scrapy.Field()
    # 物理防御
    armor = scrapy.Field()
    # 物理减伤率
    armor_percent = scrapy.Field()
    # 法术防御
    magic_resist = scrapy.Field()
    # 法术减伤率
    magic_resist_percent = scrapy.Field()
    # 移速
    movement_speed = scrapy.Field()
    # 物理护甲穿透
    armor_penetration = scrapy.Field()
    # 法术护甲穿透
    magic_penetration = scrapy.Field()
    # 攻速加成
    attack_speed = scrapy.Field()
    # 暴击几率
    critical_strike_chance = scrapy.Field()
    # 暴击效果
    critical_damage = scrapy.Field()
    # 物理吸血
    life_steal = scrapy.Field()
    # 法术吸血
    spell_vamp = scrapy.Field()
    # 冷却缩减
    cooldown_reduction = scrapy.Field()
    # 攻击范围
    attack_range = scrapy.Field()
    # 韧性
    tenacity = scrapy.Field()
    # 生命回复
    health_regen = scrapy.Field()
    # 法力回复
    mana_regen = scrapy.Field()

