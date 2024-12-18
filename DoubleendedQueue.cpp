#include<iostream>
#define SIZE 10
using namespace std;
class dequeue{
    int a[10],front,rear,count;
    public:
    dequeue();
    void add_at_beg(int);
    void add_at_end(int);
    void del_fr_front();
    void del_fr_end();
    void display();
};
dequeue::dequeue()
{
    front=-1;
    rear=-1;
    count=0;
}

void dequeue::add_at_beg(int item){
    int i;
    if (front==-1){
        front++;
        rear++;
        a[rear]=item;
        count++;
    }
    else if(rear>=SIZE-1){
        cout<<"\nInsertion is not possible Overflow!!";
    }
    else{
        for(i=count;i>=0;i--){
            a[i]=a[i-1];
        }
        a[i]=item;
        count++;
        rear++;
    }
}

void dequeue::add_at_end(int item){
    if(front==-1){
        front++;
        rear++;
        count++;
        a[rear]=item;
    }
    else if(rear>=SIZE-1){
        cout<<"\nInsertion is not possible Overflow!!";
        return ;
    }
    else{
        a[++rear]=item;
    }
}

void dequeue::display(){
    for (int i=front;i<=rear;i++){
        cout<<a[i]<<" ";
    }
}

void dequeue::del_fr_front(){
    if(front==-1){
        cout<<"Deletion is not posible: DEqueue is empty";
        return ;
    }
    else{
        if(front==rear){
            front=rear=-1;
            return;
        }
        cout<<"The deleted element is "<<a[front];
        front=front=1;
    }
}

void dequeue::del_fr_end(){
    if (front==-1){ 
        cout<<"Deletion is not posible: DEqueue is empty";
        return ;
         }
         else{
            if(front==rear){
                front=rear=-1;
            }
            cout<<"The deleted element is "<< a[rear];
            rear=rear-1;
         }
}

int main(){
    int c,item;
    dequeue d1;

    do{
        cout<<"\t\n1.Insert front"
                "\t\n2.Insert rear"
                "\t\n3.Delete front"
                "\t\n4.Delete rear"
                "\t\n5.Print"
                "\t\n6.Exit";
         cout<<"\nEnter your choice : ";
         cin>>c;
    switch(c)
        {
            case 1:
              cout<<"\nEnter item to insert front : ";
              cin>>item;
              d1.add_at_beg(item);
              break;

           case 2:
               cout<<"\nEnter the item to insert rear : ";
               cin>>item;
               d1.add_at_end(item);
               break;

           case 3:
               d1.display();
               break;

           case 4:
              d1.del_fr_front();
               break;

           case 5:
               d1.del_fr_end();
            break;

           case 6:
             exit(1);
             break;
           default:
           cout<<"Tnvalid choice";
           break;
        }
    }while (c!=7);
    return 0;
}



