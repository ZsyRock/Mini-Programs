# Define a dictionary slang_dict to store concepts and their descriptions in deep learning.
slang_dict = {
    "Linear Neural Networks": "Before introducing deep neural networks, we need to understand the fundamental knowledge of neural network training. In this chapter, we will cover the entire training process of neural networks, including defining simple neural network architectures, data processing, specifying loss functions, and training models. To facilitate learning, we will start with classical algorithms—linear neural networks—to introduce the fundamentals of neural networks. Linear regression and softmax regression in classical statistical learning techniques can be considered as linear neural networks. These concepts will lay the foundation for more complex techniques in the later chapters of this book.",

    "Multilayer Perceptron": "In this chapter, we introduce our first true deep network. The simplest deep network is called a multilayer perceptron (MLP). An MLP consists of multiple layers of neurons, each receiving input from the previous layer and passing output to the next layer, influencing its neurons. When training large-capacity models, we face the risk of overfitting. Therefore, this chapter starts with fundamental concepts such as overfitting, underfitting, and model selection. To address these issues, we introduce regularization techniques such as weight decay and dropout. We also discuss numerical stability and parameter initialization, which are critical for successfully training deep networks. At the end of the chapter, we apply the discussed concepts to a real-world case: house price prediction. Topics related to computational performance, scalability, and efficiency will be discussed in later chapters.",

    "Deep Learning Computation": "Besides large datasets and powerful hardware, excellent software tools have played an indispensable role in the rapid development of deep learning. Since the release of the pioneering Theano library in 2007, flexible open-source tools have enabled researchers to quickly prototype models, avoiding redundant work while still allowing modifications at the lower levels. Over time, deep learning libraries have evolved to provide increasingly higher-level abstractions. Just as semiconductor designers progressed from designing transistors to logic circuits and then to writing code, neural network researchers have shifted from considering individual artificial neuron behaviors to designing networks from a layer perspective, often using larger blocks when constructing architectures."
}

# Add a new section
slang_dict[
    "Convolutional Neural Networks"] = "In previous chapters, we encountered image data. Each sample of this type of data consists of a two-dimensional grid of pixels, where each pixel may contain one or more values depending on whether the image is grayscale or colored. Until now, our approach to processing such structured data has been inefficient. We simply flattened image data into one-dimensional vectors, ignoring the spatial structure of each image, and then fed it into a fully connected multilayer perceptron. Since these networks are invariant to feature element order, the optimal solution is to leverage prior knowledge—utilizing the relationships between adjacent pixels to learn an effective model from image data."

# Query functionality
query = input("Please enter the topic you want to search for: ")
if query in slang_dict:
    print("The summary of '" + query + "' is as follows:")
    print(slang_dict[query])
else:
    print("The topic you searched for is not available.")
    print("The current dictionary contains " + str(len(slang_dict)) + " entries.")
