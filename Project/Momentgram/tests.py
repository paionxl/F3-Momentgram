# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, Client
from django.contrib.auth.models import User
from Momentgram.models import Post, Message


# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("Albert", "albert.sola9@gmail.com", "admin1234")
        User.objects.create_user("Manuel", "manuel.lecha@gmail.com", "manu")
        User.objects.create_user("Jordi", "jordi@gmail.com", "idroj")
        User.objects.create_user("Joan", "joan@gmail.com", "j12345")
        User.objects.create_user("Ling", "ling@gmail.com", "lingling")
        User.objects.create_user("Carlos", "carlos_arenas@gmail.com", "esfw")
        self.client = Client()

    # Returns correct login
    def test_login_user(self):
        self.assertTrue(self.client.login(username="Albert", password="admin1234"))

    # Returns incorrect login
    def test_wrong_password(self):
        return self.assertFalse(self.client.login(username="Albert", password=""))

    def test_profile_content(self):
        user = User.objects.get(username="Albert")
        expected_user_name = f'{user.username}'
        self.assertEqual(expected_user_name,"Albert")


class PostTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("Albert", "albert.sola9@gmail.com", "admin1234")
        Post.objects.create(description="test description",
                            image="media/images/GoldenGateBridge_BakerBeach_MC.jpg",
                            user=User.objects.get(username="Albert"))

    #Returns correct content after uploading a post
    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_object_description = f'{post.description}'
        expected_object_user = f'{post.user}'
        expected_object_image = f'{post.image}'
        self.assertEqual(expected_object_description, "test description")
        self.assertEqual(expected_object_user, "Albert")
        self.assertEqual(expected_object_image, "media/images/GoldenGateBridge_BakerBeach_MC.jpg")


class FollowTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("Albert", "albert.sola9@gmail.com", "admin1234")
        User.objects.create_user("Manuel", "manuel.lecha@gmail.com", "manu")
        User.objects.create_user("Jordi", "jordi@gmail.com", "idroj")
        User.objects.create_user("Joan", "joan@gmail.com", "j12345")
        User.objects.create_user("Ling", "ling@gmail.com", "lingling")
        User.objects.create_user("Carlos", "carlos_arenas@gmail.com", "esfw")

    #TODO tests with followers and following


class MessagesTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("Albert", "albert.sola9@gmail.com", "admin1234")
        User.objects.create_user("Manuel", "manuel.lecha@gmail.com", "manu")
        Message.objects.create(sender= User.objects.get(username="Albert"),
                               receiver= User.objects.get(username="Manuel"),
                               text= "Holaaa :D")
        Message.objects.create(sender=User.objects.get(username="Manuel"),
                               receiver=User.objects.get(username="Albert"),
                               text="Hello!")
        Message.objects.create(sender=User.objects.get(username="Manuel"),
                               receiver=User.objects.get(username="Albert"),
                               text="Porque no contestas D:")
        Message.objects.create(sender=User.objects.get(username="Manuel"),
                               receiver=User.objects.get(username="Albert"),
                               text="xd")

    def test_message_content(self):
        message = Message.objects.get(sender=User.objects.get(username="Albert"))
        expected_text = f'{message.text}'
        expected_receiver = f'{message.receiver}'
        expected_sender = f'{message.sender}'
        self.assertEqual(expected_sender,"Albert")
        self.assertEqual(expected_receiver,"Manuel")
        self.assertEqual(expected_text,"Holaaa :D")

    def test_number_of_messages(self):
        #TODO when utils is uploaded