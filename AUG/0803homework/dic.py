employee_data = {
    "department": "研发部",
    "manager": {
        "name": "李雷",
        "employee_id": "M1001",
        "contact": {
            "email": "lilei@example.com",
            "phone": "13800001111"
        }
    },
    "employees": [
        {
            "name": "韩梅梅",
            "employee_id": "E2001",
            "skills": ["Python", "Django", "REST API"],
            "projects": [
                {"name": "ERP系统", "status": "进行中"},
                {"name": "自动化测试平台", "status": "已完成"}
            ]
        },
        {
            "name": "张伟",
            "employee_id": "E2002",
            "skills": ["Java", "Spring Boot"],
            "projects": [
                {"name": "大数据分析平台", "status": "暂停"}
            ]
        }
    ]
}
erp_data = {
    "orders": [
        {
            "order_id": "SO20250801001",
            "customer": {
                "id": "C1001",
                "name": "浙江华宇电子",
                "location": "杭州"
            },
            "products": [
                {"sku": "P001", "name": "控制器", "qty": 3, "price": 1299.0},
                {"sku": "P002", "name": "传感器", "qty": 10, "price": 299.0}
            ],
            "status": "已发货",
            "invoice": {
                "number": "INV-20250801-0001",
                "total": 6787.0
            }
        }
    ]
}
game_data = {
    "player_id": "U102938",
    "username": "冰封骑士",
    "level": 35,
    "guild": "暗夜联盟",
    "equipment": {
        "weapon": {
            "name": "冰霜之刃",
            "damage": 150,
            "mods": [{"type": "暴击", "value": 0.1}, {"type": "冰冻", "value": 5}]
        },
        "armor": {
            "helmet": {"name": "北境头盔", "def": 20},
            "chest": {"name": "北境铠甲", "def": 50}
        }
    },
    "missions": [
        {
            "name": "守卫村庄",
            "objectives": [
                {"desc": "击败10个强盗", "progress": 6},
                {"desc": "修复木桥", "progress": 1}
            ],
            "status": "进行中"
        }
    ]
}
school_data = {
    "class": "高三（1）班",
    "teacher": {"name": "张老师", "subject": "数学"},
    "students": [
        {
            "id": "S001",
            "name": "林佳",
            "attendance": {"2025-08-01": "Present", "2025-08-02": "Absent"},
            "scores": {"math": 95, "english": 88, "physics": 92}
        },
        {
            "id": "S002",
            "name": "陈涛",
            "attendance": {"2025-08-01": "Present", "2025-08-02": "Present"},
            "scores": {"math": 76, "english": 81, "physics": 68}
        }
    ]
}
logistics_data = {
    "shipment_id": "SH123456",
    "route": {
        "origin": "上海",
        "destination": "成都",
        "checkpoints": [
            {"city": "南京", "time": "2025-08-01 08:00"},
            {"city": "武汉", "time": "2025-08-01 18:00"},
            {"city": "重庆", "time": "2025-08-02 06:00"}
        ]
    },
    "cargo": [
        {"item": "笔记本电脑", "qty": 50, "weight_kg": 25.0},
        {"item": "打印机", "qty": 10, "weight_kg": 80.0}
    ],
    "status": "运输中"
}

