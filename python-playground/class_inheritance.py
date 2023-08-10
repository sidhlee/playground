class MixinA:
    def dispatch(self):
        print("dispatch from Mixin A")
        return super(MixinA, self).dispatch()


class MixinC:
    pass


class MixinB:
    def dispatch(self):
        print("dispatch from Mixin B")
        # python keeps searching until it finds dispatch method
        return super(MixinB, self).dispatch()


class Base:
    def dispatch(self):
        print("dispatch from base")


# Search order --------------------->
class Foo(MixinA, MixinB, MixinC, Base):
    pass


Foo().dispatch()
