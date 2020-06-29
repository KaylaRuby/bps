# example_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def half_siblings_same_father(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.half_siblings_same_father: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.half_siblings_same_father: got unexpected plan from when clause 2"
                if context.lookup_data('mother1') != context.lookup_data('mother2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('example')
  
  bc_rule.bc_rule('half_siblings_same_father', This_rule_base, 'half_sibling',
                  half_siblings_same_father, None,
                  (contexts.variable('af'),
                   contexts.variable('bf'),),
                  (),
                  (contexts.variable('af'),
                   contexts.variable('father'),
                   contexts.variable('mother1'),
                   contexts.variable('bf'),
                   contexts.variable('mother2'),))


Krb_filename = '../example.krb'
Krb_lineno_map = (
    ((14, 18), (29, 29)),
    ((20, 27), (31, 31)),
    ((28, 35), (32, 32)),
    ((36, 36), (33, 33)),
)
