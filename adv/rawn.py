from core.advbase import *

def module():
    return Rawn

class Rawn(Adv):
    conf = {}
    conf['slots.a'] = ['Resounding_Rendition', 'The_Red_Impulse']
    conf['acl'] = """
        `dragon, fsc or s
        `s3
        `s2
        `s1
        `s4, cancel
        `fs, x=5
        """
    conf['coabs'] = ['Cleo','Raemond','Peony']
    conf['share'] = ['Gala_Mym']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)