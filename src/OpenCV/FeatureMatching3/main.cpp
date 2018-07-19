//
//  main.cpp
//  FeatureMatching2
//
//  Created by Steven Cassidy on 7/10/18.
//  Copyright © 2018 Steven Cassidy. All rights reserved.
//

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/xfeatures2d/nonfree.hpp>
#include <matplotlibcpp.h>
using namespace std;
namespace plt = matplotlibcpp;

int main(int argc, const char * argv[]) {
    // insert code here...
    cv::Mat img1 = cv::imread("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/24.JPG");
    cv::Mat img2 = cv::imread("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/14.JPG");
    
    cv::Ptr<cv::xfeatures2d::SURF> surf = cv::xfeatures2d::SURF::create();
    cvNamedWindow("Image");
    vector<cv::KeyPoint> kp1,kp2;
    cv::Mat des1,des2;
    vector<vector<cv::DMatch>> matches;
    surf->detectAndCompute(img1, cv::Mat(), kp1,des1 );
    surf->detectAndCompute(img2, cv::Mat(), kp2, des2);
    cv::BFMatcher bf(cv::NORM_L2);
    bf.knnMatch(des1, des2, matches, 2,cv::Mat(),false);
    vector<cv::DMatch> good;
    for(size_t mIndex = 0;mIndex<matches.size();++mIndex)
    {
        if (matches[mIndex][0].distance < 0.80f * matches[mIndex][1].distance)
        {
            good.push_back(matches[mIndex][0]);
        }
    }
    vector<cv::Point2f> list_kp1,list_kp2;
    for (size_t index = 0; index < good.size(); index++)
    {
        int img1_idx = good[index].queryIdx;
        int img2_idx = good[index].trainIdx;
        
        list_kp1.push_back(kp1[img1_idx].pt);
        list_kp2.push_back(kp2[img2_idx].pt);
    }
    cout << list_kp1 << endl << list_kp2;
    cv::Mat immatched;
    cv::drawMatches(img1, kp1, img2, kp2, good, immatched);
    cv::resize(immatched, immatched, cv::Size(immatched.cols/6,immatched.rows/6));
    cvNamedWindow("image");
    cv::imshow("image", immatched);
    cvWaitKey(0);
    cvDestroyAllWindows();
    immatched.release();
    return 0;
}
