from sqlalchemy import Table, Column,  Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User_orders(Base):
    __tablename__ = 'users_orders'

    id  = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    user = relationship('User', back_populates = 'users_orders')
    product = relationship('Product', back_populates = 'users_orders')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    coupon_id = Column(Integer, ForeignKey("coupons.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    quantity = Column(Integer, nullable=False)

    coupon = relationship("Coupon", back_populates='products')
    category = relationship("Category", back_populates='products')
    user = relationship('User', back_populates='products')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    products = relationship('Product', back_populates='users')
    
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    name = Column(String, nullable=False)

    product = relationship('Product', back_populates='categories')

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    name = Column(String, nullable=False)

    product = relationship("Product", back_populates='coupons')

# Нужно саваязать между собой все таблицы правильными связями например: coupon-product - 1:m, category-product 1:m, user-product m:m
#  