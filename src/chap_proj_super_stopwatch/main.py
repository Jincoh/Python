import time

import logging
logging.basicConfig(level=logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        start = time.time()
        nolaps = 0
        while(True):
            ts = time.time()
            inp = input(f"{"=" * 43}\n  press enter to lap press ctrl c to exit\n{"=" * 43}")
            logging.debug(f"start = '{start}', ts = '{ts}', inp = '{inp}', nolaps = '{nolaps}'")
            if inp == "":
                nolaps +=1
                lap = time.time()
                print(f"""   
   + lap time: {round(lap - ts, 2)}
   + time since start: {round(lap - start, 2)}
   + No. laps: {nolaps}
""")

    except KeyboardInterrupt:
        print()
        return
        


if __name__ == "__main__":
    main()
