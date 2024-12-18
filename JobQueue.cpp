#include<iostream>
#include<queue>
#include<string>
using namespace std;
class jobqueue{

private:
queue<string>jobs;

public:
   void addjob(const string &job){
	jobs.push(job);
   cout<<"Job added "<<job<<endl;
}
  bool deletejob(){
	if(jobs.empty()){
		cout<<"No jobs in the queue to delete"<<endl;
		return false;
	}
	else{
		cout<<"Job deleted :"<<jobs.front()<<endl;
		jobs.pop();
		return true;
	}
  }
  void nextjob()const{
	if(jobs.empty()){
		cout<<"No jobs in the queue :"<<endl;
	}else{
		cout<<"Next job :"<<jobs.front()<<endl;
	}
 }
bool isempty()const{
	return jobs.empty();
}
};

int main(){
	jobqueue JobQueue;
	int choice;
	string job;
	while (true){
		cout<<"Jobs queue Menu :"<<endl;
		cout<<"1.Add job :"<<endl;
		cout<<"2.Delete job :"<<endl;
		cout<<"3.Show next job :"<<endl;
		cout<<"4.Exit"<<endl;
		cout<<"Enter the choice :"<<endl;
		cin>>choice;
		

		switch(choice){
			case 1:
			cout<<"Enter Job description :";
			cin.ignore();
			getline(cin,job);
			JobQueue.addjob(job);
			break;
			case 2:
			JobQueue.deletejob();
			break;
			case 3:
			JobQueue.nextjob();
			break;
			case 4:
			cout<<"Exiting the program :"<<endl;
			return 0;
			default:
			cout<<"Invalid choice.Please try again "<<endl;

		}
	}
	return 0;
}
