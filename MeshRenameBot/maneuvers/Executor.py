import asyncio
import logging
from .Default import DefaultManeuver

renamelog = logging.getLogger(__name__)

class Executor:
    def __init__(self, queue: asyncio.Queue, workerid: int) -> None:
        self.maneuvers_queue = queue
        self.workerid = workerid
        self._stop = False
        self._current_maneuver = None
        renamelog.info("Started executor with id {workerid} successfully".format(workerid=workerid))
        asyncio.get_event_loop().create_task(self.execute())

    async def execute(self) -> None:
        while not self._stop:
            maneuver = await self.maneuvers_queue.get()

            if maneuver.is_canceled:
                # Handle canceled maneuver
                continue
            elif maneuver.is_halted:
                # Requeue halted maneuver
                await self.maneuvers_queue.put(maneuver)
            else:
                self._current_maneuver = maneuver
                try:
                    await maneuver.execute()
                    maneuver.done()
                except Exception as e:
                    maneuver.done()
                    renamelog.exception("Execute failed: %s", str(e))
                self._current_maneuver = None

            await asyncio.sleep(3)

    def stop(self) -> None:
        if self._current_maneuver is not None:
            self._current_maneuver.cancel()
        
        self._stop = True
