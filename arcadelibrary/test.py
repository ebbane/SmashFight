
import arcade
import os

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Primitives Example")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()






# Draw a filled in rectangle
arcade.draw_rectangle_filled(300, 10, 600, 50, arcade.color.BLUSH)



# Finish the render.
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()