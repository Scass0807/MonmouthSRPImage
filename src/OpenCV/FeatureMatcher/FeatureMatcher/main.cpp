//
//  main.cpp
//  FeatureMatcher
//
//  Created by Steven Cassidy on 7/23/18.
//  Copyright © 2018 Steven Cassidy. All rights reser

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/xfeatures2d/nonfree.hpp>
#include <fstream>
#include<string>
using namespace std;

string getImageName(string path)
{
    string name;
    int charIndex = static_cast<int>(path.size() -1);
    bool found = false;
    while (charIndex >= 0 && !found)
    {
        if(path[charIndex] == '\\' || path[charIndex] == '/')
        {
            name = path.substr(charIndex+1, path.size());
            found = true;
        }
        charIndex--;
    }
    return name;
}

int main(int argc, const char * argv[]) {
    // insert code here..
    cout << "Computing pairwise feature matches of image set using David Lowe's Scale-Invariant Feature Transform (SIFT) algorithm ... Please wait" << endl;
    string imgDIRS_Filename = argv[1];
    ifstream imgDIRS_File;
    imgDIRS_File.open(imgDIRS_Filename);
    vector<string> files;
    vector<cv::Mat> images;
    string line;
    while (getline(imgDIRS_File,line))
    {
        files.push_back(line);
        images.push_back(cv::imread(line));
    }
    imgDIRS_File.close();

    cv::Ptr<cv::xfeatures2d::SIFT> sift = cv::xfeatures2d::SIFT::create();

    for(int image1_index = 0; image1_index <images.size();image1_index++)
    {
        cv::Mat image1 = images[image1_index];
        string image1_name = getImageName(files[image1_index]);
        for (int image2_index = 0; image2_index < image1_index; image2_index++) {
            cv::Mat image2 = images[image2_index];
            string image2_name = getImageName(files[image2_index]);
            cout << "Comparing images " + image2_name + " and " + image1_name << " ... Please wait" << endl;
            vector<cv::KeyPoint> kp1,kp2;
            cv::Mat des1,des2;
            vector<vector<cv::DMatch>> matches;
            sift->detectAndCompute(image1, cv::Mat(), kp1,des1 );
            sift->detectAndCompute(image2, cv::Mat(), kp2, des2);
            cv::FlannBasedMatcher flann;
            flann.knnMatch(des1, des2, matches, 2);

            string filename_1 = image1_name + ".csv";
            ofstream outputFile_1;
            outputFile_1 << "x to " + image2_name << "," << "y to " + image2_name << endl;
            outputFile_1 << endl;

            string filename_2 = image2_name + ".csv";
            ofstream outputFile_2;
            outputFile_2 << "x to " + image1_name << "," << "y to " + image1_name << endl;
            outputFile_2 << endl;
            cv:: DMatch goodMatch;
            for(size_t mIndex = 0;mIndex<matches.size();++mIndex)
            {
                if (matches[mIndex][0].distance < 0.80f * matches[mIndex][1].distance)
                {
                    cv:: DMatch goodMatch = matches[mIndex][0];
                    int img1_idx = goodMatch.queryIdx;
                    int img2_idx = goodMatch.trainIdx;
                    cv::Point2f img1_pt = kp1[img1_idx].pt;
                    cv::Point2f img2_pt = kp2[img2_idx].pt;
                    outputFile_1 << img1_pt.x << "," << img1_pt.y << ",";
                    outputFile_1 << endl;
                    outputFile_2 << img2_pt.x << "," << img2_pt.y << ",";
                    outputFile_2 << endl;
                }

            } //end of for loop
            outputFile_1 << endl;
            outputFile_1.close();
            outputFile_2 << endl;
            outputFile_2.close();

            kp1.clear();
            kp2.clear();
            matches.clear();

        }
    }
    files.clear();
    images.clear();
    delete sift;
    return 0;
}
