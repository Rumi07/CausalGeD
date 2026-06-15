from . import gaussian_diffusion as gd
from .respace import SpacedDiffusion, space_timesteps


def create_diffusion(timestep_respacing, sigma_small=False, diffusion_steps=1000):
    betas = gd.get_named_beta_schedule(diffusion_steps)
    if timestep_respacing is None or timestep_respacing == "":
        timestep_respacing = [diffusion_steps]
    return SpacedDiffusion(
        use_timesteps=space_timesteps(diffusion_steps, timestep_respacing),
        betas=betas,
        model_var_type=(
            gd.ModelVarType.FIXED_LARGE 
            if not sigma_small 
            else gd.ModelVarType.FIXED_SMALL
        )
    )
