import os
import pytest
from model.creature import Creature
from error import Missing, Duplicate

# 아래 줄에 있는 data.init에 DB를 사용하도록 data 모듈을 가져오기 전에 설정한다.
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
# data 모듈이 중복돼 creature 찾지 못해 src를 명시한다.
from data import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        description="harmless Himalayan",
        country="CN",
        area="Himalayas",
        aka="Abominable Snowman"
        )

def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)

def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = creature.get_one("boxturtle")

def test_modify(sample):
    resp = creature.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    thing: Creature = Creature(name="snurfle", country="RU", area="", description="some thing", aka="")
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)

def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)