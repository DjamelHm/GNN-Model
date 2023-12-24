import ignnition
import os

def main():
	model = ignnition.create_model(model_dir='./')
	model.computational_graph()
	model.train_and_validate()
	predictions = model.predict()
	
	predictions_str = [i.numpy() for i in predictions]
	file = open('predictions.txt','w')
	for j in predictions_str:
		for k in j:
			elt = [round(l,0) for l in k]
			file.write(str(elt)+"\n") 
	file.close()
	os.system("python expected.py")
	os.system("python compare.py")

if __name__ == "__main__":
	main()
