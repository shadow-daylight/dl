from core.advbase import *

def module():
    return Student_Maribelle

class Student_Maribelle(Adv):
    conf = {}
    conf['acl'] = """
        `dragon,s
        `s3, not buff(s3) and x=5
        `s4
        `s1
        `s2,cancel
        """
    conf['coabs'] = ['Blade', 'Marth', 'Gala_Sarisse']
    conf['share'] = ['Kleimann']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
