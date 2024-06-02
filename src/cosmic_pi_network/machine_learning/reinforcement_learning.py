import gym
from stable_baselines3 import PPO

class ReinforcementLearning:
    def __init__(self):
        pass

    def create_environment(self, env_name):
        env = gym.make(env_name)
        return env

    def create_agent(self, env):
        model = PPO("MlpPolicy", env, verbose=1)
        return model

    def train_agent(self, model, env):
        model.learn(total_timesteps=10000)
        return model

    def evaluate_agent(self, model, env):
        obs = env.reset()
        done = False
        rewards = 0
        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, _ = env.step(action)
            rewards += reward
        return rewards

# Example usage
reinforcement_learning = ReinforcementLearning()
env = reinforcement_learning.create_environment("CartPole-v1")
model = reinforcement_learning.create_agent(env)
model = reinforcement_learning.train_agent(model, env)
rewards = reinforcement_learning.evaluate_agent(model, env)
print("Rewards:", rewards)
