```bash 
git pull origin main 

docker build -t my-fastapi-app .  

docker run -d --name my-container -p 8000:6000 my-fastapi-app