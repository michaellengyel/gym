from environment import Environment
import random


def main():

    print("Random Testing Suite Started...")

    # Create Environment
    env = Environment(map_img_path="res/map_small_edge.jpg",
                      fov=15,
                      food_spawn_threshold=100,
                      percent_for_game_over=10,
                      steps_for_game_over=1000,
                      wait_key=200,
                      render=True)

    # Reset Environment
    env.reset()

    # Loop Environment
    while not env.game_over:

        # Render map and sub-map
        env.render_map()
        env.render_sub_map()

        # Generate a random number 0-23
        action = random.randrange(0, 24)

        next_state, reward, game_over = env.step(action)

        print("reward: {}".format(reward),
              "total reward: {}".format(env.agent_reward),
              "game_over: {}".format(game_over),
              "total_reward: {}".format(env.total_generated_rewards)
              )


if __name__ == '__main__':
    main()
