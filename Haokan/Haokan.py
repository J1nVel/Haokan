# -*- coding: utf-8 -*-

import requests
import json
class Haokan(object):
    def __init__(self):
    #    feed
    #    comment/getreply
        self.url1='https://sv.baidu.com/haokan/api?cmd='
        self.url2='&log=vhk&tn=1022344h&ctn=1022344h&imei=161353027727941&cuid=2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161&bdboxcuid=&os=android&osbranch=a0&ua=810_1440_270&ut=SM-G9550_6.0.1_23_samsung&apiv=4.6.0.0&appv=500011&version=5.0.1.10&life=1561077145&clife=1561077146&hid=2C28F27B86CB861893B8D26F24835FEB&imsi=0&network=1&location={%22prov%22:%22%22,%22city%22:%22%22,%22county%22:%22%22,%22street%22:%22%22,%22latitude%22:39.911017,%22longitude%22:116.413562}&sids=2498_1-2536_2-2540_2-2551_2-2578_2-2587_1-2601_2-2603_2-2617_1-2618_2-2627_2-2629_2-2635_1-2673_4-2680_1-2681_3-2685_2-2719_4-2721_1-2723_3-2727_1-2732_3-2739_2-2740_1-2744_2-2747_1-2749_2-2755_7-2758_1-2768_1-2772_2-2777_3-2796_2-2803_2-2807_1-2810_2-2813_1-2814_2-2816_2-2822_1&young_mode=0'
        self.flush_data={'feed':'adparam={"ac":"1","ver":"5.0.1.10","mod":"SM-G9550","ov":"6.0.1","imei":"161353027727941","cuid":"2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161","fmt":"json","apna":"com.baidu.haokan","eid":"2498_1,2536_2,2540_2,2551_2,2578_2,2587_1,2601_2,2603_2,2617_1,2618_2,2627_2,2629_2,2635_1,2673_4,2680_1,2681_3,2685_2,2719_4,2721_1,2723_3,2727_1,2732_3,2739_2,2740_1,2744_2,2747_1,2749_2,2755_7,2758_1,2768_1,2772_2,2777_3,2796_2,2803_2,2807_1,2810_2,2813_1,2814_2,2816_2,2822_1","ot":"2","ct":"2","nt":"1","network":"1","android_id":"380d1d4484577d5a","ua":"1439_768_android_5.0.1.10_270","install_timestamp":"1561077145","iad":65537,"from":"1022344h","cfrom":"1022344h","videomute":"0","apinfo":"iLrk5uTn4efk4ebj5eK5v-fnpuPn5OPi5eXq6uDr6uL0sb2__LCzu7an_LqzvbmzvPTj5OPh5-Hi4OXl4OXr5uPSD_..%7Cqloc2","ext":"[]","latitude":"39.911017","longitude":"116.413562","pid":"1510566610070","tabn":"推荐","tabid":"recommend","flr":"-1","fc":"4","ft":"4","pre_feed_count":4,"feed_total":4}&feed&rn=8&sessionid=1561077881974&tag=recommend&refreshtype=0&refreshcount=3&card={"refresh_count":3,"card_last_showtime":0,"card_show_times":0}&gr_param=[{"id":"12478756584072194811","show":0,"clk":0,"show_ts":0,"clk_ts":0,"target":"1"},{"id":"5977452998647909643","show":1,"clk":0,"show_ts":1561079884041,"clk_ts":0,"target":"1"},{"id":"13559005133391516128","show":1,"clk":0,"show_ts":1561079883966,"clk_ts":0,"target":"1"},{"id":"6350555639266783060","show":1,"clk":0,"show_ts":1561079883763,"clk_ts":0,"target":"1"}]&shuaxin_id=1561079894484'}
        self.user_param={'baijia/listall':'method=get&app_id={}&_skip=1&_limit=20&_timg_cover=100,150,1000'}
        self.userinfo_ls=[]
        self.comment_ls=[]
        self.videoinfo_ls=[]
        self.userinfo_dic={}
        self.comment_and_videoinfo_ls=[]
        self.headers={
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
        
    '''首页刷新页面'''
    def flush(self):
        flush_url=self.url1+'feed'+self.url2
        flush_resp=requests.post(flush_url,data=self.flush_data)
        flush_resp.encoding='utf-8'
        flush_rst=json.loads(flush_resp.text)
        return flush_rst
    
    '''首页刷新字段信息提取'''
    def flush_parse(self):
        randomResource = self.flush()
        random =  randomResource['feed']['data']['list']
        randomDict = {}
        for i in random:
            randomDict[i['content']['title']]={
                'appid':i['content']['appid'],'author':i['content']['author'],'author_icon':i['content']['author_icon'],
                'vid':i['content']['vid'],'title':i['content']['title'],'praiseNum':i['content']['praiseNum'],'comment_cnt':i['content']['comment_cnt'],
                'playcntText':i['content']['playcntText'],'video_short_url':i['content']['video_short_url']
            }
        return randomDict 
    
    '''评论和视频信息'''
    def comment_and_videoinfo(self):
        comment_url=self.url1+'comment/getreply'+self.url2
        flush_rst=self.flush()
        for i in range(len(flush_rst['feed']['data']['list'])):
            vid=flush_rst['feed']['data']['list'][i]['content']['vid']
            vtitle=flush_rst['feed']['data']['list'][i]['content']['title']
            comment_data={'video/detail':'method=get&url_key='+vid+'&log_param_source=bjh&vid='+vid+'&type=video&adparam={"screen_type":0,"pid":"1513598844404","ac":"1","install_timestamp":"1561077145","ext":"[{\"k\":\"video_vid\",\"v\":\"'+vid+'\"},{\"k\":\"video_title\",\"v\":\"'+vtitle+'\"},{\"k\":\"iad\",\"v\":\"65537\"}]","ver":"5.0.1.10","mod":"SM-G9550","ov":"6.0.1","imei":"161353027727941","cuid":"2E4C6CEB54F2B9BEB59ADA449D1B0BB5|149727720353161","baiduId":"592A61505CA70B187B29FD1BB3298492:FG=1","fmt":"json","apna":"com.baidu.haokan","eid":"2498_1,2536_2,2540_2,2551_2,2578_2,2587_1,2601_2,2603_2,2617_1,2618_2,2627_2,2629_2,2635_1,2673_4,2680_1,2681_3,2685_2,2719_4,2721_1,2723_3,2727_1,2732_3,2739_2,2740_1,2744_2,2747_1,2749_2,2755_7,2758_1,2768_1,2772_2,2777_3,2796_2,2803_2,2807_1,2810_2,2813_1,2814_2,2816_2,2822_1","ot":"2","ct":"2","nt":"1","android_id":"380d1d4484577d5a","iad":65537,"ua":"1439_768_android_5.0.1.10_270","apinfo":"iLrk5uTn4efk4ebj5eK5v-fnpuPn5OPi5eXq6uDr6uL0sb2__LCzu7an_LqzvbmzvPTj5OPh5-Hi4OXl4OXr5uPSD_..%7Cqloc2","latitude":"39.911017","longitude":"116.413562","source":"videolanding"}',
                      'comment/getreply':'method=get&url_key='+vid+'&pn=1&rn=10&child_rn=2&need_ainfo=0&type=0&vid='+vid
                      }
            comment_resp=requests.post(comment_url,data=comment_data)#,headers=comment_headers
            comment_resp.encoding='utf-8'
            comment_rst=json.loads(comment_resp.text)
            self.comment_and_videoinfo_ls.append(comment_rst)#每个视频请求返回的json串添加到列表中
            
#            video_comment=comment_rst['comment/getreply']
#            video_info=comment_rst['video/detail']
#            self.comment_ls.append(video_comment)
#            self.videoinfo_ls.append(video_info)
            
#            '''视频信息''' 
#            for i in range(len(video_info['data']['list'])):
#                '''视频播放地址'''
#                video_addr_resp=requests.get(flush_rst['feed']['data']['list'][1]['content']['video_short_url'])
#                video_addr_resp.encoding='utf-8'
#                html=HTML(video_addr_resp.text)
#                html.xpath('//*[@type="video/mp4"]/@src')[0]
#                '''视频标题'''
#                self.video_title=video_info['data']['title']
#                '''播放地址'''
#                self.video_src=video_info['data']['playcntText']
#                '''发布时间'''
#                self.publish_time=video_info['data']['publishTimeText']
#                '''视频点赞量'''
#                self.like_num=video_info['data']['like_num']
#                '''作者头像'''
#                self.author_icon=video_info['data']['author_icon']
#                '''作者名称'''
#                self.author=video_info['data']['author']
#                '''作者描述'''
#                self.author_desc=video_info['data']['author_desc']
#                '''作者粉丝量'''
#                self.fans_count=video_info['data']['fansCntText']
#            
#            '''评论信息'''
#            for i in range(len(video_comment['data']['list'])):
#                '''评论用户头像'''
#                self.comment_user_icon=video_info['data']['list'][i]['avatar']
#                '''评论用户名字'''
#                self.comment_user_name=video_info['data']['list'][i]['uname']
#                '''评论'''
#                self.comment_info=video_info['data']['list'][i]['content']
#                '''评论日期'''
#                self.comment_time=video_info['data']['list'][i]['create_time_text']
#                '''回复用户名'''
#                self.comment_reply_username=video_info['data']['list'][i]['reply_list']['uname']
#                '''回复'''
#                self.comment_reply=video_info['data']['list'][i]['reply_list']['content']
#                '''评论点赞量'''
#                self.comment_like_num=video_info['data']['list'][i]['like_count']
#            '''评论总数量'''
#            self.comment_count=video_info['data']['comment_count']
        return self.comment_and_videoinfo_ls
#    def videoinfo(self):
#        comment_and_videoinfo_ls=self.comment_and_videoinfo()
#        return [comment_and_videoinfo_ls[i]['video/detail'] for i in range(len(comment_and_videoinfo_ls))]
#    def comment(self):
#        comment_and_videoinfo_ls=self.comment_and_videoinfo()
#        return [comment_and_videoinfo_ls[i]['comment/getreply'] for i in range(len(comment_and_videoinfo_ls))]

    '''用户信息'''
    def userinfo(self):
        '''返回刷新的视频'''
        flush_dict= self.recommendParse()
        url='https://sv.baidu.com/haokan/api?log=vhk&tn=1008621v&ctn=1008621v&stn=&imei=865166024859905&cuid=13115066E98701E9CFB0E994EE32D79B|509958420661568&os=android&osbranch=a0&ua=1600_900_240&ut=m1%20metal_5.1.1_22_meizu&apiv=3.9.0.0&appv=182&version=3.9.0.10&life=1561037997&clife=1561037997&hid=445B1DAB6C652531F861D576CEC32A06&imsi=0&network=1&sids=2125_2-2212_2-2436_2-2515_4-2540_1-2578_1-2585_2-2601_1-2627_1-2629_2-2635_1-2658_2-2679_2-2697_1-2719_2-2724_1-2731_1-2732_1-2735_1-2739_1-2740_2-2743_1-2751_3-2755_5-2768_1-2770_4-2772_1-2775_4-2776_2-2783_2-2784_1-2786_3-2796_2-2797_2-2803_2-2807_1-2808_2-2814_2-2801_2'
        
        for i in flush_dict:
            x = flush_dict[i]['appid']
            self.user_param['baijia/listall'] = self.user_param['baijia/listall'].format(x)
            res=requests.post(url,data=self.user_param,headers=self.headers,verify=False)
            rst=json.loads(res.text)#用户信息
            
            
            for i in range(len(rst['baijia/listall']['data']['results'])):
                k=rst['baijia/listall']['data']['results'][i]['content']
                info=dict(
                    author_name=k['author'],
                    author_img=k['author_icon'],
                    author_passport_id=k['author_passport_id'],
                    authorid=k['authorid'],
                    cover_img=k['cover_src'],
                    play_num=k['playcntText'],
                    publish_time=k['publish_time'],
                    title=k['title'],
                    video_url=k['video_short_url'],
                    video_url_hd=k['video_src']
                        )
                self.userinfo_ls.append(info)
            self.userinfo_dic[x]=self.userinfo_ls
        return rst
if __name__=='__main__':
    x=Haokan()
#    a = x.flush_parse()
#    b=x.flush()
#    c=x.comment_and_videoinfo()
#    m=x.comment()
#    n=x.videoinfo()





