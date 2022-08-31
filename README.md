# loggy

## Description

loggy makes logs more readable.

## Example

    cat test.txt

it turns

    2022-08-31 12:55:16,826 - werkzeug - INFO - 172.16.105.103 - - [31/Aug/2022 12:55:16] "GET /workspaces?where=%7B%22$and%22:%20%5B%7B%22$or%22:%20%5B%7B%22state%22:%20%22DELETING%22%7D,%20%7B%22state%22:%20%22FAILING%22%7D%5D%7D,%20%7B%22type%22:%20%22625ea4d52339664183373d47%22%7D%5D%7D HTTP/1.1" 200 -

with

    tail -f test.txt | python3 loggy.py --urlunquote --ppjson

into

    2022-08-31 12:55:16,826 - werkzeug - INFO - 172.16.105.103 - - [31/Aug/2022 12:55:16] "GET /workspaces?where={"$and": [{"$or": [{"state": "DELETING"}, {"state": "FAILING"}]}, {"type": "625ea4d52339664183373d47"}]} HTTP/1.1" 200 -

    {
        "$and": [
            {
                "$or": [
                    {
                        "state": "DELETING"
                    },
                    {
                        "state": "FAILING"
                    }
                ]
            },
            {
                "type": "625ea4d52339664183373d47"
            }
        ]
    }
