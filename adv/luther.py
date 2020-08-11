from core.advbase import *
from slot.a import *
from slot.d import *
from module.x_alt import *

def module():
    return Luther

class Luther(Adv):
    a1 = ('cc', 0.15, 'hit15')

    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+His_Clever_Brother()
    conf ['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s4
        `s3, cancel
        `s2, cancel
        `fs, x=5
    """
    coab = ['Blade', 'Xander', 'Summer_Estelle']
    share = ['Gala_Elisanne', 'Ranzal']

    def fs_proc_alt(self, e):
        self.afflics.frostbite(e.name,120,0.41)

    def prerun(self):
        conf_fs_alt = {}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)
        Timer(self.fs_alt_on_crit, 10, True).on()

    def fs_alt_on_crit(self, t):
        # look i dont wanna mass sim
        self.fs_alt.on()

    def s2_proc(self, e):
        Debuff(e.name, 0.05, 10, 0.9, 'attack').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
