# 好看视频爬取

爬取好看视频,主要爬取三方面的信息:

- 刷新视频的基本信息
- 刷新视频的作者信息
- 刷新视频的评论信息(评论信息中包含了视频的评论信息和视频的属性信息)

------

1. 首先,获取刷新视频的基本信息,直接调用requests请求传递的url和param即可得到json串信息
   - url:[https://sv.baidu.com/haokan/api?cmd=feed&log=vhk&tn=1022344h&ctn=1022344h&imei=161353027727941&cuid=2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161&bdboxcuid=&os=android&osbranch=a0&ua=810_1440_270&ut=SM-G9550_6.0.1_23_samsung&apiv=4.6.0.0&appv=500011&version=5.0.1.10&life=1561077145&clife=1561077146&hid=2C28F27B86CB861893B8D26F24835FEB&imsi=0&network=1&location={%22prov%22:%22%22,%22city%22:%22%22,%22county%22:%22%22,%22street%22:%22%22,%22latitude%22:39.911017,%22longitude%22:116.413562}&sids=2498_1-2536_2-2540_2-2551_2-2578_2-2587_1-2601_2-2603_2-2617_1-2618_2-2627_2-2629_2-2635_1-2673_4-2680_1-2681_3-2685_2-2719_4-2721_1-2723_3-2727_1-2732_3-2739_2-2740_1-2744_2-2747_1-2749_2-2755_7-2758_1-2768_1-2772_2-2777_3-2796_2-2803_2-2807_1-2810_2-2813_1-2814_2-2816_2-2822_1&young_mode=0](https://sv.baidu.com/haokan/api?cmd=feed&log=vhk&tn=1022344h&ctn=1022344h&imei=161353027727941&cuid=2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161&bdboxcuid=&os=android&osbranch=a0&ua=810_1440_270&ut=SM-G9550_6.0.1_23_samsung&apiv=4.6.0.0&appv=500011&version=5.0.1.10&life=1561077145&clife=1561077146&hid=2C28F27B86CB861893B8D26F24835FEB&imsi=0&network=1&location={%22prov%22:%22%22,%22city%22:%22%22,%22county%22:%22%22,%22street%22:%22%22,%22latitude%22:39.911017,%22longitude%22:116.413562}&sids=2498_1-2536_2-2540_2-2551_2-2578_2-2587_1-2601_2-2603_2-2617_1-2618_2-2627_2-2629_2-2635_1-2673_4-2680_1-2681_3-2685_2-2719_4-2721_1-2723_3-2727_1-2732_3-2739_2-2740_1-2744_2-2747_1-2749_2-2755_7-2758_1-2768_1-2772_2-2777_3-2796_2-2803_2-2807_1-2810_2-2813_1-2814_2-2816_2-2822_1&young_mode=0)
   - param:{'feed':'adparam={"ac":"1","ver":"5.0.1.10","mod":"SM-G9550","ov":"6.0.1","imei":"161353027727941","cuid":"2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161","fmt":"json","apna":"com.baidu.haokan","eid":"2498_1,2536_2,2540_2,2551_2,2578_2,2587_1,2601_2,2603_2,2617_1,2618_2,2627_2,2629_2,2635_1,2673_4,2680_1,2681_3,2685_2,2719_4,2721_1,2723_3,2727_1,2732_3,2739_2,2740_1,2744_2,2747_1,2749_2,2755_7,2758_1,2768_1,2772_2,2777_3,2796_2,2803_2,2807_1,2810_2,2813_1,2814_2,2816_2,2822_1","ot":"2","ct":"2","nt":"1","network":"1","android_id":"380d1d4484577d5a","ua":"1439_768_android_5.0.1.10_270","install_timestamp":"1561077145","iad":65537,"from":"1022344h","cfrom":"1022344h","videomute":"0","apinfo":"iLrk5uTn4efk4ebj5eK5v-fnpuPn5OPi5eXq6uDr6uL0sb2__LCzu7an_LqzvbmzvPTj5OPh5-Hi4OXl4OXr5uPSD_..%7Cqloc2","ext":"[]","latitude":"39.911017","longitude":"116.413562","pid":"1510566610070","tabn":"推荐","tabid":"recommend","flr":"-1","fc":"4","ft":"4","pre_feed_count":4,"feed_total":4}&feed&rn=8&sessionid=1561077881974&tag=recommend&refreshtype=0&refreshcount=3&card={"refresh_count":3,"card_last_showtime":0,"card_show_times":0}&gr_param=[{"id":"12478756584072194811","show":0,"clk":0,"show_ts":0,"clk_ts":0,"target":"1"},{"id":"5977452998647909643","show":1,"clk":0,"show_ts":1561079884041,"clk_ts":0,"target":"1"},{"id":"13559005133391516128","show":1,"clk":0,"show_ts":1561079883966,"clk_ts":0,"target":"1"},{"id":"6350555639266783060","show":1,"clk":0,"show_ts":1561079883763,"clk_ts":0,"target":"1"}]&shuaxin_id=1561079894484'}

2. 提取出刷新视频的json串中的appid，vid，playcntText字段信息，因为下边的步骤需要这些字段的数据

3. 然后,获取视频作者信息。
   1. 先通过requests请求获取每次刷新的作者信息的json串。

      - url='[https://sv.baidu.com/haokan/api?log=vhk&tn=1008621v&ctn=1008621v&stn=&imei=865166024859905&cuid=13115066E98701E9CFB0E994EE32D79B|509958420661568&os=android&osbranch=a0&ua=1600_900_240&ut=m1%20metal_5.1.1_22_meizu&apiv=3.9.0.0&appv=182&version=3.9.0.10&life=1561037997&clife=1561037997&hid=445B1DAB6C652531F861D576CEC32A06&imsi=0&network=1&sids=2125_2-2212_2-2436_2-2515_4-2540_1-2578_1-2585_2-2601_1-2627_1-2629_2-2635_1-2658_2-2679_2-2697_1-2719_2-2724_1-2731_1-2732_1-2735_1-2739_1-2740_2-2743_1-2751_3-2755_5-2768_1-2770_4-2772_1-2775_4-2776_2-2783_2-2784_1-2786_3-2796_2-2797_2-2803_2-2807_1-2808_2-2814_2-2801_2](https://sv.baidu.com/haokan/api?log=vhk&tn=1008621v&ctn=1008621v&stn=&imei=865166024859905&cuid=13115066E98701E9CFB0E994EE32D79B|509958420661568&os=android&osbranch=a0&ua=1600_900_240&ut=m1%20metal_5.1.1_22_meizu&apiv=3.9.0.0&appv=182&version=3.9.0.10&life=1561037997&clife=1561037997&hid=445B1DAB6C652531F861D576CEC32A06&imsi=0&network=1&sids=2125_2-2212_2-2436_2-2515_4-2540_1-2578_1-2585_2-2601_1-2627_1-2629_2-2635_1-2658_2-2679_2-2697_1-2719_2-2724_1-2731_1-2732_1-2735_1-2739_1-2740_2-2743_1-2751_3-2755_5-2768_1-2770_4-2772_1-2775_4-2776_2-2783_2-2784_1-2786_3-2796_2-2797_2-2803_2-2807_1-2808_2-2814_2-2801_2)'
      - headers={
                        'Charset': 'UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; m1 metal Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 haokan/3.9.0.10 (Baidu; P1 5.1.1)/uziem_22_1.1.5_latem+1m/1008621v/13115066E98701E9CFB0E994EE32D79B%7C509958420661568/1/3.9.0.10/182/1',
                        'XRAY-TRACEID': 'f3c7171d-10ca-4c10-95d9-8f79f55387f6',
                        'XRAY-REQ-FUNC-ST-DNS': 'okHttp;1561088775448;0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Content-Length': '116',
                        'Host': 'sv.baidu.com',
                        'Connection': 'Keep-Alive',
                        'Accept-Encoding': 'gzip',
                        'Cookie': 'BAIDUID=04F1A17388629FF0CB343AD1D1EC1C1D:FG=1; BAIDUCUID=guvSi_aj2ilcPBipguSNt085HilOO-ifli2ailu0-aiTavtgja-_i_aj28gFa2fHA'
                        }
      - param={'baijia/listall':'method=get&app_id={}&_skip=1&_limit=20&_timg_cover=100,150,1000'}

      param部分的app_id关键字属性值不同，这个属性是作者的id值，根据这个属性即可找到作者的详细信息，这个属性值通过刷新页面的json串获取的到。

   2. 由于每次刷新都会刷出不同数量的视频，也就刷新出了相应数量的作者，所以需要通过循环遍历每个作者，而且每个作者里面有很多视频，也需要通过循环遍历每个视频，获取视频信息。

4. 最后爬取视频的评论和视频属性信息(包括视频的发布日期,视频时长,视频占用内存大小,视频点赞量等信息)。刷新的url和视频评论的url中只有cmd属性值不同，其他都一样，因此直接替换刷新的url的cmd属性值即可，将cmd='feed'替换为cmd='comment/getreply'.

   - url：[https://sv.baidu.com/haokan/api?cmd=comment/getreply&log=vhk&tn=1022344h&ctn=1022344h&imei=161353027727941&cuid=2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161&bdboxcuid=&os=android&osbranch=a0&ua=810_1440_270&ut=SM-G9550_6.0.1_23_samsung&apiv=4.6.0.0&appv=500011&version=5.0.1.10&life=1561077145&clife=1561077146&hid=2C28F27B86CB861893B8D26F24835FEB&imsi=0&network=1&location={%22prov%22:%22%22,%22city%22:%22%22,%22county%22:%22%22,%22street%22:%22%22,%22latitude%22:39.911017,%22longitude%22:116.413562}&sids=2498_1-2536_2-2540_2-2551_2-2578_2-2587_1-2601_2-2603_2-2617_1-2618_2-2627_2-2629_2-2635_1-2673_4-2680_1-2681_3-2685_2-2719_4-2721_1-2723_3-2727_1-2732_3-2739_2-2740_1-2744_2-2747_1-2749_2-2755_7-2758_1-2768_1-2772_2-2777_3-2796_2-2803_2-2807_1-2810_2-2813_1-2814_2-2816_2-2822_1&young_mode=0](https://sv.baidu.com/haokan/api?cmd=feed&log=vhk&tn=1022344h&ctn=1022344h&imei=161353027727941&cuid=2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161&bdboxcuid=&os=android&osbranch=a0&ua=810_1440_270&ut=SM-G9550_6.0.1_23_samsung&apiv=4.6.0.0&appv=500011&version=5.0.1.10&life=1561077145&clife=1561077146&hid=2C28F27B86CB861893B8D26F24835FEB&imsi=0&network=1&location={%22prov%22:%22%22,%22city%22:%22%22,%22county%22:%22%22,%22street%22:%22%22,%22latitude%22:39.911017,%22longitude%22:116.413562}&sids=2498_1-2536_2-2540_2-2551_2-2578_2-2587_1-2601_2-2603_2-2617_1-2618_2-2627_2-2629_2-2635_1-2673_4-2680_1-2681_3-2685_2-2719_4-2721_1-2723_3-2727_1-2732_3-2739_2-2740_1-2744_2-2747_1-2749_2-2755_7-2758_1-2768_1-2772_2-2777_3-2796_2-2803_2-2807_1-2810_2-2813_1-2814_2-2816_2-2822_1&young_mode=0)
   -  comment_data={'video/detail':'method=get&url_key='+vid+'&log_param_source=bjh&vid='+vid+'&type=video&adparam={"screen_type":0,"pid":"1513598844404","ac":"1","install_timestamp":"1561077145","ext":"[{\"k\":\"video_vid\",\"v\":\"'+vid+'\"},{\"k\":\"video_title\",\"v\":\"'+vtitle+'\"},{\"k\":\"iad\",\"v\":\"65537\"}]","ver":"5.0.1.10","mod":"SM-G9550","ov":"6.0.1","imei":"161353027727941","cuid":"2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161","baiduId":"592A61505CA70B187B29FD1BB3298492:FG=1","fmt":"json","apna":"com.baidu.haokan","eid":"2498_1,2536_2,2540_2,2551_2,2578_2,2587_1,2601_2,2603_2,2617_1,2618_2,2627_2,2629_2,2635_1,2673_4,2680_1,2681_3,2685_2,2719_4,2721_1,2723_3,2727_1,2732_3,2739_2,2740_1,2744_2,2747_1,2749_2,2755_7,2758_1,2768_1,2772_2,2777_3,2796_2,2803_2,2807_1,2810_2,2813_1,2814_2,2816_2,2822_1","ot":"2","ct":"2","nt":"1","android_id":"380d1d4484577d5a","iad":65537,"ua":"1439_768_android_5.0.1.10_270","apinfo":"iLrk5uTn4efk4ebj5eK5v-fnpuPn5OPi5eXq6uDr6uL0sb2__LCzu7an_LqzvbmzvPTj5OPh5-Hi4OXl4OXr5uPSD_..%7Cqloc2","latitude":"39.911017","longitude":"116.413562","source":"videolanding"}',                      'comment/getreply':'method=get&url_key='+vid+'&pn=1&rn=10&child_rn=2&need_ainfo=0&type=0&vid='+vid
                            }

   url下面的两个参数即为requests请求要传递的参数,所有的视频评论的url所有格式都一样，只是6个关键字段不同，第一个参数的4个关键字和第二个参数的2个关键字，分别为：url_key,vid,"ext":"[{\"k\":\"video_vid\",\"v\":\"变量''\"},{\"k\":\"video_title\",\"v\":\"'+变量+'\"},url_key,vid，以上6个关键字，只需要用到刷新页面获取到的json串中的vid和title即可。

5. 将项目部署到Flask服务器上面运行。
