from mml import *


def ct_3nf(attribute_instances, table):
    """Test methods using Dowe & Zaidi 2010 Table 7 data"""

    tables = [
        Table(
            unique_rows=count_unique_rows(table, [0, 1, 2]),
            attributes=[0, 1, 2],
            pks=[0, 1, 2]
        )
    ]
    return (
        "ct-3nf",
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


def ct_4nf(attribute_instances, table):
    """Test methods using Dowe & Zaidi 2010 Table 7 data"""

    tables = [
        Table(
            unique_rows=count_unique_rows(table, [0, 1]),
            attributes=[0, 1],
            pks=[0, 1]
        ),
        Table(
            unique_rows=count_unique_rows(table, [1, 2]),
            attributes=[1, 2],
            pks=[1, 2]
        )
    ]
    return (
        "ct-4nf",
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


def ct_5nf(attribute_instances, table):
    """Test methods using Dowe & Zaidi 2010 Table 7 data"""

    tables = [
        Table(
            unique_rows=count_unique_rows(table, [0, 1]),
            attributes=[0, 1],
            pks=[0, 1]
        ),
        Table(
            unique_rows=count_unique_rows(table, [1, 2]),
            attributes=[1, 2],
            pks=[1, 2]
        ),
        Table(
            unique_rows=count_unique_rows(table, [1, 2]),
            attributes=[1, 2],
            pks=[0, 2]
        )
    ]
    return (
        "ct-5nf",
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


def count_unique_rows(table: list[list[int]], pks: list[int]):
    result = set()
    for row in table:
        key = [row[pk] for pk in pks]
        result.add(tuple(key))
    return len(result)


def count_unique_attribute_instances(table: list[list[int]]):
    return [count_unique_rows(table, [i]) for i in range(len(table[0]))]

