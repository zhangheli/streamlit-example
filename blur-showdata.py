import json
from datetime import datetime, timezone, timedelta
from urllib.parse import quote

import pytz
import streamlit as st
import requests

uri = "https://core-api.prod.blur.io/v1/activity/event-filter"
user = "0x0d01FFcd7c1a17eb87718470ca2F227097234cD5".lower()
filters = {
    "count": 100,
    "eventFilter": {
        "sale": {"toAddress": user, "fromAddress": user},
        "mint": {"toAddress": user},
        "transfer": {"toAddress": user, "fromAddress": user}}
}
params = {
    "filters": json.dumps(filters)
}


print_url = "https://core-api.prod.blur.io/v1/activity/event-filter?filters=" + quote(json.dumps(filters))
print(print_url)
# res = requests.get(uri, params=params)
# print(res.request.url)
# data = res.json()

def _get_tasks():
    blur_tasks = [
        ["0x34d85c9CDeB23FA97cb08333b511ac86E1C4E258", "otherdeed"],
        ["0x23581767a106ae21c074b2276d25e5c3e136a68b", "proof-moonbirds"],
        ["0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b", "clonex"],
        ["0xba30e5f9bb24caa003e9f2f0497ad287fdf95623", "bored-ape-kennel-club"],
        ["0xbd3531da5cf5857e7cfaa92426877b022e612cf8", "pudgypenguins"],

        ["0x306b1ea3ecdf94ab739f1910bbda052ed4a9f949", "beanzofficial"],
        ["0x8a90cab2b38dba80c64b7734e58ee1db38b8992e", "doodles-official"],

        ["0x79FCDEF22feeD20eDDacbB2587640e45491b757f", "mfer"],
        ["0x524cAB2ec69124574082676e6F654a18df49A048", "lilpudgys"],
        ["0x7F36182DeE28c45dE6072a34D29855BaE76DBe2f", "wolf-game"],
        ["0xbCe3781ae7Ca1a5e050Bd9C4c77369867eBc307e", "goblintown"],
        ["0x39ee2c7b3cb80254225884ca001F57118C8f21B6", "thepotatoz"],
        ["0x57a204AA1042f6E66DD7730813f4024114d74f37", "cyberkongz"],
    ]

    bid_collection = dict([(x[0].lower(), x[1]) for x in blur_tasks])
    return bid_collection

