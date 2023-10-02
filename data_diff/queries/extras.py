"Useful AST classes that don't quite fall within the scope of regular SQL"
from typing import Callable, Sequence
from runtype import dataclass

from data_diff.abcs.database_types import ColType

from data_diff.queries.ast_classes import Expr, ExprNode


@dataclass
class NormalizeAsString(ExprNode):
    expr: ExprNode
    expr_type: ColType = None
    type = str


@dataclass
class ApplyFuncAndNormalizeAsString(ExprNode):
    expr: ExprNode
    apply_func: Callable = None


@dataclass
class Checksum(ExprNode):
    exprs: Sequence[Expr]