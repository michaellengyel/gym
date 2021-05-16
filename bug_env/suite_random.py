from environment import Environment
import cv2
import random


def main():

    print("Random Testing Suite Started...")

    # Create Environment
    env = Environment(map_img_path="res/map_small.jpg",
                      fov=15,
                      food_spawn_threshold=100,
                      percent_for_game_over=10,
                      steps_for_game_over=100,
                      render=True)

    # Reset Environment
    env.reset()

    # Loop Environment
    while not env.game_over:

        # Render map and sub-map
        env.render_map()
        env.render_sub_map()

        cv2.waitKey(30)

        # Generate a random number 0-7
        action = random.randrange(0, 8)

        next_state, reward, game_over = env.step(action)

        print("reward: {}".format(reward),
              "total reward: {}".format(env.agent_reward),
              "game_over: {}".format(game_over),
              "total_reward: {}".format(env.total_generated_rewards)
              )


if __name__ == '__main__':
    main()
