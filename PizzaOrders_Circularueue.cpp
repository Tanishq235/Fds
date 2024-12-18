#include <iostream>
#include <string>
using namespace std;
#define MAX 5
class circularqueue{
    int front,rear;
    string orders[MAX];
public:
 circularqueue(){
    front = rear = -1;
 }
 bool isfull(){
    return(front==(rear+1)%MAX);
 }
bool isempty(){
    return(front==-1);
}
void placeorder(string order){
    if (isfull()) {
        cout<<"Order is full cannot accept more orders"<<endl;
    }
    else{
        if (front==-1){ front=0;}
        rear=(rear+1)%MAX;
        orders[rear]=order;
        cout<<"order placed :"<<order<<endl;
    }
}
void serveorder(){
    if (isempty()){
        cout<<"No orders to serve"<<endl;
    }else
    {
        cout<<"order served"<<orders[front]<<endl;
        if (front==rear){
            front=rear=-1;
        }else
        {
            front=(front+1)%MAX;

        }   
    }
}
void displayorder(){
    if (isempty()){
        cout<<"No orders in the queue"<<endl;
    }else{
        cout<<"current orders in the queue :\n";
        int i=front;
        while(i!=rear){
            cout<<orders[i]<<" ";
            i=(i+1)%MAX;
        }
        cout<<orders[rear]<<endl;
    }
}
};
int main(){
    circularqueue pizzaparlor;
    int choice;
    string order;

    while(true){
        cout<<"\n pizza parlor order system menu"<<endl;
        cout<<"1. place an order"<<endl;
        cout<<"2. serve an order"<<endl;
        cout<<"3. Display all orders"<<endl;
        cout<<"4. Exit\n"<<endl;
        cout<<"Enter the choice"<<endl;
        cin>>choice;


        switch (choice)
        {
        case 1:
            cout<<"Enter order name :";
            cin>>order;
            pizzaparlor.placeorder(order);
            break;
        case 2:
            pizzaparlor.serveorder();
            break;
        case 3:
            pizzaparlor.displayorder();
            break;
        case 4:
            cout<<"Exiting......"<<endl;
            break;
        default:
        cout<<"Invalid choice!please try again";
            break;
        }
    }
    return 0;
    
}
