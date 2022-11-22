class Parent {
   public:
    Enfant* _enfant;
    int truc;

    Parent() {
        _enfant = new Enfant(truc);
    }
};