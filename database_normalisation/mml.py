from dataclasses import dataclass
from math import log2, comb


@dataclass
class Table:
    unique_rows: int  # number of unique rows of entries by its primary keys
    pks: list[int]  # id of attributes as a primary key
    attributes: list[int]  # id of attributes present in the table


@dataclass
class PrimaryKeys:
    attributes: int
    primary_keys: int


def first_part_message_length(total_attributes: int, tables: list[Table]) -> float:
    """Computes the first part message length #H"""
    message_length = 0
    # Near-constant term for length of encoding of table and attributes, which
    # can be factored out
    # message_length += len(tables)
    # message_length += total_attributes

    # message length can contain the encoding of all total attributes
    # independent from the number of tables
    # message_length += log2(total_attributes)
    for table in tables:
        message_length += (
            # log(A) encoding of all total attributes
            # commented out since the encoding is counted above
            log2(total_attributes)
            +
            # log(A choose a_t) which attributes are in table t
            log2(comb(total_attributes, table.attributes.__len__()))
            +
            # log(a_t) encoding of attributes in table t
            # log2(table.attributes.__len__())
            # +
            # Another version of log(a_t)
            # if there is only one table, then it implies that the table
            # contains all attributes from the total attributes, therefore we
            # don't need to count the encoding of the table attributes
            # (log2(table.attributes.__len__()) if len(tables) > 1 else 0)
            # +
            # log(a_t choose p_t) which attributes are primary keys
            log2(comb(table.attributes.__len__(), table.pks.__len__()))
            # log(A choose p_t) encoding primary keys using total attributes
            # instead
            # +
            # log2(comb(total_attributes, table.pks.__len__()))
        )
    return message_length


def second_part_message_length(
    attribute_instances: list[int], tables: list[Table]
) -> float:
    """Computes the second part message length #A

    Attributes_instance is a list of unique instances for all attributes found
    within tables
    where attribute_instances[i] is the number of unique instances for ith
    attribute

    Args:
        attribute_instances (list[int]): list of attribute unique instances
        tables (list[Table]): list of tables that uses the same set of attributes

    Returns:
        float: second part message length
    """
    message_length = 0

    for table in tables:
        row_encoding_length = sum(
            # log2 m_x, encoding of unique instances of values for attribute x in table t
            log2(attribute_instances[x])
            for x in table.attributes
        )
        # row encoding length now represents the encoding  for one row
        # encode each rows in table using the length of such encoding
        message_length += table.unique_rows * row_encoding_length
    return message_length


def total_message_length(attribute_instances: list[int], tables: list[Table]):
    """Helper function to add first part and second part message length"""
    return first_part_message_length(
        total_attributes=len(attribute_instances), tables=tables
    ) + second_part_message_length(
        attribute_instances=attribute_instances, tables=tables
    )


def test_1nf(attribute_instances=[5, 5, 5, 5, 4, 4, 2, 2, 3, 3], L=11):
    """Test methods using Dowe & Zaidi 2010 Table 7 data"""

    tables = [
        Table(
            unique_rows=L,
            pks=[0, 4, 8],
            attributes=list(range(len(attribute_instances))),
        )
    ]
    return (
        "DZ-1NF",
        attribute_instances,
        tables,
        first_part_message_length(
            total_attributes=attribute_instances.__len__(), tables=tables
        ),
        second_part_message_length(
            attribute_instances=attribute_instances, tables=tables
        ),
        total_message_length(attribute_instances=attribute_instances, tables=tables),
    )


def test_2nf(attribute_instances=[5, 5, 5, 5, 4, 4, 2, 2, 3, 3], L=11):
    """Test methods using Dowe & Zaidi 2010 Table 7 data"""

    tables = [
        Table(
            unique_rows=attribute_instances[0],
            attributes=[0, 1, 2, 3, 6, 7],
            pks=[0],
        ),
        Table(
            unique_rows=attribute_instances[4],
            attributes=[4, 5],
            pks=[4],
        ),
        Table(
            unique_rows=L,
            attributes=[0, 4, 8, 9],
            pks=[0, 4, 8],
        ),
    ]
    return (
        "DZ-2NF",
        attribute_instances,
        tables,
        first_part_message_length(
            total_attributes=attribute_instances.__len__(), tables=tables
        ),
        second_part_message_length(
            attribute_instances=attribute_instances, tables=tables
        ),
        total_message_length(attribute_instances=attribute_instances, tables=tables),
    )


def test_3nf(attribute_instances=[5, 5, 5, 5, 4, 4, 2, 2, 3, 3], L=11):
    """Test methods using Dowe & Zaidi 2010 Table 7 data"""

    tables = [
        Table(
            unique_rows=attribute_instances[0],
            attributes=[0, 1, 2, 3, 6],
            pks=[0],
        ),
        Table(
            unique_rows=attribute_instances[4],
            attributes=[4, 5],
            pks=[4],
        ),
        Table(
            unique_rows=L,
            attributes=[0, 4, 8, 9],
            pks=[0, 4, 8],
        ),
        Table(unique_rows=attribute_instances[6], attributes=[6, 7], pks=[6]),
    ]
    return (
        "DZ-3NF",
        attribute_instances,
        tables,
        first_part_message_length(
            total_attributes=attribute_instances.__len__(), tables=tables
        ),
        second_part_message_length(
            attribute_instances=attribute_instances, tables=tables
        ),
        total_message_length(attribute_instances=attribute_instances, tables=tables),
    )


def mml(name: str, attribute_instances: list[int], tables: list[Table]):
    return (
        name,
        attribute_instances,
        tables,
        first_part_message_length(
            total_attributes=attribute_instances.__len__(), tables=tables
        ),
        second_part_message_length(
            attribute_instances=attribute_instances, tables=tables
        ),
        total_message_length(attribute_instances=attribute_instances, tables=tables),
    )


if __name__ == "__main__":
    test_1nf()
    test_2nf()
