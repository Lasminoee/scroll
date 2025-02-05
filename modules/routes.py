import random

from loguru import logger
from utils.sleeping import sleep
from .account import Account


class Routes(Account):
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll")

    async def start(self, use_modules: list, sleep_from: int, sleep_to: int, random_module: bool):
        logger.info(f"[{self.account_id}][{self.address}] Start using routes")

        run_modules = []

        for module in use_modules:
            if type(module) is list:
                run_modules.append(random.choice(module))
            elif type(module) is tuple:
                for _ in range(random.randint(module[1], module[2])):
                    run_modules.append(module[0])
            else:
                run_modules.append(module)

        if random_module:
            random.shuffle(run_modules)

        for module in run_modules:
            if module is None:
                logger.info(f"[{self.account_id}][{self.address}] Skip module")
                continue

            await module(self.account_id, self.private_key)

            await sleep(sleep_from, sleep_to)
