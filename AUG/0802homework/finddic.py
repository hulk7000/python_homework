from dic import longdic
answer="https://manifest.googlevideo.com/api/manifest/hls_variant/expire/1754172520/ei/CDiOaNO-B5HfsfIP1bjTYQ/ip/47.147.230.223/id/56afa8352e6fc6e9/source/youtube/requiressl/yes/xpc/EgVo2aDSNQ%3D%3D/playback_host/rr2---sn-a5mekn6k.googlevideo.com/met/1754150920%2C/mh/zq/mm/31%2C26/mn/sn-a5mekn6k%2Csn-vgqsrned/ms/au%2Conr/mv/m/mvi/2/pl/13/rms/au%2Cau/tx/51539854/txs/51539853%2C51539854%2C51539855/hfr/1/demuxed/1/tts_caps/1/maudio/1/initcwndbps/3728750/bui/AY1jyLNSMqJaSosf_TleRpXV2rHkdpt38BrB6NF9S6ST2RqOymEHzb5h4oxLPLzgpeH7O7ye1_sCvCpo/spc/l3OVKYlY7kkRGjOUng-poXOfPPQvMqW0Fdd6tb4xL-d9Wi06-6XLMJS21jHpcm7v/vprv/1/go/1/rqh/5/mt/1754150508/fvip/1/nvgoi/1/short_key/1/ncsapi/1/keepalive/yes/dover/13/itag/0/playlist_type/DVR/sparams/expire%2Cei%2Cip%2Cid%2Csource%2Crequiressl%2Cxpc%2Ctx%2Ctxs%2Chfr%2Cdemuxed%2Ctts_caps%2Cmaudio%2Cbui%2Cspc%2Cvprv%2Cgo%2Crqh%2Citag%2Cplaylist_type/sig/AJfQdSswRQIgTkTk7ktBXRMGgcW5OINnRX4P9Rhdk95eVWazqsbv4okCIQCf5DFgDWm3SsHZJG6TP_unQnsddAGhZftU3uHrYhZiJQ%3D%3D/lsparams/playback_host%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps/lsig/APaTxxMwRQIhAMdNRBI94xpj4M-jwrwfWN9cyw9KhS6-9gwxfZoGDEk2AiBCS6TbY_a1P3uqRfPOfOK3cU_7ou0Od--5QcvPBmIuEw%3D%3D/file/index.m3u8"
#  row 543
a = longdic.get('formats')
print(a)
for i in a:
    if i.get("format_id") == "232":
        print(i.get('manifest_url'))
        z = i.get('manifest_url')
if z == answer:
    print("you can play")
