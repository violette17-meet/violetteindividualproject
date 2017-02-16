# -*- coding: utf-8 -*-

from database import *
from sqlalchemy import Column,Integer,String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine , func , DateTime

Base = declarative_base()
engine = create_engine('sqlite:///forum.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


el =Makeup(name='ever lasting drama eyeliner',company='maybelline',description=' This waterproof and smudge-resistant gel eyeliner glides on smooth for impactful definition. All-day wear. Ophthalmologist tested.Dermatologist tested. Suitable for sensitive eyes and contact lens wearers.',picture='https://img.makeupalley.com/6/1/7/6/2270551.JPG', website='http://www.ulta.com/eye-studio-master-precise-liquid-eyeliner?productId=xlsImpprod4070011')
session.add(el)
session.commit()

rlm = Makeup(name='roller lash mascara',company='benefit',description='Its a roller for lashes! The eye-opening Hook n Roll brush grabs, separates, lifts and curls while the instant curve-setting formula holds for 12 hours. Contains provitamin B5 and serin, ingredients known for their lash-conditioning benefits. Available in two stunning shades, original ink black or brown.',picture='http://hbz.h-cdn.co/assets/16/22/480x720/hbz-mascara-benefit_rollerlash_900x900.jpg', website='https://www.benefitcosmetics.com')
session.add(rlm)
session.commit()

rmlp = Makeup(name='laura murcier loose powder',company='laura mercier',description='Mineral pearl powder instantly brightens skin with a natural, healthy radiance. Light-reflecting minerals in the weightless loose powder blend flawlessly to create a soft-focus effect that subtly perfects and flatters your look. The perfect complement to eyes, cheeks, and face.',picture='http://i.ebayimg.com/images/g/eZIAAOSwiCRUitfe/s-l300.jpg', website='http://www.lauramercier.com/create-a-finish/mineral-illuminating-powder-prod170006.html#cm_re=12617-_-homepage+glow+all+out+-_-highlighter-illuminator+&start=9')
session.add(rmlp)
session.commit()

abhck = Makeup(name='anastassia beverly hills contour kit',company='abh',description='A best-selling set of three powder highlight and three powder contour shades. Use Anastasia Beverly Hills Contour Powder Kit to create the illusions of higher cheekbones, a slimmer nose, softer jawline, or smaller forehead.Blendable satin finish Removable and refillable set Can be layered over Contour Cream Kit to intensify results Available in 3 shades',picture='http://www.sephora.com/images/sku/s1615186-main-hero.jpg', website='http://www.anastasiabeverlyhills.com/makeup-contour-kit/contour-kit.html')
session.add(abhck)
session.commit()

mb = Makeup(name='morphe brushes',company='morphe',description="Morphe Brushes offer the must-have beauty tools and palettes that are Californias answer to effortless beauty." ,picture='https://s-media-cache-ak0.pinimg.com/originals/70/5c/81/705c8192c034ed68d2ba6ddd3bce8be4.jpg', website='https://www.morphebrushes.com/collections/brushes')
session.add(mb)
session.commit()

