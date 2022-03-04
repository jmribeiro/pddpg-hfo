from agents.random_agent import RandomAgent
from envs import offense_mid_action, goalie_mid_action, defense_mid_action
from learner import make_env
from utils.redis_manager import connect_redis


def create_environment(player='offense', server_port=6000, scale_actions=True):

    if player == 'offense':
        team = 'base_left'
        mid_action = offense_mid_action
    else:
        team = 'base_right'
        if player == 'goalie': mid_action = goalie_mid_action
        else: mid_action = defense_mid_action

    env = make_env(player, server_port, team, scale_actions)

    # configure redis
    redis_instance = connect_redis()

    # initialize teammate set
    redis_instance.sadd('teammates', env.unum)
    print('Number of teammates:', redis_instance.scard('teammates'))

    return env, mid_action


if __name__ == '__main__':

    env, mid_action = create_environment()
    agent = RandomAgent(env.observation_space, env.action_space)

    obs = env.reset()
    terminal = False
    while not terminal:
        act, (act_param, all_actions, all_action_parameters) = agent.act(obs)
        action = mid_action(act, act_param)
        next_obs, reward, terminal, info = env.step(action)
        print(next_obs)
        print(reward)
        print(terminal)
        print()
