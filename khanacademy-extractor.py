#!/usr/bin/python

import urllib2
import re
import os

KHAN_URL = 'https://www.khanacademy.org';

stream_library = urllib2.urlopen(KHAN_URL + '/library');
all_library = stream_library.read();
stream_library.close();

r_major = re.findall(r'class="subject-link" href="/([\w\d-]+)/', all_library);

for h in r_major:
    if not os.path.exists(h):
        os.makedirs(h);
        print "Create folder " + h;
    os.chdir(h);
    print "Enter folder " + h;

    r_library = re.findall(r'class="subject-link" href="/' + h + '/([\w\d-]+)"', all_library);



    for i in r_library:
        if not os.path.exists(i):
            os.makedirs(i);
            print "Create folder " + i;
        os.chdir(i);
        print "Enter folder " + i;

        #https://www.khanacademy.org/math/cc-third-grade-math
        topic_link = '/' + h + '/' + i;
        
        stream_topic = urllib2.urlopen(KHAN_URL + topic_link);
        all_topic = stream_topic.read();
        stream_topic.close();
        r_topic = re.findall(r'href="' + topic_link + '/([\w\d-]+)" class="topic-list-item"', all_topic);
        #unique value
        r_topic = list(set(r_topic));
        
        print "#Found " + str(len(r_topic)) + " topic/s";


        
        for j in r_topic:
            if not os.path.exists(j):
                os.makedirs(j);
                print "Create folder " + j;
            os.chdir(j);
            print "Enter folder " + j;
            
            #https://www.khanacademy.org/math/cc-third-grade-math/cc-3rd-add-sub-topic
            sub_topic_link = topic_link + '/' + j;
            
            stream_sub_topic = urllib2.urlopen(KHAN_URL + sub_topic_link);
            all_sub_topic = stream_sub_topic.read();
            stream_sub_topic.close();
            r_sub_topic = re.findall(r'href="' + sub_topic_link + '([/\w\d-]+)" class="progress-item-link"', all_sub_topic);
            #unique value
            r_sub_topic = list(set(r_sub_topic));

            print "#Found " + str(len(r_sub_topic)) + " sub topic/s";


            
            for k in r_sub_topic:
                #https://www.khanacademy.org/math/cc-third-grade-math/cc-3rd-add-sub-topic/cc-3rd-adding-carrying/v/carrying-when-adding-three-digit-numbers
                stream_youtube = urllib2.urlopen(KHAN_URL + sub_topic_link + '/' + k);
                all_youtubeid = stream_youtube.read();
                stream_youtube.close();
                youtubeid = re.findall(r'data-youtubeid="([\w\d-]+)"', all_youtubeid);

                ### youtubeid = Wm0zq-NqEFs
                if(len(youtubeid) == 1):
                    os.system('python ../../../youtube-dl ' + youtubeid[0]);
                    #open(youtubeid[0] + '.txt', 'w').close();
                    #print "Create file " + youtubeid[0];
                else:
                    print "Didn't download file for " + k;

            os.chdir('..');
            print "Exit folder " + j;

            
        os.chdir('..');
        print "Exit folder " + i;

        
    os.chdir('..');
    print "Exit folder " + h;
