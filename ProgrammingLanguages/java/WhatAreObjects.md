# What Are Objects In Java?

As we know JAVA is an Object Oriented programming language, therefore objects form the main crux around which the entire language is based.
Here I won't go into the technical definition but would rather explain in such a way that it would remain with you for your entire lifetime.
Now, as I said earlier java is an object oriented language, so for now keep in mind there are two entities : 
- class
- object

Now its time I tell you a small story-
Once there was a toy maker, who used to make toys using small moulds. Moulds are use to make repetitive patterns of the same type. For example consier a doll mould, so what the toy maker would do is to make number of same dolls using that one single mould. Okay the story finishes here, its a happy ending.

Now focus on what I say-
In the above story, the mould is a class, and the same toys that come out of that particular mould are its objects.
Therefore simplified:
mould - class
toys form that one mould - objects

Now its the time I introduce you to the main definition:
Object is a prototype of the class whereas a class provides a blueprint from which n-number of objects can be made.

Consider the following code:

```
class A{
    void hi(){
        System.out.println("Hi dear!");
    }
}


class B{
    public static void main(String[] args){

        A obj1 = new A();
        obj1.hi();

        A obj2 = new A();
        obj2.hi();

        A obj3 = new A();
        obj3.hi();
    }
}

```


Consider the above code, here class A contains a function that simply prints hi. Now what is happing is I am creating three objects of the same A class which access the same function hi but through different objects like obj1, obj2 and obj3. One thing to be noted here is that class A is the mould here and obj1,2 and 3 are its toys that is objects.

Feel free to provide feedback, I surely look up for improvements!