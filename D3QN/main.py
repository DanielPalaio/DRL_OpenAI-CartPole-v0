

from agent import Agent
import gym


env = gym.make("CartPole-v0")
spec = gym.spec("CartPole-v0")
train = 0
test = 1
num_episodes = 100
graph = True

file_type = 'tf'
file = 'saved_networks/d3qn_model20'

d3qn_agent = Agent(lr=0.00075, discount_factor=0.99, num_actions=2, epsilon=1.0, batch_size=64, input_dim=[4])

if train and not test:
    d3qn_agent.train_model(env, num_episodes, graph)
else:
    d3qn_agent.test(env, num_episodes, file_type, file, graph)
