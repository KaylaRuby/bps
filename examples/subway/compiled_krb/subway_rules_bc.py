# subway_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def at_station(rule, arg_patterns, arg_context):
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
        with engine.prove('subway_rules', 'take_line', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "subway_rules.at_station: got unexpected plan from when clause 1"
            with engine.prove('subway', 'at_station', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "subway_rules.at_station: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def travel_on_same_line(rule, arg_patterns, arg_context):
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
        with engine.prove('subway', 'station', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "subway_rules.travel_on_same_line: got unexpected plan from when clause 1"
            with engine.prove('subway', 'station', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "subway_rules.travel_on_same_line: got unexpected plan from when clause 2"
                if context.lookup_data('from') != context.lookup_data('to'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def connected_stations(rule, arg_patterns, arg_context):
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
        with engine.prove('subway', 'station', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "subway_rules.connected_stations: got unexpected plan from when clause 1"
            with engine.prove('subway', 'station', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "subway_rules.connected_stations: got unexpected plan from when clause 2"
                if context.lookup_data('from') != context.lookup_data('to'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('subway_rules')
  
  bc_rule.bc_rule('at_station', This_rule_base, 'at_station',
                  at_station, None,
                  (contexts.variable('station'),),
                  (),
                  (contexts.variable('from'),
                   contexts.anonymous('_line'),
                   contexts.variable('station'),))
  
  bc_rule.bc_rule('travel_on_same_line', This_rule_base, 'take_line',
                  travel_on_same_line, None,
                  (contexts.variable('from'),
                   contexts.variable('line'),
                   contexts.variable('to'),),
                  (),
                  (contexts.variable('from'),
                   pattern.pattern_tuple((contexts.variable('line'),), None),
                   contexts.anonymous('_'),
                   contexts.variable('to'),))
  
  bc_rule.bc_rule('connected_stations', This_rule_base, 'connected',
                  connected_stations, None,
                  (contexts.variable('from'),
                   contexts.variable('to'),),
                  (),
                  (contexts.variable('from'),
                   contexts.variable('line'),
                   contexts.anonymous('_'),
                   contexts.variable('to'),))


Krb_filename = '../subway_rules.krb'
Krb_lineno_map = (
    ((14, 18), (7, 7)),
    ((20, 27), (9, 9)),
    ((28, 33), (10, 10)),
    ((46, 50), (13, 13)),
    ((52, 60), (15, 15)),
    ((61, 69), (16, 16)),
    ((70, 70), (17, 17)),
    ((83, 87), (20, 20)),
    ((89, 97), (22, 22)),
    ((98, 106), (23, 23)),
    ((107, 107), (24, 24)),
)
