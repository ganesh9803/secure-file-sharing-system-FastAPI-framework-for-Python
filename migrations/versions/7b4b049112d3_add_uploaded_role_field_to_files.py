"""Add uploaded_role field to files

Revision ID: 7b4b049112d3
Revises: bd751b04fe92
Create Date: 2024-11-18 20:08:53.188134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b4b049112d3'
down_revision: Union[str, None] = 'bd751b04fe92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
