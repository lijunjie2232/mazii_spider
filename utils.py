from omegaconf import OmegaConf


def to_dict(conf):
    return OmegaConf.to_object(conf)
