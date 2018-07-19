//
//  main.cpp
//  FeatureMatching
//
//  Created by Steven Cassidy on 7/5/18.
//  Copyright © 2018 Steven Cassidy. All rights reserved.
//

#include <iostream>
#include <opencv2/opencv.hpp>
#include <matplotlibcpp.h>
using namespace std;
namespace plt = matplotlibcpp;

int main(int argc, const char * argv[]) {
    // insert code here...
    cv::Mat img1 = cv::imread("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/24.JPG");
    cv::Mat img2 = cv::imread("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/14.JPG");
    
    cv::Ptr<cv::ORB> orb = cv::ORB::create();
    cvNamedWindow("Image");
    vector<cv::KeyPoint> kp1,kp2;
    cv::Mat des1,des2;
    vector<cv::DMatch> matches;
    orb->detectAndCompute(img1, cv::Mat(), kp1,des1 );
    orb->detectAndCompute(img2, cv::Mat(), kp2, des2);
    cv::BFMatcher bf(cv::NORM_HAMMING, true);
    bf.match(des1, des2, matches,cv::Mat());
    sort(matches.begin(), matches.end());
    matches.erase(matches.begin()+50, matches.end());
    vector<cv::Point2f> list_kp1,list_kp2;
    for (size_t index = 0; index < matches.size(); index++)
    {
        int img1_idx = matches[index].queryIdx;
        int img2_idx = matches[index].trainIdx;
        
        list_kp1.push_back(kp1[img1_idx].pt);
        list_kp2.push_back(kp2[img2_idx].pt);
    }
    cout << list_kp1 << endl << list_kp2;
    cv::Mat immatched;
    cv::drawMatches(img1, kp1, img2, kp2, matches, immatched);
    cv::resize(immatched, immatched, cv::Size(immatched.cols/6,immatched.rows/6));
    cvNamedWindow("image");
    cv::imshow("image", immatched);
    cvWaitKey(0);
    cvDestroyAllWindows();
    immatched.release();
    return 0;
}
