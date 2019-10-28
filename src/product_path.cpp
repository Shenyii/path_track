#include <ros/ros.h>
#include <nav_msgs/Path.h>
#include <iostream>
#include "tf_listerner.h"

using namespace std;

Tf_Listerner* car_in_map_;
ros::Publisher pub_path_;

void pubPath()
{
    double car_x = car_in_map_->x();
    double car_y = car_in_map_->y();
    double car_oz = car_in_map_->oz();
    double car_ow = car_in_map_->ow();
    double centrol_x = car_x + 0.8;
    double centrol_y = car_y;
    nav_msgs::Path path;
    path.header.frame_id = "map";
    path.poses.resize(39);
    for(int i = 0;i < 19;i++)
    {
        path.poses[i].header.frame_id = "map";
        path.poses[i].pose.position.x = centrol_x - 0.8 * cos(i * 0.16);
        path.poses[i].pose.position.y = centrol_y + 0.8 * sin(i * 0.16);
    }
    centrol_x = car_x + 2.4;
    centrol_y = car_y;
    for(int i = 19;i < 39;i++)
    {
        path.poses[i].pose.position.x = centrol_x - 0.8 * cos((i - 19) * 0.16);
        path.poses[i].pose.position.y = centrol_y - 0.8 * sin((i - 19) * 0.16);
    }
    pub_path_.publish(path);
    cout << "product a path." << endl;
}

int main(int argc,char** argv)
{
    ros::init(argc, argv, "product_path");
    ros::NodeHandle nh;
    pub_path_ = nh.advertise<nav_msgs::Path>("/own_path", 3);
    car_in_map_ = new Tf_Listerner("map","base_footprint");
    ros::Duration(5).sleep();
    while(ros::ok())
    {
        pubPath();
        getchar();
    }
    return 0;
}