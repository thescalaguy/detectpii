from .plaintext import PlaintextResolver
from .environment import EnvironmentResolver

ResolverT = PlaintextResolver | EnvironmentResolver
