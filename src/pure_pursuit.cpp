#include <ros/ros.h>
#include <iostream>
#include <nav_msgs/Path.h>
#include "tf_listerner.h"

#define max_lin_vel 1
#define max_ang_vel 1

using namespace std;

ros::Subscriber sub_path_g;// = nh.subscribe("topic_name", 1000, subCallback);
ros::Publisher pub_vel_g;// = nh.advertise<std_msgs::String>("topic_name", 1000);

nav_msgs::Path path_g;
int get_path_flag_g = 0;
boost::shared_ptr<Tf_Listerner> car_in_map_g;

void subPathCb(nav_msgs::Path msg)
{
    path_g = msg;
    get_path_flag_g = 1;
}

void controler()
{
    double det_x1 = car_in_map_g->x() - path_g.poses[path_g.poses.size() - 1].pose.position.x;
    double det_y1 = car_in_map_g->y() - path_g.poses[path_g.poses.size() - 1].pose.position.y;
    if(det_x1 * det_x1 + det_y1 * det_y1 < 0.25)
    {
        get_path_flag_g = 0;
        return;
    }

    double min_dis = 100000;
    int n = 0;
    for(int i = 0;i < path_g.poses.size();i++)
    {
        double det_x2 = car_in_map_g->x() - path_g.poses[i].pose.position.x;
        double det_y2 = car_in_map_g->y() - path_g.poses[i].pose.position.y;
        if(min_dis > det_x2 * det_x2 + det_y2 * det_y2)
        {
            min_dis = det_x2 * det_x2 + det_y2 * det_y2;
            n = i;
        }
    }

    double det_x = path_g.poses[n + 2].pose.position.x - car_in_map_g->x();
    double det_y = path_g.poses[n + 2].pose.position.y - car_in_map_g->y();
    double car_ang = acos(2 * car_in_map_g->ow() * car_in_map_g->ow() - 1);
    car_ang = car_in_map_g->oz() * car_in_map_g->ow() < 0 ? (0 - car_ang) : car_ang;
    double x_0 = det_x * cos(car_ang) + det_y * sin(car_ang);
    double y_0 = det_y * cos(car_ang) - det_x * sin(car_ang);
    double turn_radius = 0.5 * x_0 * x_0 / y_0 + 0.5 * y_0;

    // cout << car_ang << ", "
    //      << car_in_map_g->oz() << ", " << car_in_map_g->ow() << ", " 
    //      << acos(car_in_map_g->ow()) << endl;

    geometry_msgs::Twist cmd_vel;
    double v , w;
    v = max_lin_vel;
    w = v / turn_radius;
    if(fabs(w) > max_ang_vel)
    {
        w = w / fabs(w) * max_ang_vel;
        v = w * turn_radius;
    }
    cmd_vel.linear.x = v;
    cmd_vel.angular.z = w;
    pub_vel_g.publish(cmd_vel);

    ros::Duration(0.01).sleep();
}

int main(int argc , char** argv)
{
    ros::init(argc , argv , "pure_pursuit");
    ros::NodeHandle n;
    sub_path_g = n.subscribe("/own_path" , 2 , subPathCb);
    pub_vel_g = n.advertise<geometry_msgs::Twist>("cmd_vel" , 2);
    car_in_map_g = boost::make_shared<Tf_Listerner>("map" , "base_footprint");
    while(ros::ok())
    {
        ros::spinOnce();
        if(get_path_flag_g == 1)
        {
            controler();
        }
        else
        {
            geometry_msgs::Twist cmd_vel;
            cmd_vel.linear.x = 0;
            cmd_vel.angular.z = 0;
            pub_vel_g.publish(cmd_vel);
            ros::Duration(1).sleep();
        }
    }
    return 0;
}
