from .environment import EnvironmentResolver
from .plaintext import PlaintextResolver

ResolverT = PlaintextResolver | EnvironmentResolver
