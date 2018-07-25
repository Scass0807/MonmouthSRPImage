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
#include <fstream>
using namespace std;
namespace plt = matplotlibcpp;

int main(int argc, const char * argv[]) {
    // insert code here...
    string img1_name =  "24.JPG";
    string img2_name = "14.JPG";
    cv::Mat img1 = cv::imread("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/"+ img1_name);
    cv::Mat img2 = cv::imread("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/" +img2_name );
    
    cv::Ptr<cv::xfeatures2d::SIFT> sift = cv::xfeatures2d::SIFT::create();
    cvNamedWindow("Image");
    vector<cv::KeyPoint> kp1,kp2; 
    cv::Mat des1,des2;
    vector<vector<cv::DMatch>> matches;
    sift->detectAndCompute(img1, cv::Mat(), kp1,des1 );
    sift->detectAndCompute(img2, cv::Mat(), kp2, des2);
    cv::FlannBasedMatcher flann;
    flann.knnMatch(des1, des2, matches, 2);
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
    
    cout << list_kp1 << endl << list_kp2 << endl;
    
    string filename = img1_name + "_" + img2_name + "_matches.csv";
    ofstream outputFile;
    outputFile.open(filename);
    cout << "Creating file" << endl;
    outputFile << "x (" +img1_name+")" <<"," <<"y (" +img1_name+")" <<"," << "x (" +img2_name+")" <<"," <<"y (" +img2_name+")" << endl;
    for (size_t index = 0; index < list_kp1.size(); index++) {
        outputFile << list_kp1[index].x << "," << list_kp1[index].y << ",";
        outputFile << list_kp2[index].x << "," << list_kp2[index].y << ",";
        outputFile << endl;
        cout << list_kp1[index] << ";" <<list_kp2[index] << endl;
    }
    outputFile.close();
    
    cout << "Done writing file" << endl;
    cv::Mat immatched;
    cv::drawMatches(img1, kp1, img2, kp2, good, immatched);
    cv::resize(immatched, immatched, cv::Size(immatched.cols/6,immatched.rows/6));
    cv::Mat homography = cv::findHomography(list_kp1, list_kp2);
    cv::Mat warped;
    cv::warpPerspective(img2, warped, homography, img1.size());
    cv::resize(warped, warped, cv::Size(warped.cols/6,warped.rows/6));
    cv::drawKeypoints(img1, kp1, img1);
    cv::drawKeypoints(img2, kp2, img2);
    cv::resize(img1, img1, cv::Size(img1.cols/6,img1.rows/6));
    cv::resize(img2, img2, cv::Size(img2.cols/6,img2.rows/6));
    cvNamedWindow("img1");
    cv::imshow("img1", img1);
    cvNamedWindow("img2");
    cv::imshow("img2", img2);
    cvNamedWindow("matches");
    cv::imshow("matches", immatched);
    cvNamedWindow("warped");
    cv::imshow("warped", warped);
    cvWaitKey(0);
    cvDestroyAllWindows();
    
    return 0;
}
