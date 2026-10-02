import unittest
from contextlib import redirect_stdout
import io


from video import Video

class VideoTestCase(unittest.TestCase):
    def setUp(self):
        self.video = Video("Love Me Like You Do", 10, 0)

    def test_the_initial_state_of_the_video(self):
        self.assertEqual(self.video.title, "Love Me Like You Do")
        self.assertEqual(self.video.duration, 10)
        self.assertEqual(self.video.position, 0)

    def test_that_the_initial_state_of_the_video_cannot_be_created_with_an_invalid_duration(self):
        with self.assertRaises(ValueError):
            self.video = Video("Love Me Like You Do", 0, 0)

    def test_that_the_initial_state_of_the_video_cannot_be_created_with_an_invalid_position(self):
        with self.assertRaises(ValueError):
            self.video = Video("Love Me Like You Do", 10, -1)

    def test_that_the_initial_state_of_the_video_cannot_be_created_with_an_invalid_position_beyond_the_duration(self):
        with self.assertRaises(ValueError):
            self.video = Video("Love Me Like You Do", 10, 11)

    def capture_play(self, video):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            video.play()
        return buffer.getvalue()


    def test_that_play_prints_title_of_the_video(self):
        self.assertIn("Love Me Like You Do", self.capture_play(self.video))

    def test_that_play_prints_duration_of_the_video(self):
        self.assertEqual(self.video.duration, 10)

    def test_that_play_says_now_playing_of_the_video_correctly(self):
        self.assertIn("now playing", self.capture_play(self.video).lower())

    def test_that_play_prints_the_right_title_for_each_video(self):
        new_video = Video("Kill Squad", 30, 0)
        self.assertIn("Kill Squad", self.capture_play(new_video))
        output = self.capture_play(new_video)
        self.assertIn("Kill Squad", output)
        self.assertNotIn("Oliver Twist", output)

    def test_that_play_does_not_change_position_of_the_video(self):
        self.capture_play(self.video)
        self.assertEqual(self.video.position, 0)


    def test_that_the_video_when_advance_moves_forward(self):
        self.video.advance(5)
        self.assertEqual(self.video.position, 5)

    def test_that_negative_advances_is_rejected(self):
        with self.assertRaises(ValueError):
            self.video.advance(-5)
        self.assertEqual(self.video.position, 0)

    def test_that_multiple_advances_accumulates_and_moves_forward(self):
        self.video.advance(5)
        self.video.advance(5)
        self.assertEqual(self.video.position, 10)

    def test_that_advance_supports_fractional_minutes(self):
        self.video.advance(2.5)
        self.assertEqual(self.video.position, 2.5)

    def test_that_advance_by_zero_stands_at_zero(self):
        self.video.advance(0)
        self.assertEqual(self.video.position, 0)

    def test_that_advance_to_the_end_stands_exactly_at_the_end_of_the_video_duration(self):
        self.video.advance(10)
        self.assertEqual(self.video.position, 10)

    def test_that_advance_above_the_duration_stands_at_the_end_of_the_video_duration(self):
        self.video.advance(25)
        self.assertEqual(self.video.position, 10)

    def test_that_advance_ends_after_reaching_the_end_of_the_video_duration(self):
        self.video.advance(8)
        self.video.advance(6)
        self.assertEqual(self.video.position, 10)

    def test_that_video_is_not_finished_at_the_start_of_the_video(self):
        self.assertFalse(self.video.is_finished())

    def test_that_video_is_not_finished_midway_through_after_advancing_the_video(self):
        self.video.advance(5)
        self.assertFalse(self.video.is_finished())

    def test_that_video_is_not_finished_just_before_end_of_the_video_after_advancing_to_the_tail_end_of_the_video(self):
        self.video.advance(9.99)
        self.assertFalse(self.video.is_finished())

    def test_that_video_is_finished_at_exact_end_after_advancing_to_the_exact_end_of_the_video_duration(self):
        self.video.advance(10)
        self.assertTrue(self.video.is_finished())

    def test_that_video_is_finished_after_overshooting_the_advance_of_the_video(self):
        self.video.advance(50)
        self.assertTrue(self.video.is_finished())

    def test_that_video_is_not_finished_again_after_restarting_the_video(self):
        self.video.advance(10)
        self.video.restart()
        self.assertFalse(self.video.is_finished())

    def test_that_video_restart_after_resetting_to_beginning_of_the_video(self):
        self.video.advance(6)
        self.video.restart()
        self.assertEqual(self.video.position, 0)

    def test_that_video_restart_at_start_will_not_give_problem(self):
        self.video.restart()
        self.assertEqual(self.video.position, 0)

    def test_that_video_restart_keeps_the_title_and_duration_intact_after_advancing_and_restarting_the_video(self):
        self.video.advance(4)
        self.video.restart()
        self.assertEqual(self.video.title, "Love Me Like You Do")
        self.assertEqual(self.video.duration, 10)

    def test_that_video_can_advance_normally_after_the_restart_of_the_video(self):
        self.video.advance(8)
        self.video.restart()
        self.video.advance(2)
        self.assertEqual(self.video.position, 2)


    def test_that_time_remaining_equals_the_start_of_duration_of_the_video(self):
        self.video.time_remaining()
        self.assertEqual(self.video.time_remaining(), 10)

    def test_that_time_remaining_decreases_after_advancing_of_the_video(self):
        self.video.advance(5)
        self.assertEqual(self.video.time_remaining(), 5)

    def test_that_time_remaining_decreases_after_multiple_advancing_of_the_video(self):
        self.video.advance(5)
        self.video.advance(3)
        self.assertEqual(self.video.time_remaining(), 2)

    def test_that_time_remaining_resets_after_advancing_and_restarting_of_the_video(self):
        self.video.advance(5)
        self.video.advance(3)
        self.video.restart()
        self.assertEqual(self.video.time_remaining(), 10)

    def test_that_time_remaining_support_fractional_minutes_of_the_video(self):
        self.video.advance(3.5)
        self.video.advance(2.0)
        self.assertEqual(self.video.time_remaining(), 4.5)

    def test_that_time_remaining_is_zero_at_the_end_of_the_video(self):
        self.video.advance(5)
        self.video.advance(5)
        self.assertEqual(self.video.time_remaining(), 0)

    def test_that_time_remaining_is_zero_after_overshooting_the_video(self):
        self.video.advance(5)
        self.video.advance(5)
        self.video.advance(5)
        self.assertEqual(self.video.time_remaining(), 0)

    def test_that_time_remaining_does_not_change_the_position_of_the_video(self):
       self.video.advance(5)
       self.video.time_remaining()
       self.assertEqual(self.video.position, 5)



if __name__ == '__main__':
    unittest.main()