def _fetch_data():
    return {
    "success": 1,
    "activityItems": [
        {
            "id": "173719527",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "19457",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/19457-2b696e99f0696fe3",
            "eventType": "SALE",
            "price": {
                "amount": "5.08",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x1a71709c62ad2013ea377f11602099a2b411a93c",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T12:35:23.000Z",
            "transactionHash": "0xf20f88767a23972d75605c762f2c3e3b02ca5fe26d2f08664b778d13756594ee",
            "marketplace": "BLUR"
        },
        {
            "id": "173713726",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "3375",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/3375-82b76f7838ced906",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xa38885d2225ee84a4b96ec7cf3fde0e1308945bf",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T12:25:23.000Z",
            "transactionHash": "0xf9332912f2b42bda32160a3513af90c60859c41a5d4627dd3b41db9ad770de53",
            "marketplace": "BLUR"
        },
        {
            "id": "173711724",
            "contractAddress": "0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91",
            "tokenId": "4763",
            "imageUrl": "https://images.blur.io/_blur-prod/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/4763-c1098756050b7c30",
            "eventType": "SALE",
            "price": {
                "amount": "1.31",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x34c4388c9023dca233ae49e26332434fa9c0d0aa",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T12:19:47.000Z",
            "transactionHash": "0x27c1a1e0e9d40e877631f4472f48e623292f672866d8906f8542455edf3eb2a5",
            "marketplace": "BLUR"
        },
        {
            "id": "173702579",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "8007",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/8007-760293bade65fbb0",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x8929cf8b9acfb5f1a6156e67ea573a79f16be090",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T12:01:35.000Z",
            "transactionHash": "0x07b724e74fcd18e769c1f157e339a080cee345ae6343462892431edf591a03e9",
            "marketplace": "BLUR"
        },
        {
            "id": "173693332",
            "contractAddress": "0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91",
            "tokenId": "3975",
            "imageUrl": "https://images.blur.io/_blur-prod/0x394e3d3044fc89fcdd966d3cb35ac0b32b0cda91/3975-7ca4b36e3220392d",
            "eventType": "SALE",
            "price": {
                "amount": "1.31",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xfc69b7bb84410bc6789b1cb82c11c9a2dac3d669",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T11:34:47.000Z",
            "transactionHash": "0xe9d9c23b70230993c84209dd9c9b2c28cf53defff2d2944088e544eee966b82e",
            "marketplace": "BLUR"
        },
        {
            "id": "173675148",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "4173",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/4173-66f859c98806d78e",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xd9944919dca2d49c6d6f272353b46703eb9335fc",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T10:57:47.000Z",
            "transactionHash": "0x65f892061f7b5919cd56680261face88be2a69d929e6ee48a9c761c26ac59083",
            "marketplace": "BLUR"
        },
        {
            "id": "173675146",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "3912",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/3912-ecbc59ca320638e1",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xd9944919dca2d49c6d6f272353b46703eb9335fc",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T10:57:47.000Z",
            "transactionHash": "0x65f892061f7b5919cd56680261face88be2a69d929e6ee48a9c761c26ac59083",
            "marketplace": "BLUR"
        },
        {
            "id": "173675145",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "368",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/368-f1d9d95e466af58d",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xd9944919dca2d49c6d6f272353b46703eb9335fc",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T10:57:47.000Z",
            "transactionHash": "0x65f892061f7b5919cd56680261face88be2a69d929e6ee48a9c761c26ac59083",
            "marketplace": "BLUR"
        },
        {
            "id": "173675134",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "1632",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/1632-fad5d4c186505f9d",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xd9944919dca2d49c6d6f272353b46703eb9335fc",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T10:57:47.000Z",
            "transactionHash": "0x65f892061f7b5919cd56680261face88be2a69d929e6ee48a9c761c26ac59083",
            "marketplace": "BLUR"
        },
        {
            "id": "173663875",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "1281",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/1281-297a0cf4c07567a4",
            "eventType": "SALE",
            "price": {
                "amount": "5.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x3ce1a9014c591ea471c38880dae4630607a88663",
                "username": None
            },
            "createdAt": "2023-02-23T10:29:23.000Z",
            "transactionHash": "0x968c290d5d654ef451fd75fb7403527f38974fe833a742d1de8afb24219f804d",
            "marketplace": "BLUR"
        },
        {
            "id": "173662713",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "4548",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/4548-fc12cf0beda981be",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xfe4b04ade5478f3b649614221cdcc43ee31fa27e",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662712",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "3286",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/3286-9620a20e1caff019",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xfe4b04ade5478f3b649614221cdcc43ee31fa27e",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662711",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "11895",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/11895-65e4d63a143c10ce",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xcbc69338c98887ddf680da64bf2495855e3a7218",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662710",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "15022",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/15022-85d49bf122ba4fd3",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xb8d8d919244f8015ca3c61cd7211386a477fce53",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662709",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "9143",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/9143-010330855c36e5fb",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xcbc69338c98887ddf680da64bf2495855e3a7218",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662708",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "719",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/719-a85783753a07c217",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xfe4b04ade5478f3b649614221cdcc43ee31fa27e",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662707",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "6984",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/6984-9a66ba90c4ec901e",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xcbc69338c98887ddf680da64bf2495855e3a7218",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662706",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "4933",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/4933-21ee47510a93790e",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xcbc69338c98887ddf680da64bf2495855e3a7218",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662705",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "19454",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/19454-6e23d86cc4dbf8d4",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xb8d8d919244f8015ca3c61cd7211386a477fce53",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662704",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "18212",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/18212-dcc75fc701670e84",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x864d2437ed789ccec3107727cc0cf65b0cd0a3b9",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662703",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "15150",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/15150-50f10744bee11057",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xfe4b04ade5478f3b649614221cdcc43ee31fa27e",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662702",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "13506",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/13506-bd81411c1318140a",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xfe4b04ade5478f3b649614221cdcc43ee31fa27e",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662701",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "11443",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/11443-d9e0163a660b4f84",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xfe4b04ade5478f3b649614221cdcc43ee31fa27e",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662700",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "1933",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/1933-8309c3680a53f211",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xcbc69338c98887ddf680da64bf2495855e3a7218",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173662699",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "18504",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/18504-a6a4b7d10cc83b67",
            "eventType": "SALE",
            "price": {
                "amount": "5.14",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x1572d06d995651b2717df78f0d31f86b6d34200a",
                "username": None
            },
            "createdAt": "2023-02-23T10:27:23.000Z",
            "transactionHash": "0xb1dd6ef21b4b0527843ef3efd30fa900682b5060a795851fc00afa98ec64ef64",
            "marketplace": "BLUR"
        },
        {
            "id": "173644708",
            "contractAddress": "0x1792a96e5668ad7c167ab804a100ce42395ce54d",
            "tokenId": "6023",
            "imageUrl": "https://images.blur.io/_blur-prod/0x1792a96e5668ad7c167ab804a100ce42395ce54d/6023-cadf49f5d1db1380",
            "eventType": "SALE",
            "price": {
                "amount": "0.99",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x37b45293aaf561a2cdf9e260bf984b643dd3699a",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T09:49:35.000Z",
            "transactionHash": "0x05679d199dc01c4e98214eeb016dd47544728f4c3300d559868a5b6de69bc0a7",
            "marketplace": "BLUR"
        },
        {
            "id": "173616667",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "558",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/558-700468fea6255e95",
            "eventType": "SALE",
            "price": {
                "amount": "15.06",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T08:45:35.000Z",
            "transactionHash": "0xf9b258c12ef26847a9c08bb189207c2d18aae8490deddb6df2877909c67bfa18",
            "marketplace": "BLUR"
        },
        {
            "id": "173561649",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "558",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/558-700468fea6255e95",
            "eventType": "SALE",
            "price": {
                "amount": "15.07",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T06:52:11.000Z",
            "transactionHash": "0x0dc2513f55ad2be60a0184312a0cc38c4130ae53e48d09c9fa6c06b3847c8b1d",
            "marketplace": "BLUR"
        },
        {
            "id": "173530952",
            "contractAddress": "0xbd3531da5cf5857e7cfaa92426877b022e612cf8",
            "tokenId": "8595",
            "imageUrl": "https://images.blur.io/_blur-prod/0xbd3531da5cf5857e7cfaa92426877b022e612cf8/8595-b9b192367ceff42a",
            "eventType": "SALE",
            "price": {
                "amount": "5.54",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x76dc804b968a1adde9ee8f9248e91e527cfcc38f",
                "username": None
            },
            "createdAt": "2023-02-23T06:14:47.000Z",
            "transactionHash": "0xe76f9a14cc8cf19e7e870eab2dec77e4baf18bdc33ad614701080f90122ac949",
            "marketplace": "BLUR"
        },
        {
            "id": "173512599",
            "contractAddress": "0x769272677fab02575e84945f03eca517acc544cc",
            "tokenId": "8613",
            "imageUrl": "https://images.blur.io/_blur-prod/0x769272677fab02575e84945f03eca517acc544cc/6389-65bde76766152ced",
            "eventType": "SALE",
            "price": {
                "amount": "4.55",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x6d371ac2176efc639da95c569e37f0374296fc70",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T05:25:23.000Z",
            "transactionHash": "0xaea88ecb004a4be92eea231f630dee7a310caab67f9e7b716964516b7be81c2e",
            "marketplace": "BLUR"
        },
        {
            "id": "173501475",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "6741",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/6741-c7bbcfa548b9dc88",
            "eventType": "SALE",
            "price": {
                "amount": "15.09",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xa7078ddf23d29e9d6e54e34909cd2ac1b33a67c5",
                "username": None
            },
            "createdAt": "2023-02-23T04:59:35.000Z",
            "transactionHash": "0x146fe2426c31f2908233bc3bdd7ee3f3e55b71ef650519083400e86cf9508c30",
            "marketplace": "BLUR"
        },
        {
            "id": "173501440",
            "contractAddress": "0x60e4d786628fea6478f785a6d7e704777c86a7c6",
            "tokenId": "8620",
            "imageUrl": "https://images.blur.io/_blur-prod/0x60e4d786628fea6478f785a6d7e704777c86a7c6/8620-c616ffbb21e8a391",
            "eventType": "SALE",
            "price": {
                "amount": "16.18",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xf40f793ba6bf4ff3b7a7180e4da9c721bea85c69",
                "username": None
            },
            "createdAt": "2023-02-23T04:59:23.000Z",
            "transactionHash": "0xa51bc841b04930c171314cf3cf6ae685e01cdf95892e488f9aabb1a719ff6685",
            "marketplace": "BLUR"
        },
        {
            "id": "173488835",
            "contractAddress": "0x7bd29408f11d2bfc23c34f18275bbf23bb716bc7",
            "tokenId": "18946",
            "imageUrl": "https://images.blur.io/_blur-prod/0x7bd29408f11d2bfc23c34f18275bbf23bb716bc7/18946-7ff32917d81d9335",
            "eventType": "SALE",
            "price": {
                "amount": "3.23",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xc45c7a82623d33ee882f7cd2fb1c74de44ace7fb",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T04:22:59.000Z",
            "transactionHash": "0xa75d9b0951ab676d82994212a7ddaade5a8677a9929737615d1f6444787b670b",
            "marketplace": "BLUR"
        },
        {
            "id": "173488174",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "1800",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/1800-d4e0db37e0d0711a",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xe968099c18ad1b28d49fbf103b844a7f03137c40",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T04:21:35.000Z",
            "transactionHash": "0x7dfab9b42d36c9b99abd248cfa1c69fe3d662af7dbc48b11c33ca358582a3fed",
            "marketplace": "BLUR"
        },
        {
            "id": "173487909",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "8894",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/8894-a525bdadf7a6f3aa",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487908",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "8846",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/8846-64c927ec191c2020",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487907",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "8097",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/8097-3a5781bd829308bc",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487906",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "7898",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/7898-67ac85975f20c9e9",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487905",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "7754",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/7754-ead20a554e462c6a",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487903",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "761",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/761-8d9b4e1663669e0a",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487901",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "7384",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/7384-c995ee742496f303",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487900",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "6904",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/6904-5a50c137e861d44d",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487898",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "6190",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/6190-fd1f74cc7224cde7",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487897",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "5946",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/5946-1499e87a37188e12",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487895",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "5398",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/5398-1e978c9dbdae9606",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487894",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "2516",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/2516-ffad244c14d825de",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487893",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "2398",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/2398-1bbf7d64bd2f75c5",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173487890",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "1747",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/1747-1f0d4b37f6c12479",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T04:20:59.000Z",
            "transactionHash": "0xfe53ffa5c8f688292d167ddaa15476615d5aa1572f1880d34ae2c622d44a4e4b",
            "marketplace": "BLUR"
        },
        {
            "id": "173480391",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "8515",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/8515-433b3aeb3bc8d435",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T03:59:59.000Z",
            "transactionHash": "0x610d2a6491fa38ca4e4f5092eb81958c39eb1b88937d4a280eebd3db98feaef8",
            "marketplace": "BLUR"
        },
        {
            "id": "173480385",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "6210",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/6210-8c845b74be697fd2",
            "eventType": "SALE",
            "price": {
                "amount": "5.74",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T03:59:59.000Z",
            "transactionHash": "0x610d2a6491fa38ca4e4f5092eb81958c39eb1b88937d4a280eebd3db98feaef8",
            "marketplace": "BLUR"
        },
        {
            "id": "173474420",
            "contractAddress": "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258",
            "tokenId": "57660",
            "imageUrl": "https://images.blur.io/_blur-prod/0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258/57660-4e0f2c6eb31f3c17",
            "eventType": "SALE",
            "price": {
                "amount": "2",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x2ca212af7e65631d46a1cf406427f257d2976a71",
                "username": None
            },
            "createdAt": "2023-02-23T03:40:23.000Z",
            "transactionHash": "0x64693bbc74fb03dfbff5ddf345a9c7237790173469891330af1bf4b0c8ce3e62",
            "marketplace": "BLUR"
        },
        {
            "id": "173474419",
            "contractAddress": "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258",
            "tokenId": "61118",
            "imageUrl": "https://images.blur.io/_blur-prod/0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258/61118-0cab46bd27c6608b",
            "eventType": "SALE",
            "price": {
                "amount": "2",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xd7f4e01b66bedde8aa85300130cc6c7b9823942c",
                "username": None
            },
            "createdAt": "2023-02-23T03:40:23.000Z",
            "transactionHash": "0x64693bbc74fb03dfbff5ddf345a9c7237790173469891330af1bf4b0c8ce3e62",
            "marketplace": "BLUR"
        },
        {
            "id": "173474404",
            "contractAddress": "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258",
            "tokenId": "76437",
            "imageUrl": "https://images.blur.io/_blur-prod/0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258/76437-dfd1815672ed7a29",
            "eventType": "SALE",
            "price": {
                "amount": "2",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x327c86581e15d6a72207e655216938ef10c78999",
                "username": None
            },
            "createdAt": "2023-02-23T03:40:23.000Z",
            "transactionHash": "0x64693bbc74fb03dfbff5ddf345a9c7237790173469891330af1bf4b0c8ce3e62",
            "marketplace": "BLUR"
        },
        {
            "id": "173474399",
            "contractAddress": "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258",
            "tokenId": "83614",
            "imageUrl": "https://images.blur.io/_blur-prod/0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258/83614-4ea83c7c29b2be26",
            "eventType": "SALE",
            "price": {
                "amount": "2",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xb8983d041f4e752032f2964b8e095c1f1c61956b",
                "username": None
            },
            "createdAt": "2023-02-23T03:40:23.000Z",
            "transactionHash": "0x64693bbc74fb03dfbff5ddf345a9c7237790173469891330af1bf4b0c8ce3e62",
            "marketplace": "BLUR"
        },
        {
            "id": "173474395",
            "contractAddress": "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258",
            "tokenId": "98331",
            "imageUrl": "https://images.blur.io/_blur-prod/0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258/98331-be7f7052f401cbf0",
            "eventType": "SALE",
            "price": {
                "amount": "2",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xacdaeeb57ff6886fc8e203b9dd4c2b241df89b7a",
                "username": None
            },
            "createdAt": "2023-02-23T03:40:23.000Z",
            "transactionHash": "0x64693bbc74fb03dfbff5ddf345a9c7237790173469891330af1bf4b0c8ce3e62",
            "marketplace": "BLUR"
        },
        {
            "id": "173473378",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "6741",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/6741-c7bbcfa548b9dc88",
            "eventType": "SALE",
            "price": {
                "amount": "15.09",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xa7078ddf23d29e9d6e54e34909cd2ac1b33a67c5",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T03:37:35.000Z",
            "transactionHash": "0x4404aaabc85a378cde7ae2075e31ed4fa172bfb7bdb7459a6ca471e938c2afc9",
            "marketplace": "BLUR"
        },
        {
            "id": "173471780",
            "contractAddress": "0x60e4d786628fea6478f785a6d7e704777c86a7c6",
            "tokenId": "8620",
            "imageUrl": "https://images.blur.io/_blur-prod/0x60e4d786628fea6478f785a6d7e704777c86a7c6/8620-c616ffbb21e8a391",
            "eventType": "SALE",
            "price": {
                "amount": "16.18",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xbb6101475240234e13e815fa4a7f1238ca2fefdf",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T03:32:47.000Z",
            "transactionHash": "0x0428f76c5d6de277f4546e3708323ea3fe9a804fdb12ec831fb9cda63dc6cbd6",
            "marketplace": "BLUR"
        },
        {
            "id": "173465881",
            "contractAddress": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "tokenId": "1747",
            "imageUrl": "https://images.blur.io/_blur-prod/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/1747-1f0d4b37f6c12479",
            "eventType": "SALE",
            "price": {
                "amount": "5.7",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xcb8e41c7e926072e93bc6fca3c39b2b8721ce6b6",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T03:13:35.000Z",
            "transactionHash": "0x03c184fd6b7a1712c6b9a835e83c7d42008494f143acd349d7f06f5e8d4dfa2a",
            "marketplace": "BLUR"
        },
        {
            "id": "173452805",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "5358",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/5358-2242c76e21e4b1a9",
            "eventType": "SALE",
            "price": {
                "amount": "8.09",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xa0f3ec4ac5ecc9f94f05c7110bf1d268e0cb0faf",
                "username": None
            },
            "createdAt": "2023-02-23T02:28:59.000Z",
            "transactionHash": "0x7480688afaed3642f4f96dca53d8fcf159c1aa7039580b478d3aa5579aa9271c",
            "marketplace": "BLUR"
        },
        {
            "id": "173452804",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "6585",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/6585-03dbb65e1b41a736",
            "eventType": "SALE",
            "price": {
                "amount": "8.09",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x76dc804b968a1adde9ee8f9248e91e527cfcc38f",
                "username": None
            },
            "createdAt": "2023-02-23T02:28:59.000Z",
            "transactionHash": "0x7480688afaed3642f4f96dca53d8fcf159c1aa7039580b478d3aa5579aa9271c",
            "marketplace": "BLUR"
        },
        {
            "id": "173452803",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "7546",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/7546-8fdb76b00a8a9af8",
            "eventType": "SALE",
            "price": {
                "amount": "8.09",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x76dc804b968a1adde9ee8f9248e91e527cfcc38f",
                "username": None
            },
            "createdAt": "2023-02-23T02:28:59.000Z",
            "transactionHash": "0x7480688afaed3642f4f96dca53d8fcf159c1aa7039580b478d3aa5579aa9271c",
            "marketplace": "BLUR"
        },
        {
            "id": "173451121",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "6542",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/6542-dd2266cddfd37b02",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x944fdea9d4956ce673c7545862cefccad6ee1b04",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451118",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "5032",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/5032-57fcb6bc6dd5079e",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451114",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "4708",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/4708-5bff8646145fe003",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x900b7ce829e58f284c46db1fa468dde519f485e3",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451112",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "4678",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/4678-87557d16314e81b5",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x944fdea9d4956ce673c7545862cefccad6ee1b04",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451111",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "4178",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/4178-5677b48d7db74482",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451110",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "3648",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/3648-96a8fdbf13d7b081",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451108",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "357",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/357-9dd52fdad66a5636",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451107",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "2394",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/2394-fc8f19aae8ca4d4d",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x944fdea9d4956ce673c7545862cefccad6ee1b04",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451106",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "2234",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/2234-6109a8c396abe4ce",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173451105",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "2146",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/2146-bae7959ddf5a9a08",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x5e1416e0ec35b47a6b7687c5e783e9b98a83dd45",
                "username": None
            },
            "createdAt": "2023-02-23T02:25:11.000Z",
            "transactionHash": "0xa2798017d8d52532e2c764cc6e40ad0a0577c5b3a6c6ca31d2d534a61476e6f2",
            "marketplace": "BLUR"
        },
        {
            "id": "173449892",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "1163",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/1163-9cbfba514f661d12",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xc175f8d59766aa1cc3993ccd969463d26d36ae50",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:22:47.000Z",
            "transactionHash": "0x8439a78ae49e5ce51bae6288bc5c1c8c115fd20b30f2ae42afb36169e00c4f2a",
            "marketplace": "BLUR"
        },
        {
            "id": "173449817",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "9418",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/9418-94d8725f6d0db821",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:22:35.000Z",
            "transactionHash": "0x457666de2932bfec64558db4c10124911145c92173719726a857b435b9ab687a",
            "marketplace": "BLUR"
        },
        {
            "id": "173449814",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "7002",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/7002-0df0a78048bba658",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:22:35.000Z",
            "transactionHash": "0x457666de2932bfec64558db4c10124911145c92173719726a857b435b9ab687a",
            "marketplace": "BLUR"
        },
        {
            "id": "173449594",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "8529",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/8529-6ef0f964771dd66e",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4ce0f96c459df322df68f393569549d5a54a1929",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:22:11.000Z",
            "transactionHash": "0x36514935b60c6c79aff615df15dac7156a6f9a17907463d873dc92e5183d5ee6",
            "marketplace": "BLUR"
        },
        {
            "id": "173448958",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "9376",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/9376-f44251d4954b0584",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448952",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "8250",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/8250-bc44eb4e203bc265",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448937",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "5963",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/5963-e288664846c1370a",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448936",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "5955",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/5955-86d8fbeb7589c17b",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448934",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "5936",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/5936-9b5d1bd9dcebbd48",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448929",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "4427",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/4427-0357dbefa7d6dcea",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448926",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "4175",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/4175-47e719f36f93e948",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448923",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "3908",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/3908-7f320b2e5f20aa27",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173448920",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "3759",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/3759-29f3d427a038276b",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x4d417dfe10a8ebe24bed38c3861e9acd0d9ef717",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:20:59.000Z",
            "transactionHash": "0x35fe0596af2342ca68c40ebcda4c1a17db87ceb0118117a5d7c9862578400ad0",
            "marketplace": "BLUR"
        },
        {
            "id": "173443577",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "4548",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/4548-fc12cf0beda981be",
            "eventType": "SALE",
            "price": {
                "amount": "5.07",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x14ee554c0ae6d541c9fae9f8ce6cd28a1bfc8c0e",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T02:11:59.000Z",
            "transactionHash": "0x9d26c86bcbad5b7ccff74bba5089064bcdd70cde6192f8b7fdb87da605871872",
            "marketplace": "BLUR"
        },
        {
            "id": "173433459",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "9168",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/9168-bcb57ecbd49a14cc",
            "eventType": "SALE",
            "price": {
                "amount": "15.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xcbb0fe555f61d23427740984325b4583a4a34c82",
                "username": None
            },
            "createdAt": "2023-02-23T02:01:35.000Z",
            "transactionHash": "0x14cc5447c10c307c6a583aa2ffddd8a0014c326fdc4e37aee4e48edd693767e5",
            "marketplace": "BLUR"
        },
        {
            "id": "173433455",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "1928",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/1928-38fc8c187ac3c177",
            "eventType": "SALE",
            "price": {
                "amount": "15.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0xa7078ddf23d29e9d6e54e34909cd2ac1b33a67c5",
                "username": None
            },
            "createdAt": "2023-02-23T02:01:35.000Z",
            "transactionHash": "0x14cc5447c10c307c6a583aa2ffddd8a0014c326fdc4e37aee4e48edd693767e5",
            "marketplace": "BLUR"
        },
        {
            "id": "173422610",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "378",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/378-8f2729a019212b9b",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T01:31:23.000Z",
            "transactionHash": "0xcb2513abb462e61e0fc9a4f16e6d66102f35ed1a1d158230f2f352a43d03cb01",
            "marketplace": "BLUR"
        },
        {
            "id": "173422604",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "443",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/443-4c20931109249f06",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9c81522976f5eebba38c60d36c63facb5e9e9f23",
                "username": None
            },
            "createdAt": "2023-02-23T01:31:23.000Z",
            "transactionHash": "0xcb2513abb462e61e0fc9a4f16e6d66102f35ed1a1d158230f2f352a43d03cb01",
            "marketplace": "BLUR"
        },
        {
            "id": "173414827",
            "contractAddress": "0xb852c6b5892256c264cc2c888ea462189154d8d7",
            "tokenId": "506",
            "imageUrl": "https://images.blur.io/_blur-prod/0xb852c6b5892256c264cc2c888ea462189154d8d7/506-7cbf9bbc8533ea17",
            "eventType": "SALE",
            "price": {
                "amount": "1.22",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x041c36713d3142b520aed45cbd3ffc5b91311eef",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T01:09:47.000Z",
            "transactionHash": "0xafcdaf518890b5da8fe1be6e63289a522070f1fc3855d40be1f8b50df9477329",
            "marketplace": "BLUR"
        },
        {
            "id": "173409560",
            "contractAddress": "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
            "tokenId": "6542",
            "imageUrl": "https://images.blur.io/_blur-prod/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/6542-dd2266cddfd37b02",
            "eventType": "SALE",
            "price": {
                "amount": "8.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x89cc7317dafb318c71b3a721c5f98fb08ba45799",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T01:05:47.000Z",
            "transactionHash": "0xd5b915ee6eacb56870d3cea31b394f68aeec59719eb65f54853a74e844f185e0",
            "marketplace": "BLUR"
        },
        {
            "id": "173405173",
            "contractAddress": "0x1792a96e5668ad7c167ab804a100ce42395ce54d",
            "tokenId": "9707",
            "imageUrl": "https://images.blur.io/_blur-prod/0x1792a96e5668ad7c167ab804a100ce42395ce54d/9707-5af49708270a35f4",
            "eventType": "SALE",
            "price": {
                "amount": "1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xa08a472b2983b5485442b0d3a7ba7d4b2ca8ca9a",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T00:50:47.000Z",
            "transactionHash": "0x9948f00550790790a6347339b3fe13296c517ea8365d3d4e80c70c2e573816ef",
            "marketplace": "BLUR"
        },
        {
            "id": "173402053",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "1928",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/1928-38fc8c187ac3c177",
            "eventType": "SALE",
            "price": {
                "amount": "15.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xa7078ddf23d29e9d6e54e34909cd2ac1b33a67c5",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T00:40:59.000Z",
            "transactionHash": "0x3614332f7d338d8c915796ebed737e8560ccdc4b8ebf7dc8f5381f960cce766b",
            "marketplace": "BLUR"
        },
        {
            "id": "173402047",
            "contractAddress": "0xed5af388653567af2f388e6224dc7c4b3241c544",
            "tokenId": "9168",
            "imageUrl": "https://images.blur.io/_blur-prod/0xed5af388653567af2f388e6224dc7c4b3241c544/9168-bcb57ecbd49a14cc",
            "eventType": "SALE",
            "price": {
                "amount": "15.1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0xa7078ddf23d29e9d6e54e34909cd2ac1b33a67c5",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T00:40:59.000Z",
            "transactionHash": "0x3614332f7d338d8c915796ebed737e8560ccdc4b8ebf7dc8f5381f960cce766b",
            "marketplace": "BLUR"
        },
        {
            "id": "173399948",
            "contractAddress": "0x1792a96e5668ad7c167ab804a100ce42395ce54d",
            "tokenId": "42",
            "imageUrl": "https://images.blur.io/_blur-prod/0x1792a96e5668ad7c167ab804a100ce42395ce54d/42-d177524e5822c565",
            "eventType": "SALE",
            "price": {
                "amount": "1",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x8909e6f8adfbdf105625bc444b541a230103d98e",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T00:33:35.000Z",
            "transactionHash": "0xcd7b259b53a05bb9dc489deadd3a2ec19cf0936b6c30a453436666a1c8e7ca32",
            "marketplace": "BLUR"
        },
        {
            "id": "173396396",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "1933",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/1933-8309c3680a53f211",
            "eventType": "SALE",
            "price": {
                "amount": "5.08",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x9b633acb3996147705f923b37fb8ee8755681389",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T00:21:23.000Z",
            "transactionHash": "0x8750198792906ea4611ead580d904721d989726e7d8079b2672a35b755be7fec",
            "marketplace": "BLUR"
        },
        {
            "id": "173396393",
            "contractAddress": "0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",
            "tokenId": "18504",
            "imageUrl": "https://images.blur.io/_blur-prod/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/18504-a6a4b7d10cc83b67",
            "eventType": "SALE",
            "price": {
                "amount": "5.08",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x9b633acb3996147705f923b37fb8ee8755681389",
                "username": None
            },
            "toTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "createdAt": "2023-02-23T00:21:23.000Z",
            "transactionHash": "0x8750198792906ea4611ead580d904721d989726e7d8079b2672a35b755be7fec",
            "marketplace": "BLUR"
        },
        {
            "id": "173388751",
            "contractAddress": "0x23581767a106ae21c074b2276d25e5c3e136a68b",
            "tokenId": "8566",
            "imageUrl": "https://images.blur.io/_blur-prod/0x23581767a106ae21c074b2276d25e5c3e136a68b/8566-fd8e6847998f12d3",
            "eventType": "SALE",
            "price": {
                "amount": "6.75",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "createdAt": "2023-02-22T23:56:47.000Z",
            "transactionHash": "0xf3fb315c541673ecca9128112daeafb5c093ffeb778c5fa3d8ec9086dce86467",
            "marketplace": "BLUR"
        },
        {
            "id": "173388750",
            "contractAddress": "0x23581767a106ae21c074b2276d25e5c3e136a68b",
            "tokenId": "7905",
            "imageUrl": "https://images.blur.io/_blur-prod/0x23581767a106ae21c074b2276d25e5c3e136a68b/7905-5fc50c389aca4a99",
            "eventType": "SALE",
            "price": {
                "amount": "6.75",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "createdAt": "2023-02-22T23:56:47.000Z",
            "transactionHash": "0xf3fb315c541673ecca9128112daeafb5c093ffeb778c5fa3d8ec9086dce86467",
            "marketplace": "BLUR"
        },
        {
            "id": "173388749",
            "contractAddress": "0x23581767a106ae21c074b2276d25e5c3e136a68b",
            "tokenId": "1002",
            "imageUrl": "https://images.blur.io/_blur-prod/0x23581767a106ae21c074b2276d25e5c3e136a68b/1002-df3c9e842ad23343",
            "eventType": "SALE",
            "price": {
                "amount": "6.75",
                "unit": "ETH"
            },
            "fromTrader": {
                "address": "0x0d01ffcd7c1a17eb87718470ca2f227097234cd5",
                "username": None
            },
            "toTrader": {
                "address": "0x9a68cb9c15a24da0c3d9852950aa6da0e3bf5622",
                "username": None
            },
            "createdAt": "2023-02-22T23:56:47.000Z",
            "transactionHash": "0xf3fb315c541673ecca9128112daeafb5c093ffeb778c5fa3d8ec9086dce86467",
            "marketplace": "BLUR"
        }
    ],
    "cursor": "eyJiZWZvcmVEYXRlIjoiMjAyMy0wMi0yMlQyMzo1Njo0Ny4wMDBaIiwiaWQiOiIxNzMzODg3NDkifQ=="
}


data = _fetch_data()

items = data.get("activityItems")
sell = [x for x in items if x['eventType'] == 'SALE']
buy = [x for x in items if x['eventType'] == 'BUY']

rows = []

_tasks = _get_tasks()
buy, sell = 1, -1

today = datetime.today()
for x in items:
    type_ = sell if x['fromTrader']['address'] == user else buy
    if x['eventType'] == 'BUY':
        type_ = -type_

    event_type = 'BUY' if type_ == buy else 'SELL'
    collection_name = _tasks.get(x['contractAddress'].lower(), "-")
    gmt_time = datetime.strptime(x['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
    gmt_time = gmt_time.replace(tzinfo=pytz.utc)
    local_time = gmt_time.astimezone(pytz.timezone("Asia/Shanghai"))
    print(local_time)
    rows.append(dict(
        eventType=event_type,
        collection_name=collection_name,
        item=x.get("tokenId"),
        amount=x['price']['amount'],
        time=local_time,
        user=user,
    ))

st.table(rows)
